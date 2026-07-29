---
name: mcp-doc-query
description: Doc-query MCP playbook for expert routing, filtering, and disclaimer handling.
---

# EducationAI Doc-Query Playbook

## Purpose
- Provide canonical routing and filtering rules for doc-query expert tools.
- Ensure disclaimers are handled correctly.

## When to use
- Before calling any doc-query expert tool.

## Expert routing

Always use one of the expert tools provided by the doc-query MCP for retrieval tasks.
Exception: if the query is conversational and does not require retrieval.

## Scope/Topic filtering (mandatory)

For retrieval accuracy, use context to filter and to enrich the query text.
- If the user query includes a specific topic, filter the query to that topic.
- If the user query is broad, enrich it with relevant context to narrow down the retrieval scope.

## Expert response handling (mandatory)

### Expert disclaimers

When any expert tool returns a disclaimer, warning, or legal notice, include it in the response.
Preserve the disclaimer's meaning, scope, and conditions exactly.

If the disclaimer is not in the user's conversation language, translate it faithfully into the
user's language (as literally as possible; no additions or omissions) so the overall reply remains
in exactly one language.

Embed expert disclaimers naturally within the response text. Do not use meta-language like
"Wichtiger Hinweis vom Expertentext (wörtlich):" or "The expert says:". Present disclaimers as if
they are part of the guidance, maintaining the natural flow of the response.

Include expert disclaimers toward the end of the response, not in the middle of the main content.