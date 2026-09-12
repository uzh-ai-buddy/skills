---
lang: de
summary: "Use when the answer depends on current content AND the live fetch succeeded. Structure: lead-in, the current facts, source labels marking the live fetch and its timestamp, then Quellen closed by the live-content disclaimer. If the fetch did not succeed, this shape does not apply -- follow 17 instead."
---

**User:**
Wie lange hat die Hauptbibliothek heute geöffnet?

**Assistant:**

Lass mich die aktuellen Öffnungszeiten nachschauen.

Die **Hauptbibliothek Universität Zürich – Zentrum** ist heute bis **22:00 Uhr** geöffnet. Die
Ausleihe schliesst bereits um **21:45 Uhr**, plane den Bezug von Büchern also etwas früher ein.

An Sonn- und Feiertagen gelten abweichende Zeiten.

---

## Quellen

- [Hauptbibliothek UZH – Öffnungszeiten](https://www.hbz.uzh.ch/de/oeffnungszeiten.html) — live abgerufen, 31. Juli 2026 09:15 UTC

_Live abgerufene Inhalte entsprechen dem Stand zum angegebenen Zeitpunkt und können sich seither
geändert haben._

---

This shape holds only when the live fetch succeeded. When it returned `not_live_fetchable`, an error,
or nothing usable, do not put the facts first and append a note about verification -- follow
`17-uzh-unverified-current-content.md`, which leads with the limitation, presents no fact as current,
and cites the resource that was actually selected rather than a broader page of the same site.
