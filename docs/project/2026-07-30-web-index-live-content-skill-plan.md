# Web Index live-content skill plan

Date: 2026-07-30

## Plan identity

- Repository: `uzh-ai-buddy/skills`
- Branch: `enhance/web-index-live-content-skill`
- Worktree: `skills/trees/web-index-live-content-skill`
- Target: `dev`

## Goal

Make `mcp-web-index` the single source of truth for discovering and live-refreshing catalog-backed
UZH web content. Users may ask naturally; they do not need to provide a URL or catalog ID.

## Contract

1. Use the skill for website discovery, likely time-sensitive UZH web content, a supplied UZH URL,
   or indexed/RAG evidence that appears dated.
2. Without a URL, search `web_index_pages`, select a relevant result, then call
   `web_index_fetch(id=...)` when live verification is useful.
3. With a suitable user-supplied URL, call `web_index_fetch(url=...)` directly.
4. Never live-fetch an arbitrary URL learned outside the catalog.
5. Answer from successful live evidence.
6. For `not_live_fetchable`, use indexed evidence only with an explicit not-live-verified caveat
   and no current/today claim.
7. Route PDFs to document retrieval. Retry `fetch_pending` once; keep other retries bounded.
8. If no relevant catalog result or usable evidence exists, say current information is unavailable.

## Scope

- Update only `skills/aibuddy/mcp-web-index/SKILL.md`.
- Keep the skill concise; add no scripts, references, dependencies, or duplicate prompt policy.
- Do not change catalogs, MCP tools, scraping, deployment, or environments.

## Verification

- Run the repository validator and the system skill validator.
- Assert the skill contains discovery-by-ID, direct-URL, stale-evidence, catalog confinement,
  bounded retry, PDF, and fail-honest fallback rules.
- Forward-test representative no-URL, direct-URL, stale-evidence, and unavailable-live-fetch cases
  through independent review without live mutations.
- Review the committed change for clarity, token cost, and contradictions.

## Progress

- [x] User approved the skill-first design and fallback.
- [x] MCP contract and current catalog coverage verified.
- [x] Skill implemented.
- [x] Repository and system skill validators pass.
- [ ] Forward tests pass.
- [ ] Independent review complete.
- [ ] PR published to `dev`.
