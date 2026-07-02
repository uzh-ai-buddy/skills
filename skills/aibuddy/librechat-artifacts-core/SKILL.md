---
name: librechat-artifacts-core
description: Canonical wrapper rules and identifiers for LibreChat artifacts.
---

# LibreChat Artifacts Core

## Purpose
- Single source of truth for LibreChat artifact wrapper syntax and identifiers.
- Update this skill whenever LibreChat’s artifact system or prompt rules change.

## When to use
- **Before** emitting any `:::artifact{...}` block.
- When updating or iterating on existing artifacts.

## Wrapper rules (mandatory)
- The artifact block **must be top-level** (do not wrap the `:::artifact...` block in a code fence).
- Always include **identifier**, **type**, and **title** attributes.
- Use **stable kebab-case identifiers**; reuse the same identifier for updates.
- One artifact per assistant message.
- Only the **inner content** is fenced with triple backticks.
- Always close with `:::` on its own line.
- Provide complete content (no placeholders or “rest unchanged”).
- Avoid the exact sequence `:::` anywhere inside artifact content (LibreChat edit parsing uses `:::`
  to find the end of the artifact).

## Current policy
- Default to `type="text/markdown"` (or `text/md`).
- Other types are only allowed when a **use-case skill** you have read explicitly instructs that
  type (for example, a weekly timetable skill may instruct `application/vnd.react`).

## Formatting conventions
- Whenever presenting multiple comparable data points (courses, module options, deadlines), use a
  Markdown table with clear headers instead of bullet lists unless the content is sequential.
- Mermaid diagrams are allowed only when a **use-case skill** explicitly instructs them. Never use
  Mermaid class syntax with `:::` inside an artifact.

## Example (correct format)

````text
:::artifact{identifier="example-doc" type="text/markdown" title="Example Document"}
```md
# Title

## Summary
- ...

## Details
- ...
```
:::
````
