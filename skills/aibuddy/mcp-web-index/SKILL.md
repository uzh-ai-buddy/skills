---
name: mcp-web-index
description: Web-index MCP playbook for retrieval-only UZH website discovery — the fallback when document experts return no results or the user asks where to find something online (Webseite, Link, wo finde ich). Load before calling web_index_pages.
---

# AI Buddy Web-Index Playbook

## Purpose
- Provide canonical rules for when and how to use the `web_index_pages` tool.

## When to use
- Before calling `web_index_pages`.
- When primary tools return insufficient results, or the user explicitly requests websites or
  online resources.

## Tool overview

The `web_index_pages` tool searches through all catalog-backed UZH websites and returns relevant
page records with titles, URLs, snippets, and metadata. It does not synthesize an answer and does
not call the web-index LLM.

Use `web_index_pages` by default. Do not call the LLM-backed `web_index` answer tool unless
`web_index_pages` is unavailable and the user specifically asks for generated web-index
recommendations.

**CRITICAL**: For better ranking, naturally enrich the query with context info about
study_level and department/faculty (when known).

## Fallback priority (mandatory)

Always use `web_index_pages` as a fallback when:

1. Primary tools (course_data + expert tools) return insufficient or no results
2. The user explicitly requests websites, online resources, or "where can I find..."
3. You need to suggest relevant UZH websites for further information
4. Complex queries require additional resources beyond primary tools

## Coverage categories

The web-index pages tool covers websites organized by:

- General Info & Regulations
- Study Programs & Assessment
- Exams & Courses
- Career & Internships
- Health & Support Services
- Infrastructure & IT
- Associations & Exchange
- Theses & Research

## No results protocol (mandatory)

1. State explicitly: "I am sorry, but I do not have any specific information about this in my
   database. Let me provide you with a list of websites that might be relevant."
2. Use `web_index_pages` to search indexed UZH websites for relevant categories.
3. Present results with the user-responsibility notice using the **Website References** template
   from the system prompt.
4. Suggest appropriate human contact if still insufficient.
5. Offer an alternative search approach.

## Tool chaining pattern: No results → fallback

Primary tools return nothing → `web_index_pages` as fallback → present with user responsibility
notice → suggest direct contact if still insufficient.
