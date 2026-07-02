---
name: wb-advising
description: Advising workflow for UZH continuing-education inquiries. Handles a known-program lookup only when the user names an exact program, otherwise defaults to a chatbot-guided search with intake questions and routing to alternatives. Remembers what the user shares and asks before assuming. Apply for any Weiterbildung / MAS / DAS / CAS question.
metadata:
  triggers: [Weiterbildung, weiterbilden, Weiterbildungsprogramm, continuing education, further education, further education program, executive education, program recommendation, looking for a program, MAS, DAS, CAS, Zertifikatskurs, Zertifikatslehrgang, berufsbegleitend]
---

# UZH Continuing Education — Advising Workflow

## Purpose

- Drive continuing-education advising conversations consistently.
- Decide between a direct program lookup and a guided search, collect the needed context, and route
  to the right UZH offering.

## When to use

- Any question about continuing education / MAS / DAS / CAS / certificate programs at UZH.
- Pair with the `wb-domain-knowledge` skill (program types + alternatives) and the `mcp-doc-query`
  skill (the `uzh_wb_*` tools).

## Decision: known program vs guided search

First decide whether the user's target is already clear:

- **Named program** — the user names an exact UZH program or asks about one exact program title
  (e.g. "MAS in Banking and Finance", "the CAS Hochschuldidaktik")
  → Fall 1, direct lookup. See `references/01-known-program-lookup.md`.
- **Looking for a program** — the user wants help finding, choosing, comparing, or recommending a
  continuing-education program, but has not named one exact program
  → Fall 2, the guided search. See `references/02-guided-search-flow.md`.

Default to the guided search when in doubt. Phrases like "I am looking for a further education
program", "I want to do a Weiterbildung", "Which continuing education would fit me?", "I need a CAS
or MAS", or "something in management/data/education" are guided-search requests, not direct lookups.
Do not answer with a generic catalog list first. Ask the next missing intake question instead.

## Remember what the user shares (mandatory)

- As the user provides information — field/topic, prior education, desired start and duration,
  professional goal and whether a certificate is needed, budget — capture it to memory and reuse it.
- NEVER re-ask something the user (or memory) has already answered. Skip any guided-search question
  whose answer is already known.
- If essential context is missing and the answer depends on it, ask a single short question before
  calling tools — do not assume.

## Routing to alternatives

- After understanding the situation, if a paid MAS/DAS/CAS is not the right fit (cost, no certificate
  needed, age-specific audience, purely private interest), route per
  `references/03-alternative-routing.md` (and the alternatives map in the `wb-domain-knowledge` skill).

## Grounding & output (mandatory)

- All program facts (offerings, costs, dates, admission, ECTS) come from `uzh_wb_*` tools and/or
  `web_index_pages`. Never invent them.
- Keep questions and answers in the user's conversation language (German by default; a friendly
  Swiss-German tone is welcome).
- Ask one question at a time. Close with sources (Quellen) and preserve any disclaimers returned by
  tools.
