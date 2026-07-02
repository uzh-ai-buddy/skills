---
name: mcp-rooms
description: Rooms MCP playbook for room lookup, building info, campus navigation, and accessibility.
---

# AI Buddy Rooms Playbook

## Purpose
- Bridge between `course_data` room codes and physical locations (address, accessibility, transit).
- Provide campus navigation, building info, and room search capabilities.

## When to use
- Before calling any rooms MCP tool.
- When the user asks about room locations, building directions, accessibility, campus navigation,
  or study spaces.

## Tool selection (mandatory)

| Use case | Tool |
|----------|------|
| Room code from schedule (e.g. KOL-F-101) | `get_room_details(room_code=...)` |
| Find rooms by criteria (capacity, type) | `search_rooms(campus?, usage_type?, min_seats?, max_seats?, building_code?, limit=20)` |
| Building address, accessibility, room list | `get_building_info(building_code=...)` |
| List all buildings (optionally by campus) | `list_buildings(campus?)` |
| Directions, transit, entrance info | `navigate_to_building(building_code=..., from_location?)` |
| Upcoming trams/buses at a building | `get_departures(building_code=..., limit=8)` |
| Campus-level stats and overview | `get_campus_overview(campus=...)` |

## Room code format (mandatory)

Room codes follow the pattern `BUILDING-FLOOR-NUMBER` (e.g. `KOL-F-101`, `Y25-H-30`).
These appear in `course_data` schedule results. Use `get_room_details` to resolve them to
physical locations.

## Campus values (mandatory)

Pass `"Zentrum"` or `"Irchel"` for campus parameters. The server handles case-insensitively.

## Relationship to doc-query

- Catalog doc-query tools such as `uzh_campus_digital_services_expert` handle policy questions,
  study space availability, and general campus facility information.
- Rooms MCP provides structured live data: exact addresses, accessibility details, transit stops,
  and navigation URLs.
- Use both when a question spans policy and location (e.g. "Where can I study and how do I get
  there?").

## Tool chaining pattern

Course schedule query (`search_courses_by_criteria`) -> extract room code from results ->
`get_room_details(room_code=...)` -> optionally `navigate_to_building(building_code=...)` if the
user needs directions.

## Navigation artifact

When the user asks for **directions**, **transit connections**, or **how to get to** a building,
emit a navigation card artifact instead of plain text.

**When to emit**: directions, transit, departure board requests.
**When NOT to emit**: simple "what's the address of X?" questions — answer those inline.

### Data mapping
1. Call `navigate_to_building(building_code, from_location?)` → provides `building`, `google_maps_url`, `campus_map_url`, `accessibility`, `transit_connections`.
2. Optionally call `get_departures(building_code, limit=8)` → provides `departures`, `stop`.
3. Map tool results to template constants and emit the artifact.

See the `librechat-artifacts-navigation` skill for full template instructions.
