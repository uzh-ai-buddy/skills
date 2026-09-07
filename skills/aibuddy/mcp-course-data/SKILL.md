---
name: mcp-course-data
description: Course-data MCP playbook for course search, timetables/schedules, lecturers, ECTS filters, and program/field eligibility — Vorlesungsverzeichnis, VVZ, Modul, Stundenplan. Load before the first course-data tool call.
---

# AI Buddy Course-Data Playbook

## Purpose
- Provide canonical rules for using course-data tools and presenting course results.

## When to use
- Before calling any course-data MCP tool (course search, schedules, program/field eligibility).

## Out of scope (mandatory)
- Doctoral/PhD-only course listings: politely refuse (no tool call).

## Complementary course sources

- A Klicker course binding does not replace Course Data for catalog descriptions, objectives,
  prerequisites, schedules, credits, instructors or assessment details. Use this playbook for
  those questions, including independent catalog comparisons across courses.
- For mixed requests, use the relevant Klicker binding only for supported facts from teaching
  materials, and Doc Query for regulations or policy. Keep each source's claims and citations
  distinct. A course-content failure or tutoring handoff does not block independent catalog
  questions; never use catalog retrieval to reconstruct denied teaching material.

## Tool selection (mandatory)

- **List faculties** → `get_faculties(name_query=...)`
- **Degree programs for a faculty** → `get_degree_programs_for_faculty(faculty_name=...)`
- **Majors/minors for a program** → `get_fields_for_program(program_name=...)`
- **Courses within a field** → `search_courses_by_criteria(field_name=...)`
- **Filtered course search** (day/time, lecturer, language, topic, degree program, core elective area, course code, ECTS)
  → `search_courses_by_criteria(...)`
- **Batch/exact ID lookup** → `search_courses_by_criteria(ids=[...])`
- **Filter-then-detail pattern**: when the user asks about content, assessment, or prerequisites
  that require full details across multiple filtered courses, use two calls:
  1. `search_courses_by_criteria(...)` with filters to get candidates
  2. `search_courses_by_criteria(ids=[picked IDs], include_full_details=True)` to fetch details
     for the relevant subset
- **Semantic search by topic/description** → `search_courses_by_similarity(query=...)`
- **Semantic + filters** → `search_courses_combined(...)`

## Degree program filtering (mandatory)

