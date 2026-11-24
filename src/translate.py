# /// script
# requires-python = ">=3.13"
# dependencies = ["anthropic", "pyyaml"]
# ///
"""Translate posts and pages of the living literature review into German.

The English files are the source of truth. Each German file stores a hash of the
English file it was made from (`source-hash`), so a translation is only redone when
the English original changed.

Usage (from the repository root):
    uv run src/translate.py              # translate everything missing or outdated
    uv run src/translate.py --dry-run    # only list what would be translated
    uv run src/translate.py --only 2022-08-29-potatoes.md
    uv run src/translate.py --limit 3    # translate at most three files
    uv run src/translate.py --stamp      # mark existing translations as up to date

Needs an Anthropic API key (ANTHROPIC_API_KEY) or a profile from `ant auth login`.
"""

import argparse
import hashlib
import re
from pathlib import Path

import anthropic
import yaml

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
DE_POSTS_DIR = ROOT / "_de"
DE_PAGES_DIR = ROOT / "de"
# English pages with a German version (references.md is mirrored at build time)
PAGES = [
    "overview.md",
    "factors.md",
    "resilience.md",
    "casestudies.md",
    "how_to_cite.md",
    "further.md",
    "aboutme.md",
]
MODEL = "claude-opus-5-5"

SYSTEM_PROMPT = """\
You translate blog posts of a living literature review on societal collapse from \
English into German. The author is Florian Ulrich Jehn, a researcher on global \
catastrophic risk. The German version is published as an automatic translation; \
the English original stays the source of truth.

How to translate:
- Keep the author's voice: casual, direct, first person, dry understatement. Address \
readers with "du" where the English says "you". Write natural German, not \
word-for-word German. Keep the meaning exactly; do not add, cut or soften anything.
- Use the German terms that are normal in the field (e.g. "Kipppunkt", "nuklearer \
Winter", "Resilienz"). Keep English terms where German researchers would too.
- Keep the Markdown structure exactly: headings, lists, emphasis, tables, footnotes, \
line breaks between paragraphs.
- Keep every URL, image path, HTML tag, Liquid tag ({% ... %}, {{ ... }}) and code \
unchanged. Translate link texts and image alt texts.
- Do not translate titles of books, papers or podcasts, names, or reference lists. \
Keep citations such as "(Kemp et al., 2022)" as they are.
- Numbers: German decimal comma, space before % and units (e.g. "2,5 %", "2 °C").
- If the text ends with a "How to cite" section: translate the heading as \
"Zitieren", put the line "Bitte das englische Original zitieren:" under it and keep \
the citation itself unchanged.
- Do not add a note that this is a translation; the website adds that itself.

Answer with exactly three parts and nothing else:
<title>German title</title>
<subtitle>German subtitle, or empty</subtitle>
<body>
German body in Markdown
</body>"""


