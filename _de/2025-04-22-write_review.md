---
title: Wie man einen fortlaufenden Literaturüberblick schreibt
subtitle: Paper finden, Ideen entwickeln, schreiben und veröffentlichen
tags: [Further Reading, Meta]
readtime: true
source: 2025-04-22-write_review.md
source-hash: db5129cd8c3a1e51
---

Wie schreibt man also eigentlich einen fortlaufenden Literaturüberblick? In den über zwei Jahren, in denen ich das hier schreibe (die Zeit vergeht wirklich schnell), werde ich manchmal gefragt, wie ich beim Schreiben der Beiträge vorgehe. Mit diesem Beitrag will ich diese Frage beantworten. Er dreht sich zwar um einen fortlaufenden Literaturüberblick, aber ich glaube, diese Notizen sind wahrscheinlich für alle hilfreich, die zumindest etwas wissenschaftlich schreiben müssen oder das in Zukunft mehr tun wollen. Außerdem ist zumindest das erste Drittel des Beitrags genau das Vorgehen, mit dem ich auch wissenschaftliche Paper schreibe.

# Relevante Literatur finden

Ich glaube, der wichtigste Teil des Prozesses ist, relevante Paper zu finden, die man lesen und über die man schreiben kann. Das ist schwieriger, als man denkt. Wenn man in einer hochspezialisierten Disziplin arbeitet, kann man oft einfach sein Lieblingsthema auf ArXiv abonnieren, und alles ist gut. Sobald man aber interdisziplinär arbeitet (was dieser fortlaufende Literaturüberblick eindeutig tut), hat man das Problem, dass es keinen offensichtlichen Ort gibt, an dem man nach Papern suchen kann. Mit der Zeit habe ich ein paar Orte gefunden, die vernünftige Ergebnisse liefern, aber wenn man auf interdisziplinärer Reise ist, muss man einfach akzeptieren, dass die Quote falscher Treffer bei den Papern, die man sich anschaut, immer ziemlich hoch sein wird. Im Folgenden beschreibe ich kurz, wie man relevante Literatur finden kann.

# Gute Suchbegriffe nutzen

Bevor wir uns die verschiedenen Dienste anschauen, ein Punkt vorab. Bei vielen dieser Dienste muss man festlegen, nach welcher Art von Forschung man sucht. Dabei muss man den schmalen Grat zwischen zu allgemein und zu spezifisch treffen. Man muss einen Suchbegriff finden, der in der Forschung zum gewünschten Thema verwendet wird, der aber nicht so obskur ist, dass man Tausende Alerts einrichten muss, um ein Paper pro Woche zu bekommen. Andererseits wird man mit E-Mails überschwemmt, wenn man so etwas wie „climate change“ als Suchbegriff nimmt. Ein Beispiel für einen Suchbegriff mit der richtigen Spezifität, der regelmäßig Ergebnisse liefert, mich aber nicht mit Alerts überflutet, ist „Global Food Trade“. Zu breit wäre „Global Trade“, zu spezifisch „Global Wheat Trade“.