`degree_program` accepts only category codes: `"bachelor"` or `"master"`.
Do NOT pass full program names from `get_degree_programs()` (e.g., "Bachelor of Arts UZH in
Business and Economics (RVO22)") — these will fail.

`degree_program_field` narrows within a category: `"informatics"`, `"business and economics"`,
`"quantitative finance"`, `"veterinary"`, `"theology and religion"`.

Mapping from student context:
- `study_level: BA` / `Bachelor` → `degree_program: "bachelor"`
- `study_level: MA` / `Master` → `degree_program: "master"`

## Course search specificity (mandatory)

For a named course without an ID, start with `search_courses_by_similarity(query=...)`.
`field_name` means a study field, not a course title. Do not infer degree or field filters
from words in the title; use only filters established by the user or returned catalog data.

When searching by similarity, ensure the result is an **exact match**. If not, ask the user to
clarify the course name or provide a course code. Example: if the user asks for "Banking" and the
tool returns "Banking and Finance", do not assume the result is valid.

For each unresolved named course, allow at most one corrected search after the initial search.
If neither identifies the course, stop that lookup, state what could not be confirmed, and ask
for a course code or official VVZ link. Do not continue through faculty enumeration, repeated
filter variations, Cypher, Doc Query or web searches to resolve the same missing course.
This limit does not block detail lookup for an identified course, requested listing pagination,
or independent policy and teaching-material questions. Never imply a missing result proves
the course does not exist or use another semester as confirmation of the requested semester.

## Full details usage (mandatory)

Basic listings always include assessment info (`tests_description`), course `category`
(e.g. "Lecture with Practical Exercises"), `offer_pattern`, and `repeat_type`.
Use `include_full_details=True` when students ask about:

- Course content ("What does this course cover?")
- Prerequisites ("What do I need before taking X?")
- Specific course codes mentioned ("Tell me about AOEC10")

`include_full_details` adds objectives, prerequisites, and further info descriptions.

Notes:
- `search_courses_by_similarity(..., include_full_details=True)` returns at most 3 results.
- `search_courses_by_criteria(..., include_full_details=True)` adds description fields; it also
  returns `full_schedule` and lecturers.

## Schedule & time queries (mandatory)

- **When/where a specific course meets** → `search_courses_by_criteria(course_id=...)` and read
  `full_schedule`.
- **Day/time filtering** (e.g., Friday courses, morning slots) →
  `search_courses_by_criteria(day_of_week=..., start_time=..., end_time=...)`.
- If the user only gives a **course name**, first resolve it with
  `search_courses_by_similarity`, then ask for the course code if you need an exact schedule.

Conventions:
- Day abbreviations: Mon/Tue/Wed/Thu/Fri/Sat/Sun (full names also accepted).
- Time format: HH:MM.

For multiple specific courses, make separate calls per course code.

## Lecturer queries (mandatory)

- **Courses taught by a lecturer** → `search_courses_by_criteria(lecturer_name=...)`.
- **Who teaches a specific course** → if course code is known, call
  `search_courses_by_criteria(course_id=...)` and read `lecturers` from the results.

## Eligibility and requirements

For questions regarding eligibility of courses for specific study programs/majors/minors and/or
areas (compulsory or elective), always use the course-data MCP to double-check.
- **Courses counting toward a core elective area** → `search_courses_by_criteria(areas=...)`
- areas can be BF1 to BF5, BWL1 to BWL6, ECON1 to ECON3.
- If we want the course to count for any area from a given list, pass a list (e.g ["BF1","BWL3","BWL4"]).

## Course listing neutrality

When presenting lists of courses, do not weight, rank, curate, or pick examples from a larger set
unless specifically for the purpose of accounting for stated user preferences. Present all results
returned by the tool without cherry-picking. **Never claim these are "all" matching courses** —
tools return a limited sample (default 10-20, or 3 with `include_full_details`). Instead, state
how many results were found and suggest the user refine criteria or ask for more if needed. If
results seem truncated, increase `limit` or ask the user to narrow criteria rather than picking
examples. Use `offset` for pagination through large result sets (e.g., `offset=10, limit=10` for
the second page).

## Ad-hoc Cypher queries

- **When structured tools can't answer** (aggregations, graph traversals, complex joins) →
  `run_cypher_query(query=..., parameters={...}, limit=50)`
- **Before writing any Cypher**, read `references/cypher-guide.md`. It contains the correct
  graph model, node properties, and 10 working example queries.
- Read-only only; write keywords are rejected.
- Use `$param` bindings for values instead of string interpolation.
- Max 200 results; queries time out after 10s.
- Embedding vectors are automatically stripped from results.
- Prefer structured tools first; use `run_cypher_query` only as a fallback.
- **Common mistake**: There is no direct StudyModule→Person link. Lecturers connect via Event:
  `(:StudyModule)-[:HAS_EVENT]->(:Event)-[:TAUGHT_BY]->(:Person)`

## Language and topic filters

- `language` prefers: "English", "German", "French", "Italian".
- For bilingual requests, pass a list (e.g., `["English", "German"]`).
- **Topic filters**: before passing `topic_names`, read `references/topic-vocabulary.md` for the
  exact valid names for the tool you are calling — the tool schemas no longer list them, and
  `search_courses_by_criteria` and `search_courses_combined` use different, non-interchangeable
  topic vocabularies (both support a few common abbreviations, e.g. AI/ML/HCI).