def file_hash(path):
    """Hash an English source file.

    Arguments:
        path (Path): file to hash
    Returns:
        str: first 16 hex characters of the SHA-256 of the file
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def split_front_matter(text):
    """Split a Jekyll file into front matter and body.

    Arguments:
        text (str): full file content
    Returns:
        tuple[dict, str]: parsed front matter and the body after it
    """
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    return yaml.safe_load(match.group(1)) or {}, match.group(2)


def jobs():
    """List all English files with the path of their German version.

    Returns:
        list[tuple[Path, Path, str]]: (English file, German file, kind)
    """
    found = [(p, DE_POSTS_DIR / p.name, "post") for p in sorted(POSTS_DIR.glob("*.md"))]
    for name in PAGES:
        found.append((ROOT / name, DE_PAGES_DIR / name, "page"))
    return found


def is_outdated(source, target):
    """Check whether a German file is missing or older than its English source.

    Arguments:
        source (Path): English file
        target (Path): German file
    Returns:
        bool: True if the translation has to be (re)done
    """
    if not target.exists():
        return True
    meta, _ = split_front_matter(target.read_text(encoding="utf-8"))
    return meta.get("source-hash") != file_hash(source)


def translate(client, title, subtitle, body):
    """Translate one post or page with Claude.

    Arguments:
        client (anthropic.Anthropic): API client
        title (str): English title
        subtitle (str): English subtitle (may be empty)
        body (str): English Markdown body
    Returns:
        tuple[str, str, str]: German title, subtitle and body
    """
    user = (
        f"<title>{title}</title>\n<subtitle>{subtitle}</subtitle>\n"
        f"<body>\n{body}\n</body>"
    )
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=64000,
        system=SYSTEM_PROMPT,
        output_config={"effort": "medium"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": user}],
    ) as stream:
        message = stream.get_final_message()
    if message.stop_reason == "refusal":
        raise RuntimeError("the model declined to translate this text")
    if message.stop_reason == "max_tokens":
        raise RuntimeError("the translation was cut off (max_tokens)")
    text = "".join(b.text for b in message.content if b.type == "text")

    def part(tag):
        match = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        if match is None:
            raise RuntimeError(f"no <{tag}> in the answer")
        return match.group(1).strip()

    return part("title"), part("subtitle"), part("body")


def german_front_matter(meta, source, kind, title, subtitle):
    """Build the front matter of the German file.

    Arguments:
        meta (dict): front matter of the English file
        source (Path): English file
        kind (str): "post" or "page"
        title (str): German title
        subtitle (str): German subtitle
    Returns:
        str: YAML front matter including the --- lines
    """
    out = {k: v for k, v in meta.items() if k not in ("title", "subtitle")}
    out["title"] = title
    if subtitle:
        out["subtitle"] = subtitle
    if kind == "page":
        out["permalink"] = f"/de/{source.stem}/"
    out["source"] = source.name
    out["source-hash"] = file_hash(source)
    dumped = yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=1000)
    return f"---\n{dumped}---\n"


def stamp(target, source):
    """Write the current source hash into an existing German file.

    Arguments:
        target (Path): German file
        source (Path): English file
    Returns:
        None
    """
    text = target.read_text(encoding="utf-8")
    line = f"source-hash: {file_hash(source)}"
    if re.search(r"^source-hash:.*$", text, re.MULTILINE):
        text = re.sub(r"^source-hash:.*$", line, text, count=1, flags=re.MULTILINE)
    else:
        text = text.replace("\n---", f"\nsource: {source.name}\n{line}\n---", 1)
    target.write_text(text, encoding="utf-8")


def main():
    """Translate everything that is missing or outdated."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="only list the files")
    parser.add_argument("--only", help="file name of one English post or page")
    parser.add_argument("--limit", type=int, help="translate at most this many")
    parser.add_argument(
        "--stamp", action="store_true", help="mark existing translations up to date"
    )
    args = parser.parse_args()

    todo = [j for j in jobs() if args.only in (None, j[0].name)]
    if args.stamp:
        for source, target, _ in todo:
            if target.exists():
                stamp(target, source)
                print(f"stamped {target.relative_to(ROOT)}")
        return

    todo = [j for j in todo if is_outdated(j[0], j[1])]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(todo)} file(s) to translate")
    if args.dry_run:
        for source, target, _ in todo:
            print(f"  {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        return

    client = anthropic.Anthropic()
    for i, (source, target, kind) in enumerate(todo, 1):
        print(f"[{i}/{len(todo)}] {source.relative_to(ROOT)}")
        meta, body = split_front_matter(source.read_text(encoding="utf-8"))
        try:
            title, subtitle, body_de = translate(
                client, meta.get("title", ""), meta.get("subtitle", ""), body
            )
        except anthropic.RateLimitError as err:
            print(f"  rate limited, stopping here: {err}")
            break
        except anthropic.APIStatusError as err:
            print(f"  API error {err.status_code}, skipped: {err.message}")
            continue
        except anthropic.APIConnectionError as err:
            print(f"  connection error, skipped: {err}")
            continue
        except RuntimeError as err:
            print(f"  skipped: {err}")
            continue
        target.parent.mkdir(exist_ok=True)
        front = german_front_matter(meta, source, kind, title, subtitle)
        target.write_text(front + "\n" + body_de + "\n", encoding="utf-8")
        print(f"  wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
