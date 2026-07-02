# Fall 1 — User Already Has a Program in Mind (Direct Lookup)

Trigger only when the user names one exact UZH continuing-education program or asks about one exact
program title (e.g. "MAS in Banking and Finance", "the CAS Hochschuldidaktik").

Do NOT use this path merely because the user wants a continuing-education program, names a broad
topic, or mentions a credential type. Requests like "I am looking for a further education program",
"I want to do a Weiterbildung", "I need a CAS/MAS", or "something in management" go to
`references/02-guided-search-flow.md`.

Do NOT run the guided intake questions. Instead:

1. Confirm the program/topic only if it is genuinely ambiguous (one short question; otherwise
   proceed directly).
2. Retrieve facts with the continuing-education tools (see the `mcp-doc-query` skill):
   - `uzh_wb_program_finder_expert` — find / confirm the program.
   - `uzh_wb_courses_expert` — content, structure, modules.
   - `uzh_wb_costs_funding_expert` — costs and funding.
   - `uzh_wb_admission_registration_expert` — admission requirements, registration, deadlines.
   - `uzh_wb_degrees_credentials_expert` — degree / credential (CAS/DAS/MAS, ECTS).
   - Add `uzh_wb_services_contact_expert` / `uzh_wb_legal_quality_expert` when relevant.
3. Answer with the essentials the user needs: a short lead-in, then duration, costs, admission
   requirements, registration / next start, and the official link.
4. Remember the program of interest and any constraints the user stated (memory), so follow-up turns
   do not re-ask.
5. Offer a clear next step (registration link, contact, or info event) and close with Quellen.

If the named program cannot be found via the tools, say so plainly, offer the closest matches from
`uzh_wb_program_finder_expert`, and fall back to `web_index_pages`.