Bisher habe ich zwei gute Wege gefunden, um diese genau richtigen Suchbegriffe zu finden:
* Gib dem Sprachmodell deiner Wahl ein paar Paper und frag es, welche Suchbegriffe gut wären, wenn man nach ähnlicher Forschung sucht.
* Such auf [OpenAlex](https://openalex.org/) nach Papern, die du interessant findest (mehr zu OpenAlex weiter unten). Wenn du die Ergebnisse deiner Suche hast, kannst du dort einen Reiter mit Schlagwörtern hinzufügen. Das sind Schlagwörter, die OpenAlex auf Grundlage seiner eigenen bibliometrischen Analyse automatisch erzeugt. Sie erfassen oft ziemlich gut die Ideen, nach denen man sucht, und man kann damit weitersuchen.

## [Google Scholar](https://scholar.google.com/)-Alerts

Google Scholar versucht, einen großen Teil der wissenschaftlichen Literatur zu indexieren. Es hat zwar ein paar blinde Flecken (zum Beispiel indexiert es [Zenodo](https://zenodo.org/) nicht), findet aber meistens gut Paper. Wenn man ein Profil bei Google Scholar hat, kann man Alerts einrichten. Dann bekommt man jedes Mal eine E-Mail, wenn Google Scholar ein neues Paper findet, das den angegebenen Suchbegriff erwähnt.

## [Research Gate](https://www.researchgate.net/)

Research Gate ist eine Webseite, auf der Forschende ihre Arbeit teilen und sich mit anderen Forschenden vernetzen. Im Home-Reiter bekommt man Paper angezeigt, die einen interessieren könnten. Der Algorithmus funktioniert meiner Erfahrung nach oft ziemlich gut, ist nur mühsam zu trainieren. Er beruht auf den Papern, die man hochgeladen hat, den Leuten, denen man folgt, und den Papern und Themen, mit denen man sich bisher beschäftigt hat. Es macht also etwas Arbeit, all diese Infos einzugeben und interessante Forschende zum Folgen zu finden, aber wenn das erledigt ist, tauchen dort manchmal Paper auf, die ich nirgendwo anders finde.

## [OpenAlex](https://openalex.org/)

OpenAlex ist ein bibliografischer Katalog wissenschaftlicher Paper. Er ähnelt anderen Katalogen wie Web of Science, hat aber den großen Vorteil, dass er komplett kostenlos und für alle verfügbar ist. Man kann direkt auf der Webseite suchen, es gibt aber auch eine API, über die man Paper abfragen kann. Um das einfacher zu machen, habe ich [etwas Code](https://github.com/florianjehn/OpenAlex-Paper-Request) geschrieben (danke, Claude), um die API abzufragen. Damit kann man Paper zu bestimmten Themen in einem festgelegten Zeitraum abfragen und bekommt eine schöne CSV-Datei, die man durchgehen kann, um zu schauen, ob man interessante Paper gefunden hat.

## Newsletter von Forschungsorganisationen
Das ist ziemlich selbsterklärend. Forschungsorganisationen geben gern mit dem an, was sie veröffentlichen. Also such dir die Newsletter der Forschungsorganisationen, die du magst, und abonnier sie.

## [TERRA](https://www.cser.ac.uk/work/the-existential-risk-research-assessment-terra/) (leider eingestellt)

Das [CSER](https://www.cser.ac.uk/) hatte ein Werkzeug, das versucht hat, automatisch Paper zu finden, die für globale katastrophale Risiken relevant sind. Leider wurde es vor Kurzem eingestellt, und man kann nur noch die bisherigen Ergebnisse herunterladen. Da sind aber trotzdem noch viele Perlen dabei.

## Auf Konferenzen gehen

Such dir große, interdisziplinäre Konferenzen und schau dir so viele wissenschaftliche Poster an, wie du nur kannst. Natürlich ist die Fehlerquote hier ziemlich hoch, aber so bekommt man auch die neueste Forschung mit und weiß, auf welche Paper man in nicht allzu ferner Zukunft achten sollte, und man kann sich leicht ein paar Hundert Poster in wenigen Stunden anschauen.

## Ins Literaturverzeichnis schauen

Wissenschaftliche Paper verweisen für ihre Aussagen auf andere Paper. Wenn du eine Aussage interessant fandest, such einfach das zitierte Paper heraus.

## Bestimmte Paper finden
Manchmal hat man schon eine Ahnung, welche Art von Papern man sucht, etwa wenn es eine Lücke in einem Argument gibt, die von einem passenden Zitat profitieren würde. Auch dafür gibt es ein paar sehr hilfreiche Werkzeuge:
* [Elicit](https://elicit.com/): Eine Suchmaschine, die darauf optimiert ist, die Paper zu finden, die man braucht, und die auch das Herausziehen von Informationen automatisieren kann. Frag einfach, was dich interessiert, und sie versucht, Paper zu finden, die deine Fragen beantworten. Sie ist ein bisschen auf medizinische Paper optimiert, kann aber meiner Erfahrung nach auch für viele andere Felder ziemlich hilfreich sein.
* [Connected Papers](https://www.connectedpapers.com/): Dieses Werkzeug nutzt man vor allem, um das Netz von Papern rund um ein bestimmtes Paper zu finden. Man gibt den Namen eines Papers ein, das man interessant findet, und bekommt ein Netzwerk relevanter Paper. Die Auswahl beruht auf Ähnlichkeit, die berechnet wird, indem geprüft wird, ob sich Paper in ihren Zitaten und Quellen überschneiden.
* [Research Rabbit](https://researchrabbitapp.com/): Eine Art Mischung aus den beiden anderen Werkzeugen. Damit kann man im Netzwerk der Paper suchen, die man angegeben hat.

# Lesen und Notizen machen
Gut, jetzt hast du einen großen Stapel Paper, die dich interessieren könnten, aber du musst sie noch lesen. Es kann knifflig sein, ein Setup zu finden, mit dem man bequem viele Paper lesen kann (zumindest war es das für mich). Inzwischen habe ich aber einen Arbeitsablauf, mit dem ich Paper leicht lesen und die Informationen trotzdem ohne viel Zusatzaufwand herausziehen kann:

* Die Paper zu [Zotero](https://www.zotero.org/) hinzufügen: Zotero ist ein großartiges, kostenloses Werkzeug, um zu organisieren, was man lesen will. Es holt automatisch alle Metadaten zum Paper, und man kann Paper sogar direkt aus dem Browser hinzufügen.
* Die Paper auf das Lesegerät bringen: Ich nutze ein [Boox Note Air 2](https://euroshop.boox.com/collections/e-ink-tablets/products/noteair2promo?variant=42340358979784). Ich mag diese Geräte, weil sie ein E-Ink-Display haben, aber unter der Haube sind sie einfach normale Android-Tablets, sodass alle normalen Apps funktionieren. Du kannst aber jedes Gerät nehmen, auf dem du gerne liest, solange man darauf Notizen machen kann. Um die Paper aufs Tablet zu bekommen, habe ich einfach einen Ordner auf meinem Computer, der mit dem Tablet synchronisiert wird. Um die Paper in den Ordner zu bekommen, nutze ich die Erweiterung [Attanger](https://github.com/MuiseDestiny/zotero-attanger) für Zotero.
* Die Paper lesen und kommentieren: Auf dem Boox kann ich einfach alles im Paper unterstreichen, was ich interessant finde, und handschriftliche Notizen an den Rand kritzeln. Wenn ich ein Paper fertig habe, synchronisiere ich es zurück auf meinen Computer. Ich wähle die Paper nach dem Datum aus, an dem sie hinzugefügt wurden, also wer zuerst kommt, wird zuerst gelesen.
* Die Notizen aus dem Paper holen: Zotero kann automatisch alles herausziehen, was man in einem PDF unterstrichen hat, also mache ich genau das.
* Die Notizen dauerhaft machen: Um seine Notizen nutzen zu können, braucht man einen festen Ort für sie, an dem man sie leicht mit anderen Dingen verbinden kann, die man schreibt. Dafür nutze ich [Logseq](https://logseq.com/). In Logseq kann man Paper direkt aus Zotero importieren. Dann entsteht eine neue Seite für das Paper, auf der der ganze unterstrichene Text direkt eingefügt ist. Auf dieser Seite ordne ich dann die Notizen und schreibe all meine handschriftlichen Notizen ab. Ich füge auch Tags hinzu, um Dinge später leichter zu finden. Außerdem tagge ich gezielt alle Paper, aus denen meiner Meinung nach ein guter Beitrag werden könnte, und verlinke sie mit anderen Papern zu dem Thema. In Logseq kann man seine Notizen abfragen. Ich nutze diese Funktion, um automatisch eine Liste aller Ideen für Beiträge zu erstellen, die ich irgendwo in meinen Notizen aufgeschrieben habe.

# Auf Ideen kommen

Wenn du all diese Schritte gemacht hast, um Paper zu finden, zu lesen und zu verarbeiten, hast du meiner Meinung nach schon das Wichtigste getan, was man tun kann, um auf Ideen zum Schreiben zu kommen. Denn meiner Erfahrung nach hängt die Zahl der Ideen, die man hat, sehr direkt davon ab, wie viele Paper man liest. Das mag offensichtlich klingen, war es für mich aber nicht, als ich angefangen habe, Wissenschaftler zu werden (und niemand hat sich die Mühe gemacht, es mir zu sagen). Ich glaube, das liegt daran, dass meiner Erfahrung nach viele Wissenschaftler einfach nicht so viel lesen und deshalb nie merken, was ihnen entgeht. Ich habe angefangen, mehr zu lesen, nachdem ich meine Promotion abgeschlossen hatte, weil mir aufgefallen ist, dass ich nicht viele gute Forschungsideen hatte. Auf meiner Suche danach, wie man bessere Ideen bekommt, bin ich auf das Buch „[Constructing Research Questions](https://www.goodreads.com/book/show/17323972-constructing-research-questions)“ von Mats Alvesson und Jörgen Sandberg gestoßen. Ich gehe hier nicht ins Detail, weil ich schon eine Zusammenfassung [hier](https://florianjehn.github.io/Societal_Collapse/2023-02-03-gap_spotting/) geschrieben habe, aber die Kernaussage des Buchs ist: „Du musst mehr lesen! Wenn du glaubst, dass du genug liest, lies mehr! Wenn du glaubst, dass du zu viel liest, stimmt das nicht, lies lieber mehr.“ Und ich finde, das trifft es genau. Denn wenn man gute Ideen haben will, muss man wissen, was andere schon gemacht haben, in welche Richtung sich das eigene Feld entwickelt, welche Techniken und Methoden es gibt und welche großen Fragen die Leute umtreiben. Der einzige Weg, verlässlich an diese Informationen zu kommen, ist, verdammt viele Paper zu lesen. So ziemlich alle guten Ideen, die ich hatte, kann ich darauf zurückführen, dass ich einfach mehr gelesen habe, und ich glaube, einfach mehr zu lesen ist eine Fähigkeit, die viele Wissenschaftler zu wenig nutzen. Alle Beiträge in meinem fortlaufenden Literaturüberblick haben als Notizen begonnen, die auf PDFs gekritzelt waren. Dasselbe gilt für alle Paper, die ich seit meiner Promotion geschrieben habe.

# Einen Beitrag schreiben

Das ist eigentlich der einfachste Teil, weil man die harte Arbeit in den vorherigen Schritten schon erledigt hat. Ich schaue mir einfach die automatisch erstellte Liste mit Ideen für Beiträge in Logseq an und suche mir eine aus, die mich an dem Tag reizt. Dann schaue ich mir kurz alle Notizen zu den relevanten Papern an und skizziere eine Gliederung meines Arguments. In vielen Fällen kann ich meine vorher gemachten Notizen fast eins zu eins verwenden. Wenn ich einen ersten Entwurf habe, schicke ich ihn meist an eine der Personen, deren Paper ich zusammengefasst habe, und bitte um Feedback. Darauf bekomme ich meistens eine positive Antwort, weil Leute es mögen, wenn man sich für ihre Arbeit interessiert, und einem gerne sagen, wo man ihr Argument oder ihre Technik vielleicht missverstanden hat. Sobald ich das Feedback eingearbeitet habe, plane ich den Beitrag zur Veröffentlichung ein.

# Technisches Setup

Um meine Beiträge zu verbreiten, habe ich zwei getrennte Systeme. GitHub Pages als dauerhaftes Archiv meiner Beiträge und Substack als einfachen Weg für Leute, meine Arbeit zu abonnieren, und um über deren Algorithmus etwas mehr Resonanz zu bekommen.

## GitHub Pages

Ich nutze GitHub Pages, um sicherzustellen, dass ich meine Beiträge auf einfache Weise langfristig verfügbar machen und Änderungen nachverfolgen kann. Außerdem sind die eigentlichen Beiträge einfach als Markdown-Dateien gespeichert, wenn GitHub also mit [Enshittification](https://en.wikipedia.org/wiki/Enshittification) anfängt, kann ich leicht woandershin umziehen.

### Einen GitHub-Account anlegen

Ich glaube, das muss ich nicht erklären.

### GitHub Pages mit Beautiful Jekyll einrichten

[Beautiful Jekyll](https://beautifuljekyll.com/) ist eine Vorlage für leicht anpassbare statische Webseiten. Es gibt eine gute [Anleitung](https://github.com/daattali/beautiful-jekyll#readme) für den Einstieg, aber ich gebe einen Überblick plus ein paar Extras:
* Forke das Beautiful-Jekyll-Repository und benenne es unbedingt in DEINBENUTZERNAME.github.io um. Daran erkennt GitHub, dass daraus eine GitHub Page werden soll. So entsteht eine statische Webseite unter https://DEINBENUTZERNAME.github.io
* Installiere [GitHub Desktop](https://desktop.github.com/download/) auf deinem Computer. Mit diesem Programm kannst du von dem gerade erstellten Repository herunterladen und dorthin hochladen. Klone damit dein Repository in einen lokalen Ordner deiner Wahl. Sobald du irgendetwas in diesem Ordner änderst, bemerkt GitHub Desktop das und lässt dich die Änderungen wieder in dein Online-Repository hochladen. Sobald sie hochgeladen sind, baut GitHub die Webseite mit deinen Änderungen neu.
* Im lokalen Ordner deines Repositorys solltest du eine Datei namens **_config.yml** finden. Mit dieser Datei kannst du so ziemlich alles an deiner Webseite ändern. Probier einfach herum.

Wenn dir gefällt, [wie ich alles eingerichtet habe](https://florianjehn.github.io/Societal_Collapse/), kannst du diese Schritte auch einfach machen, aber statt Beautiful Jekyll mein Repository forken.

### Beiträge veröffentlichen
Dein Repository sollte einen Ordner namens posts enthalten. In diesen Ordner kannst du Markdown-Dateien mit folgendem Namensschema legen: **JJJJ-MM-TT-name_deiner_datei.md**. Wenn du diese Datei mit GitHub Desktop in dein Repository hochlädst, erstellt GitHub an dem im Namen angegebenen Datum einen neuen Beitrag. Liegt das Datum in der Vergangenheit, wird der Beitrag sofort erstellt. Ein Beispiel, wie diese Dateien in Markdown formatiert sind, findest du [hier](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/refs/heads/main/_posts/2020-10-28-bronze_age.md).

## Substack

Einen Substack einzurichten ist ziemlich selbsterklärend, und es gibt viele Anleitungen dafür, deshalb gehe ich hier nicht ins Detail. Am hilfreichsten, um mehr Leserinnen und Leser zu bekommen, waren für mich aber Empfehlungen von anderen Substacks. Um sie zu bekommen, rede einfach mit Leuten, die über ähnliche Dinge schreiben wie du, und überzeuge sie, dass deine Arbeit auch für ihre Leserschaft relevant ist.

## Alles zitierfähig machen

Da dieser Blog im Grunde nur eine andere Form von Forschung ist, wollte ich sicherstellen, dass er über akademische Kanäle auffindbar ist und dass die Leute, die ich zitiere, mitbekommen können, was ich hier tue. Das schien ziemlich schwierig umzusetzen, bis ich auf [Rogue Scholar](https://rogue-scholar.org/) gestoßen bin, das ein Zuhause für wissenschaftliche Blogs sein will. Es ist eine Plattform, die automatisch DOIs für meine Blogbeiträge erstellt und meine Quellen herauszieht, damit andere sehen können, dass ich sie zitiert habe.

Um das auch für deinen fortlaufenden Literaturüberblick einzurichten, musst du ein paar Schritte gehen:
* Einen Account bei Rogue Scholar anlegen (optional).
* Den [Blog-Fragebogen](https://tally.so/r/nPvNK0) ausfüllen. Damit bekommt Rogue Scholar die Informationen, die es braucht, um herauszufinden, ob deine Arbeit tatsächlich ein wissenschaftlicher Blog ist.
* Einen Tag oder so warten.
* Sobald Rogue Scholar entschieden hat, dass deine Arbeit ein wissenschaftlicher Blog ist, gehen sie alle deine bisherigen Beiträge durch, um sie zu archivieren und mit DOIs zu versehen. Das Ergebnis sieht dann etwa [so](https://rogue-scholar.org/communities/existentialcrunch/records?q=&l=list&p=1&s=10&sort=newest) aus.

Jedes Mal, wenn du einen neuen Beitrag in deinem Blog veröffentlichst, wird er auch dem Archiv hinzugefügt. Die DOI leitet auf den ursprünglichen Blogbeitrag weiter, außer der ist nicht mehr verfügbar, dann greift sie auf eine archivierte Version im [Internet Archive](https://archive.org/) zurück.

Wenn ich Beiträge aktualisiert habe, muss ich Rogue Scholar manuell Bescheid geben, weil Substack diese Information nicht automatisch liefert (Wordpress zum Beispiel schon). Rogue Scholar aktualisiert dann auch die Version bei sich.

Du kannst auch zusätzliche Metadaten wie deine [ORCID](https://orcid.org/0000-0002-7296-8008) oder Informationen zur Finanzierung hinzufügen, wenn du willst.

Insgesamt eine ziemlich coole Lösung! Und jetzt hat jeder meiner Beiträge auch einen Abschnitt „Zitieren“.


# Die eigene Arbeit bekannt machen

Das ist mein unliebster Teil des ganzen Unterfangens, also mache ich das vielleicht nicht optimal. Inzwischen habe ich aber mehrere Kanäle, über die ich Leuten Bescheid gebe, wenn ich etwas Neues geschrieben habe. Ich schreibe eine kurze Zusammenfassung meines neuen Beitrags und warum er Leute interessieren könnte. Diese Zusammenfassung veröffentliche ich dann zusammen mit einem Bild aus dem Beitrag und einem Link darauf auf LinkedIn, Substack Notes und Mastodon (mit einer Brücke zu Bluesky). Außerdem schicke ich eine E-Mail an alle Abonnenten meines Newsletters. Die große Mehrheit der Leserinnen und Leser kommt über den E-Mail-Newsletter, aber über die anderen Kanäle kommen genug, damit sich die Extraarbeit dort lohnt.

# Wie fängt man seinen eigenen fortlaufenden Literaturüberblick an?

Glückwunsch, jetzt weißt du, wie man einen eigenen fortlaufenden Literaturüberblick schreibt. Wenn dich das neugierig gemacht hat, selbst einen zu schreiben, kannst du das tun. Open Phil sucht immer noch nach Leuten, die diese Art des wissenschaftlichen Schreibens ausprobieren wollen. Mehr Infos findest du [hier](https://mattsclancy.substack.com/p/time-for-more-living-literature-reviews).

# Zitieren
Bitte das englische Original zitieren:

Jehn, F. U. (2025, April 23). How to write a living literature review. Existential Crunch. [https://doi.org/10.59350/2vd97-whc20](https://doi.org/10.59350/2vd97-whc20)
