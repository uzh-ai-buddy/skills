---
name: mcp-web-index
description: Discover catalog-backed UZH web resources and refresh eligible pages live. Use for website or link searches, user-supplied UZH URLs, any request whose answer depends on current content whatever its topic or content type, including freshness wording such as today, now, currently, latest, or this week, and when retrieved web evidence appears older than the period the user asks about.
---

# AI Buddy Web Index

Use `web_index_catalogs` to discover available catalogs, `web_index_pages` to find pages within
them, and `web_index_fetch` for current content. These tools are catalog-bound; never treat them
as unrestricted web access.

When current content matters, use Web Index before any document-retrieval expert.

## Select the workflow

### Discover, then refresh

Use this default when the user did not supply the resource:

1. If an exact catalog ID is already known, use it. Otherwise call `web_index_catalogs` once and
   select catalogs from the returned producer-owned metadata. Never invent IDs or use a fixed
   topic-to-catalog routing map.
2. Search each confidently selected catalog separately with `web_index_pages`, passing its exact
   `catalog_id` and the same useful query based on the request and returned metadata. Leave other
   optional filters unset unless the user or returned metadata supplies an exact valid value.
   If catalog selection is uncertain, relevant metadata is truncated, or the discovery tool is
   unavailable, use query-only search without guessed filters.
3. Use plain search terms. Operators such as `site:` do not restrict this index; use the tool's
   structured filter parameters for restrictions, not operators embedded in `query`.
4. Select only a result that clearly matches the requested resource. Do not fetch a merely
   plausible or loosely related result.
5. When current content matters, call `web_index_fetch` with the selected result's `id`, then
   answer from the live result and cite its resolved URL.

If the first search returns no clearly relevant resource, try at most two distinct reformulations
per selected catalog. Preserve the user's subject and constraints, the selected `catalog_id`, and
any justified filters. Use synonyms or a translation into the language of returned titles and
descriptions; catalog vocabulary can guide wording but must not replace the requested subject.
Do not hardcode language, organization, topic, or URL rules. Stop early when a relevant resource
is found; otherwise report the retrieval gap rather than repeating ineffective searches or
concluding that the requested offering does not exist. This fallback does not change supplied-URL
handling or justify fetching a loosely related result.

Do not skip the live fetch because another tool already returned an answer or because search metadata
suggests that live fetch may be unavailable. Call `web_index_fetch` and handle its explicit status.

This includes requests about what is true today, now, currently, or latest; frequently changing
menus, opening hours, schedules, deadlines, events, closures, and availability; and equivalent
freshness-sensitive wording.

### Refresh dated evidence

When another retrieval result identifies a web page but its date or content appears older than the
requested period:

1. Use the catalog-aware discovery workflow above to search for that resource.
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

Use the discovery workflow above without live fetch when the user wants relevant official websites
or when freshness does not affect the answer.

## Handle results

- `success`: inspect whether the fetched content supports the requested subject, provider, and
  period before using it, then cite the returned URL. A successful fetch proves retrieval, not
  that every requested fact is present or current. A directory of other providers does not verify
  the requested provider's offering, and a historical schedule does not verify the current one.
  If the content is irrelevant or lacks the requested evidence, say what could not be verified;
  do not use that fetch to validate older indexed claims.
- `not_live_fetchable`: use indexed evidence only if it directly helps, state that it was not
  verified live, and make no claim about what is true today or currently.
  - Falling back to a document-retrieval expert does not lift this. Indexed content repeating the
    same facts came from the same page at an earlier time, so it is not independent confirmation.
- `not_in_catalog` or no relevant search result: do not fetch another arbitrary URL. Say that
  current information could not be verified and offer the closest relevant official links.
- `pdf_resource`: use the appropriate document-retrieval expert for the PDF.
- `fetch_pending`: retry the same selector once. If it remains pending, say that current content is
  temporarily unavailable.
- `busy` or `upstream_error`: retry once only when useful, then report that current content could
  not be verified.
- `robots_blocked`: do not retry; report that live verification is unavailable.
- `page_unavailable`: the page no longer answers at that address. Do not retry and do not fall back
  to indexed content as if it described the page today. Say the resource appears to have moved or
  been removed, and use the discovery workflow above to find the current equivalent.

Never turn an error, indexed snippet, or irrelevant search result into a current-content claim.
Keep retries bounded and do not repeat a successful fetch.

## Cite and disclose

Cite the resource you actually selected and fetched. Do not substitute a different page of the same
site because its content reads better.

The Sources section labels and the live-content disclaimer follow the output standard. Use
`fetched_at` as the live-fetch timestamp: it is when the page was last pulled from the site, so
report it unchanged even when `cache.fetch_hit` is true.

When live verification failed or fetched content did not support the requested current facts, the
body of the answer states that plainly before the facts it qualifies, and does not describe the
information as current, today's, or confirmed. The Sources line alone is not sufficient.

## No-results fallback

After ordinary retrieval is insufficient, use the discovery workflow above to find relevant official
UZH resources. Present only relevant results with their links. If none are useful, suggest the
appropriate human contact or a narrower search rather than inventing an answer.
