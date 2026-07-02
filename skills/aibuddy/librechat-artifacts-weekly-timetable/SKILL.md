---
name: librechat-artifacts-weekly-timetable
description: Create a color-coded weekly timetable with conflict detection.
metadata:
  triggers: [Wochenplan, Stundenplan, visuell, Konflikte, timetable, schedule grid]
---

# Weekly Timetable

## Purpose
- Provide a structured weekly schedule with color-coded blocks and clear conflict warnings.

## When to use
- The user asks for a weekly timetable, schedule overview, or time grid.
- The user wants conflict detection between overlapping events.

## Inputs to collect
- **Course events**: Use `search_courses_by_similarity` with `include_full_details=True` to fetch times, rooms, and types for all mentioned courses. Extract Events data from the tool response.
- **Personal commitments** (work, etc.): Parse day and time ranges from the user's message (e.g., "Di/Do Nachmittag" → Tuesday/Thursday 13:00–18:00).
- Highlighted commitments (work, mandatory courses) to style differently if needed.

## Tool workflow
1. Identify mentioned courses in the user's request.
2. Call `search_courses_by_similarity` for each course with `include_full_details=True` to get schedule/Events data.
3. Parse personal work/timing constraints from user message.
4. Merge all events into the `events` array for the React artifact.
5. Generate the artifact with merged data.

## Output requirements
- Follow `librechat-artifacts-core` wrapper rules.
- Provide a brief 2–5 line summary in chat and exactly one artifact.
- Use `type="application/vnd.react"`.
- Include a conflict list and a legend for color meanings.
- Keep the component self-contained with no external assets.

## Templates

- Calendar grid (time-axis, visual blocks):
  `references/01-weekly-timetable-calendar-grid.react.md`
- Compact columns (stacked blocks, quick overview):
  `references/02-weekly-timetable-compact-columns.react.md`
