---
layout: page
title: Quellen
permalink: /de/references/
---

Diese Seite enthält alle Quellen, die für diesen lebendigen Literaturüberblick verwendet wurden. Die Liste wird direkt von der englischen Seite übernommen, die Einträge selbst bleiben im Original.

{% assign en_refs = site.pages | where: "url", "/references/" | first %}
{% assign en_intro = "This page contains all references used in the creation of this living literature review:" %}
{{ en_refs.content | remove_first: en_intro | markdownify }}
