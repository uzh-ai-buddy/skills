:::artifact{identifier="study-plan-scenario-compare" type="text/markdown" title="Study Plan Scenarios"}
```md
## Scenario A: Exchange Semester

| Semester | Module / Track | ECTS | Prerequisites / Status | Risk / Notes |
| --- | --- | --- | --- | --- |
| HS26 | Core Bachelor modules | 30 | *Assessment completed* | Keep workload balanced before exchange. |
| FS27 | Exchange window | 30 | Learning agreement | Track transfer eligibility. |
| HS27 | Core Bachelor modules | 24 | *Exchange credits recognized* | Substitute electives if transfer is partial. |

**ECTS overview (Scenario A)**
- Assessment: {{assessment_ects}} / 60 ECTS
- Core Bachelor: {{core_ects}} / 90 ECTS
- Electives & Thesis: {{elective_ects}} / 30 ECTS
- **Total projected**: {{total_ects}} / 180 ECTS

## Scenario B: Internship Semester

| Semester | Module / Track | ECTS | Prerequisites / Status | Risk / Notes |
| --- | --- | --- | --- | --- |
| HS26 | Core Bachelor modules | 30 | *Assessment completed* | Build prerequisites early. |
| FS27 | Internship + electives | 18 | Internship contract | Internship hours may reduce study load. |
| HS27 | Core Bachelor modules | 30 | *Internship completed* | Use electives to catch up. |

**ECTS overview (Scenario B)**
- Assessment: {{assessment_ects}} / 60 ECTS
- Core Bachelor: {{core_ects}} / 90 ECTS
- Electives & Thesis: {{elective_ects}} / 30 ECTS
- **Total projected**: {{total_ects}} / 180 ECTS

**Impact summary**
- Delta: Scenario A shifts {{module}} to {{semester}} due to exchange credits.
- Delta: Scenario B reduces elective load in FS27 to allow internship hours.

**Risks & mitigations**
- If exchange credits are not recognized → reserve {{makeup_module}} in HS27.
- If internship hours exceed plan → lower elective load in FS27.

**Milestones & follow-ups**
- [ ] Submit exchange learning agreement by {{deadline}}.
- [ ] Confirm internship eligibility or contract by {{semester}}.
- [ ] Verify credit transfer rules with the program office.

**What-if adjustments**
- If exchange credits are short → add {{makeup_module}} in {{semester}}.
- If internship workload is high → shift {{module}} to {{semester}}.
```
:::
