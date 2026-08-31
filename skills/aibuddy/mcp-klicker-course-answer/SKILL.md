---
name: mcp-klicker-course-answer
description: Route short factual and course-administrative questions about the OEC pilot courses to the dedicated Klicker course-answer MCP tools; do not use for teaching or participant-specific help.
---

# OEC Klicker Course Answers

Use this skill only for a simple factual or course-administrative question about one of the two
pilot courses. Keeping these answers on the dedicated course binding prevents generic retrieval
from bypassing the pilot boundary.

## Classify first

- Treat direct course facts and course administration as in scope.
- Treat conceptual teaching, explanations, worked examples, exercises, hints, solutions, diagnosis,
  grading, feedback, multi-turn learning, and participant-specific requests as out of scope. Direct
  these requests to the lecturer-governed Klicker course chatbot and do not provide substantive
  teaching in the OEC response.
- If a request mixes these categories, do not use this skill for its didactical or participant-specific
  portion.

## Call the dedicated binding

- For the OEC Finance course, call exactly `klicker_course_answer-klicker_course_finance`.
- For the OEC IUW course, call exactly `klicker_course_answer-klicker_course_iuw`.
- Call only the binding for the clearly relevant course. If the course is not clear, ask the user to
  name it; do not guess or call another tool.
- For an in-scope question, use the selected binding instead of generic doc-query, web-index,
  course-data, or general-knowledge answers.
- Pass only the course question and non-personal course information required by the binding. Keep
  student identity and participant context out of every argument, including names, IDs, enrollment,
  history, profile, role, and personalized state.

## Render the result

- Treat a successful result as presentation-ready. Render only its display-ready content; never
  expose or reconstruct chunks, excerpts, source lists, scores, filenames, retrieval locations,
  metadata, or internal IDs.
- Preserve the tool-provided Klicker reference and disclaimer verbatim exactly once, including the
  statement that the link must be provided as a reference to Klicker. Consume the tenant-provided
  reference from the result and never hardcode a real course URL.

## Fail closed

- For an error, empty result, malformed result, or unavailable binding, stop and state briefly that
  the course answer cannot be provided here.
- Never retry, broaden the question, call a companion topic tool, use generic retrieval or course
  data, consult web-index, or answer from general knowledge after such a failure. Do not reveal raw
  errors or internal data.
