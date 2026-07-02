:::artifact{identifier="procedure-decision-tree" type="text/markdown" title="Procedure Decision Tree"}
```md
## {{Procedure name}}

```mermaid
flowchart TD
  A[{{Trigger or question}}] -->|Yes| B[{{Action step}}]
  A -->|No| C[{{Alternative action}}]
  B --> D[{{Required document or evidence}}]
  D -->|Valid| E[{{Outcome / next step}}]
  D -->|Missing| F[{{Consequence or follow-up}}]
```

**Notes**
- Replace placeholders with official wording from the regulation or office guidance.
- Confirm deadlines and required documents from official sources.
```
:::
