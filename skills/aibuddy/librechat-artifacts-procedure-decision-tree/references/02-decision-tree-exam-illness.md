:::artifact{identifier="exam-illness-decision-tree" type="text/markdown" title="Exam Illness Decision Tree"}
```md
## Exam day illness: decision tree

```mermaid
flowchart TD
  A[Ill on exam day?] -->|Yes| B[Contact the exam office immediately]
  A -->|No| C[Attend the exam as scheduled]
  B --> D[Provide medical certificate as required]
  D -->|Accepted| E[Office confirms excused absence]
  D -->|Not accepted| F[Absence may count as fail]
  E --> G[Register for the next exam date]
```

**Notes**
- Always verify deadlines and document requirements in the official regulation.
```
:::
