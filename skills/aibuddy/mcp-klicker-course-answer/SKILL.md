---
name: mcp-klicker-course-answer
description: Route short factual and course-administrative questions about the OEC pilot courses to the dedicated Klicker course-answer MCP tools; do not use for teaching or participant-specific help.
---

# OEC Klicker Course Answers

Use this skill only for a simple factual or course-administrative question about one of the two
pilot courses. Keeping these answers on the dedicated course binding prevents generic retrieval
from bypassing the pilot boundary.

Use this skill in Answer mode only. Never use it to populate Documents mode or expose course
material as document chunks.

## Classify first

- Treat direct course facts and course administration as in scope.
- Treat conceptual teaching, explanations, worked examples, exercises, hints, solutions, diagnosis,
  grading, feedback, multi-turn learning, and participant-specific requests as out of scope. Direct
  these requests to the lecturer-governed Klicker course chatbot and do not provide substantive
  teaching in the OEC response.
- If a request mixes in-scope and prohibited content, prohibited content wins: do not call a pilot
  tool and hand off the entire request to the relevant lecturer-governed Klicker course chatbot.

## Call the dedicated binding

- For the OEC Finance course, call exactly `klicker_course_answer-klicker_course_finance`.
- For the OEC IuW course, call exactly `klicker_course_answer-klicker_course_iuw`.
- Call only the binding for the clearly relevant course. If the course is not clear, ask the user to
  name it; do not guess or call another tool.
- Never combine the Finance and IuW bindings or use one to answer about the other. If a request
  spans both courses or asks for a comparison across them, do not call either pilot tool; hand off
  the complete request to the lecturer-governed Klicker course chatbots.
- For an in-scope question, use the selected binding instead of generic doc-query, web-index,
  course-data, or general-knowledge answers.
- Pass only `question` and optional `locale` (`de` or `en`) to the selected binding. Omit `locale`
  when it is unresolved so the binding applies its default. Pass no other argument. Keep student
  identity and participant context out of every argument, including names, IDs, enrollment,
  history, profile, role, and personalized state.

## Render the result

- Accept only the three Doc Query outcomes `grounded_success`, `didactic_handoff`, and `no_grounding`.
  For any accepted outcome, render only `display_ready_content`; never render `answer`, the raw
  envelope, or reconstruct content from it.
- Never expose or reconstruct chunks, excerpts, source lists, scores, filenames, retrieval locations,
  metadata, or internal IDs.
- Use the approved tenant/agent configuration as the only source for the handoff reference and
  disclaimer. Do not invent, substitute, infer, or hardcode a URL from a prompt, tool name, course
  name, or prior turn.
- Require the tool-provided disclaimer and Klicker reference, including the statement that the link
  must be provided as a reference to Klicker, verbatim exactly once. If either value is missing,
  invalid, or duplicated, fail closed; never repair it.

## Fail closed

- For an error, empty result, malformed result, or unavailable binding, stop and state briefly that
  the course answer cannot be provided here.
- Never retry, broaden the question, call a companion topic tool or any alternate tool, use generic
  retrieval or course data, use web search or browsing, consult web-index, or answer from general
  knowledge after such a failure. Do not reveal raw errors or internal data.
