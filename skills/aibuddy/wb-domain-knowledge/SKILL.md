---
name: wb-domain-knowledge
description: Orientation knowledge for UZH continuing education (Weiterbildung) — MAS/DAS/CAS types and alternative routes when a paid program is not the right fit. Load for Weiterbildung, weiterbilden, MAS, DAS, CAS questions; pairs with wb-advising.
---

# UZH Continuing Education — Domain Knowledge

## Purpose

- Provide curated, non-exhaustive orientation for UZH continuing education (Weiterbildung).
- Explain the MAS / DAS / CAS program types and the alternatives when a paid program is not the
  right fit.
- Keep the system prompt lean; all binding facts are retrieved at runtime.

## When to use

- The user asks about continuing education, MAS, DAS, CAS, certificate programs, or "weiterbilden".
- Read this together with the `wb-advising` skill, which drives the advising conversation.

## Program types (orientation)

- Read `references/01-program-types.md` for the CAS / DAS / MAS structure, typical ECTS, format,
  and admission basics.

## Alternatives map

- When a paid UZH continuing-education program is not the right fit (cost, no certificate needed,
  age-specific audience, purely private interest), read `references/02-alternatives-map.md` to route
  to the correct UZH offering.

## Grounding rules (mandatory)

- This skill is orientation only. NEVER invent program names, prices, dates, ECTS, admission
  criteria, or deep links.
- For any binding or current fact, retrieve via the continuing-education catalog tools (`uzh_wb_*`,
  see the `mcp-doc-query` skill) and/or `web_index_pages` (see the `mcp-web-index` skill).
- Preserve disclaimers, validity conditions, and source links returned by tools, in the user's
  language.

## Scope

- Covers UZH continuing education. For continuing education at other institutions (ETH, universities
  of applied sciences, etc.), state that this is outside scope and point the user to the respective
  institution.
