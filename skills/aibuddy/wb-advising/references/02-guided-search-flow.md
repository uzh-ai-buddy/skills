# Fall 2 — Chatbot-Guided Search

Use when the user's target is not yet clear. Ask the questions below ONE AT A TIME, in order, and
SKIP any question already answered or held in memory. Keep it conversational, not an interrogation.

1. Field / topic — "In welchem Bereich oder zu welchem Thema möchtest du dich weiterbilden?"
2. Prior education — "Was ist dein höchster Abschluss (und in welchem Bereich)?"
   (admission to many programs depends on this)
3. Timing & format — "Wann möchtest du ungefähr starten, und welche Dauer bzw. welches Pensum
   stellst du dir vor (z. B. berufsbegleitend)?"
4. Professional purpose / certificate — "Geht es um berufliche Ziele — brauchst du einen formellen
   Abschluss bzw. ein Zertifikat?"
5. Budget — "Spielen die Kosten eine Rolle für dich (Budget)?"

Then:

- Use the collected criteria to query `uzh_wb_program_finder_expert` (add `continuing_education_type`
  and `topic_filters` when known).
- Present 2–4 matching options with type (CAS/DAS/MAS), duration, indicative cost, and an admission
  note — all from tool output.
- If results are weak, broaden the wording or fall back to `web_index_pages`.
- Based on the answers, branch to alternatives where appropriate (see
  `references/03-alternative-routing.md`):
  - Too expensive → Studienberatung / grundständiges-Studium hint / MOOCs.
  - No certificate / purely private interest → UZH Agenda (public events) / Auditor:innen
    (Vorlesungsverzeichnis).
  - Topic fits children or seniors → Kinder-Universität / Senior:innen-Universität (state the age
    group).
- Remember every answer to memory; never re-ask.

Always close with Quellen and keep the tone friendly and Swiss-German-aware.
