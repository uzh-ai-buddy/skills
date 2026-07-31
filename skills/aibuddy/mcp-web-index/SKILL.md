---
name: mcp-web-index
description: Discover catalog-backed UZH web resources and refresh eligible pages live. Use for website or link searches, user-supplied UZH URLs, any request whose answer depends on current content whatever its topic or content type, including freshness wording such as today, now, currently, latest, or this week, and when retrieved web evidence appears older than the period the user asks about.
---

# AI Buddy Web Index

Use `web_index_pages` for discovery and `web_index_fetch` for current content. Both tools are
catalog-bound; never treat them as unrestricted web access.

When current content matters, use Web Index before any document-retrieval expert.

## Select the workflow

### Discover, then refresh

Use this default when the user did not supply the resource:

1. Start with `web_index_pages` using only `query`. Put the user's topic, language, and known study
   or faculty context in the query text. Leave all optional filter fields unset; guessed filter
   values suppress valid results. Keep any refined retry query-only too.
2. Select only a result that clearly matches the requested resource. Do not fetch a merely
   plausible or loosely related result.
3. When current content matters, call `web_index_fetch` with the selected result's `id`.
4. Answer from the live result and cite its resolved URL.

Do not skip step 3 because another tool already returned an answer or because search metadata
suggests that live fetch may be unavailable. Call `web_index_fetch` and handle its explicit status.

This includes requests about what is true today, now, currently, or latest; frequently changing
menus, opening hours, schedules, deadlines, events, closures, and availability; and equivalent
freshness-sensitive wording.

### Refresh dated evidence

When another retrieval result identifies a web page but its date or content appears older than the
requested period:

1. Search `web_index_pages` for that resource.
2. Match the result by subject and URL where possible.
3. Live-fetch the matched result by `id`.
4. Prefer successful live evidence over the older indexed evidence.

Do not refresh merely because a page lacks a visible date. Use this path when the user asks for
current information or the retrieved evidence is visibly inconsistent with the requested date,
semester, or period.

### Use a supplied URL

When the user supplies a public UZH URL and asks about its current content, call
`web_index_fetch` with that URL as the first content-tool call. Do not require a catalog ID or call
`web_index_pages` or a document-retrieval expert first.

Never send credentials, signed tokens, personal data, or private URLs to either tool. Do not alter
the supplied URL to guess another resource.

### Discovery only

Use `web_index_pages` without live fetch when the user wants relevant official websites or when
freshness does not affect the answer.

## Handle results

- `success`: use the fetched content and cite the returned URL.
- `not_live_fetchable`: use indexed evidence only if it directly helps, state that it was not
  verified live, and make no claim about what is true today or currently.
  - Falling back to a document-retrieval expert does not lift this. Indexed content that repeats
    the same facts is not independent confirmation, because it came from the same page at an
    earlier time. The answer still carries the not-verified-live statement.
- `not_in_catalog` or no relevant search result: do not fetch another arbitrary URL. Say that
  current information could not be verified and offer the closest relevant official links.
- `pdf_resource`: use the appropriate document-retrieval expert for the PDF.
- `fetch_pending`: retry the same selector once. If it remains pending, say that current content is
  temporarily unavailable.
- `busy` or `upstream_error`: retry once only when useful, then report that current content could
  not be verified.
- `robots_blocked`: do not retry; report that live verification is unavailable.

Never turn an error, indexed snippet, or irrelevant search result into a current-content claim.
Keep retries bounded and do not repeat a successful fetch.

## Cite and disclose

Cite the resource you actually selected and fetched. Do not substitute a different page of the same
site because its content reads better.

Label every entry in the Sources section with where its content came from:

- Live fetch: `- [Title](url) — live fetch, 31 Jul 2026 15:30 UTC`, using the `fetched_at` value the
  tool returned. Give the date always and add the time when the fetch happened on the current day.
  `fetched_at` is when the page was last pulled from the site, so report it unchanged even when
  `cache.fetch_hit` is true.
- Indexed evidence: `- [Title](url) — indexed`. Add `, last fetched <date>` only when the retrieval
  result carries an indexing or fetch timestamp; never estimate or invent one.

German responses use `— live abgerufen, 31. Juli 2026 15:30 UTC` and `— indexiert`.

When any live fetch was attempted in the response, close the Sources section with one line:

- English: `_Live-fetched content reflects the page at the time shown and may have changed since._`
- German: `_Live abgerufene Inhalte entsprechen dem Stand zum angegebenen Zeitpunkt und können sich
  seither geändert haben._`

When live verification was attempted and did not succeed, the body of the answer states that plainly
before the facts it qualifies, and does not describe the information as current, today's, or
confirmed. The Sources line alone is not sufficient.

## No-results fallback

After ordinary retrieval is insufficient, use `web_index_pages` to find relevant official UZH
resources. Present only relevant results with their links. If none are useful, suggest the
appropriate human contact or a narrower search rather than inventing an answer.
