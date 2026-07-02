---
name: librechat-artifacts-study-planner
description: Create semester-by-semester study plan artifacts with ECTS tracking and milestones.
metadata:
  triggers: [Studienplan, Semester-Plan, ECTS, Meilensteine, study plan, scenario]
---

# Study Planner Artifacts

## Purpose
- Deliver comprehensive study plans with semester tables, ECTS summaries, and milestones.

## When to use
- The user requests a full study plan or semester-by-semester plan.
- The user asks for multiple scenarios (exchange vs internship) that benefit from side-by-side
  comparisons or a dedicated “What-if adjustments” section.

## Output requirements
- Follow `librechat-artifacts-core` wrapper rules.
- Provide 2–5 line summary in chat and exactly one artifact.
- Include a semester-by-semester table with columns: Semester, Module/Track, ECTS,
  Prerequisites/Status, Risk/Notes.
- After the table, provide aggregated ECTS by phase + total.
- Include a milestone checklist and a short “What-if adjustments” section.

## Templates

- Full 6-semester study plan template:
  `references/01-study-plan-6-semesters.md`
- Scenario comparison template (exchange vs internship):
  `references/02-study-plan-scenario-compare.md`
