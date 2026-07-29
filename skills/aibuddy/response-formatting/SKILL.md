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
- **Multi-part queries**: lead with a bullet-point summary, expand only essential points

**Eliminate unnecessary elements**:

- Skip meta-commentary ("Here's what I found..." "Let me explain...")
- Avoid explaining what you're about to explain
- Don't introduce topics the user didn't ask for
- Focus on actionable information, not background context

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
- End with a **specific follow-up question** to narrow scope.

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

**Tabular data rule**: when results contain **2+ comparable items** with shared attributes (e.g.,
name, ECTS, level, semester, lecturer), present them as an **inline Markdown table** instead of
bullet points. Use bullets only for sequential steps, single-attribute lists, or items with no
shared structure.

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
- **Headers**: use proper hierarchy (## then ###), blank line before each.
- **Lists**: blank line before list blocks; use `-` consistently.
- **Bold**: first mention of key terms only — do not overuse.
- **Tables**: use tables for comparable data points (courses, module options, deadlines) unless the
  information is sequential.
  - **Inline** (<=10 rows): place directly in chat for quick reference.
  - **Artifact** (>10 rows, or the user requests a shareable/downloadable document, or a complex
    multi-section table): use `skill://librechat-artifacts-markdown/SKILL.md`.
  - Keep columns minimal (3-5); link text in cells is fine.
