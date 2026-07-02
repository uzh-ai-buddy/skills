---
name: librechat-artifacts-navigation
description: Render a navigation card artifact with building info, transit connections, departure board, and map links.
metadata:
  triggers: [navigation, directions, transit, departures, "how do I get to", Anfahrt, Wegbeschreibung]
---

# Navigation Card

## Purpose
- Render a rich navigation card showing building info, transit connections, departure board, and map links.

## When to use
- The user asks for directions to a building, transit options, or a departure board.
- The user asks "How do I get to [building]?" or similar navigation questions.
- **NOT** for simple "What's the address of X?" questions — answer those inline.

## Tool workflow
1. Call `navigate_to_building(building_code, from_location?)` to get building info, map URLs, accessibility, and transit connections.
2. Optionally call `get_departures(building_code, limit=8)` if the user wants a departure board or you think it adds value.
3. Read the template at `references/01-navigation-card.react.md`.
4. Replace the placeholder JS constants at the top with the actual tool results.
5. Emit exactly one artifact.

## Data mapping (tool results to template constants)

| Template constant | Source |
|---|---|
| `building` | `navigate_to_building` → `result.building` (`{code, name, address, campus}`) |
| `googleMapsUrl` | `navigate_to_building` → `result.google_maps_url` |
| `campusMapUrl` | `navigate_to_building` → `result.campus_map_url` |
| `accessibility` | `navigate_to_building` → `result.accessibility` (object or `null`) |
| `transitConnections` | `navigate_to_building` → `result.transit_connections` (array, may be absent → `[]`) |
| `departures` | `get_departures` → `result.departures` (array, may be absent → `[]`) |
| `stopName` | `get_departures` → `result.stop` (string, or `""` if not called) |

## Output requirements
- Follow `librechat-artifacts-core` wrapper rules.
- Use `type="application/vnd.react"`.
- Provide a 1-3 line summary before the artifact.
- Keep the component self-contained with no external assets.

## Template
- `references/01-navigation-card.react.md`
