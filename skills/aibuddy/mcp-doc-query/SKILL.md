---
name: mcp-doc-query
description: Doc-query MCP playbook for generated catalog expert routing, filters, and citation handling.
---

# AI Buddy Catalog Doc-Query Playbook

## Purpose

- Route UZH policy, study, service, and catalog questions to generated catalog expert tools.
- Apply only narrowing filters that match the question and known student context.
- Preserve retrieved source citations, page labels, and disclaimers accurately.

## When to use

Read this skill before calling any catalog doc-query tool.

Use catalog doc-query for questions about:

- admissions, enrollment, module booking, exams, theses, study regulations, and study programs
- central student services, counseling, mobility, funding, disability support, and UZH policies
- continuing education programs, registration, costs, degrees, and public learning events
- ZI/IT services, accounts, VPN/network, software, learning platforms, and digital services
- faculty-specific catalog information for OEC, TRF, and VET

## Tool naming

Catalog tools are generated from the catalog taxonomy. Select the most specific available tool by
combining a scope prefix with a domain suffix.

### Scope prefixes

| Prefix | Scope |
| --- | --- |
| `uzh_` | UZH-wide study and central student information |
| `uzh_wb_` | UZH continuing education |
| `zi_` | Central IT / ZI services |
| `oec_` | Faculty of Business, Economics, and Informatics |
| `trf_` | Theological and Study of Religions Faculty |
| `vet_` | Vetsuisse / Veterinary Medicine |

### Common domain suffixes

These suffixes exist for `uzh_`, `oec_`, `trf_`, and `vet_` scopes:

| Suffix | Use for |
| --- | --- |
| `admissions_regulations_expert` | admissions, enrollment, module booking, policies, regulations |
| `courses_exams_expert` | courses, exams, assessment, grading, module information |
| `study_programs_degrees_expert` | bachelor/master programs, majors/minors, degrees, theses |
| `student_services_expert` | counseling, funding, disability support, career, fees, family, student life |
| `mobility_exchange_expert` | exchange, mobility, international study, partner programs |
| `research_doctoral_studies_expert` | PhD, research groups, research projects, seminars |
| `campus_digital_services_expert` | facilities, library, accounts, VPN, learning platforms, infrastructure |
| `general_info_expert` | catch-all for scope-specific information not covered above |

Examples:

- `uzh_admissions_regulations_expert`
- `oec_courses_exams_expert`
- `trf_study_programs_degrees_expert`
- `vet_student_services_expert`
- `zi_campus_digital_services_expert`

### Continuing education tools

Use `uzh_wb_*` tools for continuing education. Important tools include:

- `uzh_wb_program_finder_expert`
- `uzh_wb_courses_expert`
- `uzh_wb_admission_registration_expert`
- `uzh_wb_costs_funding_expert`
- `uzh_wb_degrees_credentials_expert`
- `uzh_wb_legal_quality_expert`
- `uzh_wb_services_contact_expert`

## Routing rules

1. Choose the narrowest scope that matches the user question.
   - askUZH-wide questions: use `uzh_*`, `uzh_wb_*`, or `zi_*`.
   - OEC questions: always start with the matching `oec_*` expert. Add a `uzh_*` expert only for genuinely central UZH rules or services — do not substitute `uzh_general_info_expert` or a `uzh_*` scope expert for an OEC-specific question that an `oec_*` expert covers.
   - TRF questions: prefer `trf_*`; call `uzh_*` too only for central UZH rules or services.
   - VET questions: prefer `vet_*`; call `uzh_*` too only for central UZH rules or services.
2. Choose the domain suffix from the user's intent, not from keywords alone.
   - Exam rules and module booking: `*_admissions_regulations_expert` or `*_courses_exams_expert`.
   - Program structure, majors/minors, theses, degree requirements:
     `*_study_programs_degrees_expert`.
   - Specific course offerings, schedules, instructors, ECTS, or assessments: use course-data first;
     use catalog doc-query for rules and policy context.
3. If the first result is empty or too broad, call the adjacent domain tool before refusing.
   - Example: exam booking may require both `*_admissions_regulations_expert` and
     `*_courses_exams_expert`.
4. For ambiguous catalog subtopics, do NOT guess `topic_filters`: run the expert tool without
   topic filters first, then narrow with `topic_filters` only when the returned chunks make the
   exact topic value certain.

## Filter rules

- The selected tool already enforces its catalog expert scope. Do not pass `expert_filters`.
- Use runtime filters only to narrow retrieval when the value is known:
  - `language`
  - `topic_filters`
  - `parser_used`
  - `source_type`
  - `continuing_education_type`
- Use student context filters when known and relevant:
  - `study_level`
  - `department`
  - `faculty`
- Do not guess missing filter values. Ask a short clarification only when the answer depends on the
  missing value.
- Keep the free-text `question` in the user's conversation language.

## Response handling

- Answer only from retrieved catalog content.
- Include source links and page information when returned by the tool.
- If a retrieved source includes a disclaimer, warning, legal notice, or validity condition,
  preserve its meaning and include it in the user's language.
- If the retrieved context is insufficient after retrying adjacent tools or broader wording, use the
  no-matching-context refusal from the main prompt.

## Tool chaining patterns

- Course details: course-data first, then the relevant catalog expert for policy or regulation.
- Exam or assessment policy: `*_courses_exams_expert` plus `*_admissions_regulations_expert` when
  registration, deadlines, or legal rules are involved.
- Study planning or degree requirements: `*_study_programs_degrees_expert` plus course-data for
  concrete module choices.
- Continuing education: start with `uzh_wb_program_finder_expert`; add
  `uzh_wb_admission_registration_expert`, `uzh_wb_costs_funding_expert`, or
  `uzh_wb_degrees_credentials_expert` as needed.
- IT support: use `zi_campus_digital_services_expert`; use `zi_general_info_expert` for broad ZI
  overview questions.
