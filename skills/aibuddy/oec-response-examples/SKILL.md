---
name: oec-response-examples
description: Canonical worked response examples and style templates per query type for AI Buddy — load when drafting a response that is template-adjacent, procedural, or a novel query type, to match structure, tone, and phrasing.
---

# AI Buddy Response Examples

## Purpose

- Provide canonical response examples as structure and phrasing templates.
- Ensure consistent formatting, tone, and flow across common query types.

## When to use

- Before drafting a response that is similar in type or style to the listed examples.

## How to use (mandatory)

- For a Klicker Course Answer portion, its dedicated playbook owns formatting, source fidelity,
  the first-course disclaimer and the final chatbot container. Do not load these examples solely
  for that portion or replace its presentation with an example. For independent administrative
  or policy portions, apply the relevant examples while keeping all content and notices before
  the trusted final chatbot container.
- Determine the **primary response type** that best matches the user's query.
- Identify **secondary style needs** (e.g., procedural steps + regulation disclaimer, exploratory
  prose + follow-up question, schedule + currency notice).
- **Read all relevant examples** from `references/` before drafting the final response:
  - Always read the **primary** example.
  - Also read any **secondary** examples that match query parts or required style.
  - Typical: **1–3 examples**; read more only if the user question is clearly multi-part.
- Use examples strictly as **structure and phrasing templates**. All factual content must still
  come from tool outputs.

## Example index

<!-- BEGIN:AUTO-GENERATED -->
| Example | When to use | Lang | Summary | URI |
| --- | --- | --- | --- | --- |
| 01 (uzh) | Association information | en | Use when the user asks about a student association or club. Structure: brief lead-in, short overview of purpose + activities + governance, then link and friendly close; finish with Sources. | `references/01-uzh-association-information.md` |
| 02 (wwf) | Procedure information | de | Use for administrative procedures like illness on exam day. Structure: lead-in plus numbered steps, highlight key constraints, add required disclaimer, then Quellen. | `references/02-wwf-procedure-information.md` |
| 03 (wwf) | Course information | de | Use for course assessment/requirements. Structure: lead-in, explain assessment components, add official links, include extra hints + disclaimer + Aktualität note, then Quellen. | `references/03-wwf-course-information.md` |
| 04 (wwf) | Schedule information | de | Use for time/place of a course. Structure: lead-in, bullet list with semester/time/rooms/exam note, add currency reminder, then Quellen. | `references/04-wwf-schedule-information.md` |
| 05 (wwf) | Exam overview | de | Use for exam schedules across modules. Structure: lead-in, list exam dates by course, add official schedule link and Aktualität reminder, then Quellen. | `references/05-wwf-exam-overview.md` |
| 06 (wwf) | Grade issues | de | Use when a user disputes a grade. Structure: lead-in, explain inspection first, then numbered appeal/recourse steps with deadlines, add tip + disclaimer, then Quellen. | `references/06-wwf-grade-issues.md` |
| 07 (wwf) | Failed twice switch major | de | Use when a student failed a module twice and asks about switching. Structure: lead-in, consequences (exclusion/sperre), options by faculty, minor special case, advisory contact + disclaimer, then Quellen. | `references/07-wwf-failed-twice-switch-major.md` |
| 08 (wwf) | Credit transfer vocational | de | Use for credit transfer of vocational training. Structure: lead-in, state vocational training not creditable, list conditions and steps, add disclaimer, then Quellen. | `references/08-wwf-credit-transfer-vocational.md` |
| 09 (policy) | Content definition refusal | en | Use for content-definition questions without tool context. Structure: short refusal stating scope, mention only official sources, direct to lecturers; no extra info. | `references/09-policy-content-definition-refusal.md` |
| 10a (uzh) | Exploratory summary | en | Use for vague exploratory student-life queries. Structure: brief summary of tool findings, ask a clarifying question, then Sources. | `references/10a-uzh-exploratory-summary.md` |
| 10b (uzh) | Exploratory after clarification | en | Use after clarification; present only the relevant subset from prior retrieval. Structure: concise recommendations + follow-up question, then Sources. | `references/10b-uzh-exploratory-after-clarification.md` |
| 11 (wwf) | Minor to major change | de | Use when a student in a minor program wants to switch to a major after receiving a Fachsperre. Structure: lead-in, answer key questions about assessment requirements and implications for course booking, add advisory note about individual case review, then Quellen. | `references/11-wwf-minor-to-major-change.md` |
| 12 (wwf) | Module booking deadline | de | Use when a student asks about the deadline for module booking or cancellation. Structure: lead-in, explain the official deadlines and consequences of missing them, add links to official sources and a disclaimer, then Quellen. | `references/12-wwf-module-booking-deadline.md` |
| 13 (uzh) | Money problems | de | Use when a student expresses financial difficulties related to tuition fees. Structure: lead-in, explain the option of applying for a hardship loan, provide links to the financial aid office and resources, offer to help draft an email, then Quellen. | `references/13-uzh-money-problems.md` |
| 14 (wwf) | Tutorat | de | Use when a student asks about tutoring as part of their studies. Structure: lead-in, explain what a tutorat is and how it works, offer to help with the application process, then Quellen. | `references/14-wwf-tutorat.md` |
| 15 (wwf) | Eth module recognition | de | Use when a student asks about recognizing ETH modules for their OEC program. Structure: lead-in, explain the general process and criteria for recognition, provide links to the official guidelines and contact information for the recognition office, then Quellen. | `references/15-wwf-eth-module-recognition.md` |
| 16 (uzh) | Live current content | de | Use when the answer depends on current content AND the live fetch succeeded. Structure: lead-in, the current facts, source labels marking the live fetch and its timestamp, then Quellen closed by the live-content disclaimer. If the fetch did not succeed, this shape does not apply -- follow 17 instead. | `references/16-uzh-live-current-content.md` |
| 17 (uzh) | Unverified current content | en | Use when the user asks what is currently true about a page or offering -- who it is for now, what applies this semester, what the current rules are -- and the answer rests on content that was not verified live. Structure: state up front that the information could not be verified live, give the indexed facts qualified as such, point to the official page, then Sources labelled indexed. | `references/17-uzh-unverified-current-content.md` |
<!-- END:AUTO-GENERATED -->
