---
name: mcp-klicker-course-answer
description: Route short factual and course-administrative questions to the configured Klicker course-answer MCP tool for the relevant course; do not use for teaching or participant-specific help.
---

# Klicker Course Answers

Use this skill only for a simple factual or course-administrative question about a course that has
a configured Klicker course-answer binding. Keeping these answers on the dedicated course binding
prevents generic retrieval from bypassing the course boundary.

Use this skill in Answer mode only. Never use it to populate Documents mode or expose course
material as document chunks.

## Classify first

- Treat direct course facts and course administration as in scope.
- Treat conceptual teaching, explanations, worked examples, exercises, hints, solutions, diagnosis,
  grading, feedback, multi-turn learning, and participant-specific requests as out of scope. Direct
  these requests to the lecturer-governed Klicker course chatbot and do not provide substantive
  teaching in the AI Buddy response.
- If a request mixes in-scope and prohibited content, prohibited content wins: do not call a
  course-answer tool and hand off the entire request to the relevant lecturer-governed Klicker
  course chatbot.

## Call the configured binding

- Course-answer bindings appear as `klicker_course_answer_mcp_klicker_course_<course>` in the
  tool list; each configured course exposes exactly one binding. Choose among the bindings
  actually offered in the current tool list; never invent or construct a binding name.
- Call only the binding for the clearly relevant course. If the course is not clear, ask the user to
  name it; do not guess or call another tool.
- Never combine bindings or use one binding to answer about another course. If a request spans
  multiple courses or asks for a comparison across them, do not call any binding; hand off the
  complete request to the lecturer-governed Klicker course chatbots.
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
