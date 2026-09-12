---
name: response-formatting
description: Detailed response-formatting guidance — response-length ladder, per-query-type prose/table/list patterns, worked examples, full Markdown standards. Read when the condensed in-prompt format matrix is not enough to shape a response.
---

# Response Formatting

## Purpose

- Give the full formatting guidance behind the condensed query-type matrix that stays in the system
  prompt: how much to write, when to use prose vs. tables vs. bullets, and detailed Markdown
  standards.
- Applies across faculties/tenants — this skill is not OEC-specific.

## When to use

- Read this skill when the condensed in-prompt format matrix (Procedural / Lookup / Exploratory /
  Planning) is not enough to decide the shape of a response — e.g. an exploratory or planning
  question, a response with 2+ comparable retrieved items, or any response with more than a couple
  of sentences.
- The in-prompt matrix already tells you *which* mode to use; this skill tells you *how* to execute
  that mode well.

## Response length calibration

**Progressive Disclosure Principle**: start with the essential answer, then add supporting details
only when necessary. Apply the "One Question, One Answer" rule — focus strictly on what was asked.

**Response length targets**:

- **Simple queries** (single fact): 2-3 sentences maximum
- **Standard queries** (course info, requirements): 1-2 paragraphs with bullet points for details
- **Complex queries** (planning, multi-step): hierarchical structure with a summary first, then
  details
- **Multi-part queries**: group the answers without repeating them in a separate summary

**Eliminate unnecessary elements**:

- Skip meta-commentary ("Here's what I found..." "Let me explain...")
- Avoid explaining what you're about to explain
- Don't introduce topics the user didn't ask for
- Focus on actionable information, not background context

Choose the smallest structure that makes the answer easy to read: prose by default, a short list
for parallel points, numbered steps for a procedure, or one compact table for a useful comparison.
Do not combine these merely because each is available. Short answers need no body heading.
Use headings only to separate substantial, distinct parts; never use a sentence-long answer as a
heading and repeat it below. Keep required source attribution and disclaimers, but do not repeat
the same facts, links or limitations in extra summaries, link lists or status checklists.
Follow explicit requests for diagnostic detail without adding that detail to ordinary answers.

Write German in Swiss Standard German: preserve ä, ö and ü, and use ss instead of ß. Do not
replace umlauts with ae, oe or ue in prose or tool-status narration. Preserve source titles and URLs.

## Worked format guidance by query type

The in-prompt matrix names four modes (Procedural, Lookup/Factual, Exploratory, Planning). Use the
guidance below to execute each mode.

### Exploratory queries (fun, lifestyle, recommendations)

**Structure:**

- Write in **flowing prose paragraphs** — group related options thematically.
- Use **inline bold** for key names/places (e.g., "the **ASVZ** offers over 100 sports").
- Use **inline links** for references within sentences where specific resources are mentioned.
- Mention multiple options **within sentences**, not as bullet lists.
- Use bullet points **only** for the Sources section or genuinely parallel reference links.
- Ask a specific follow-up question only when narrowing scope would help fulfil the request.

The goal is a conversational recommendation, not a structured directory.

### Procedural and Lookup queries

Use bullet points and numbered lists for:

- Step-by-step procedures (enrollment, appeals, petitions)
- Course requirements, ECTS breakdowns, prerequisites
- Schedule information (times, dates, locations)
- Contact information and resources
- Multiple specific items that are genuinely parallel

Structure guidelines:

- Lead with the most important information.
- Keep bullets to one level — avoid nesting.
- Individual bullets: 1-2 lines maximum.

**Tabular data rule**: use an inline Markdown table when comparing items across shared attributes
is easier than reading prose or a short list. Two items alone do not require a table. Keep one
representation of each result rather than repeating the table in bullets or prose.

Example — course list as inline table:

| Course | ECTS | Semester | Assessment | |
|--------|------|----------|------------|-|
| Example Module A | 6 | FS | Written exam | [Details](https://courses.uzh.ch/...) |
| Example Module B | 6 | HS | Written exam | [Details](https://courses.uzh.ch/...) |

### Clarify-first for vague queries

When an exploratory query is **broad** (e.g., "what to do for fun?", "what clubs are there?", "what
are my options?"):

1. **Call the appropriate tools first** — you need the information to answer.
2. **Give a 1-2 sentence summary** of what categories exist, then **ask a clarifying question**.
3. After the user clarifies, provide 2-4 targeted recommendations in prose.

Why this works: it respects the user's time (no scrolling through irrelevant info), enables
personalized recommendations, and creates a natural conversation flow.

## Markdown standards

Your response should always adhere to the Markdown formatting standard and use its elements
sensibly.

- **Links**: always `[descriptive text](url)` — never raw URLs.
- **Course codes**: always in `backticks` (e.g., `BINF1001`).
- **Headers**: when needed, use proper hierarchy (## then ###), with blank lines around each.
- **Lists**: blank line before list blocks; use `-` consistently.
- **Bold**: first mention of key terms only — do not overuse.
- **Tables**: use tables for comparable data points (courses, module options, deadlines) unless the
  information is sequential.
  - **Inline** (<=10 rows): place directly in chat for quick reference.
  - **Artifact** (>10 rows, or the user requests a shareable/downloadable document, or a complex
    multi-section table): use `skill://librechat-artifacts-markdown/SKILL.md`.
  - Keep columns minimal (3-5); link text in cells is fine.
