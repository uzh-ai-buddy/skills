---
name: oec-domain-knowledge
description: Curated OEC domain knowledge resources for program structure and rules.
---

# OEC Domain Knowledge

## Purpose

- Provide curated, non-exhaustive program structure knowledge for OEC BA/MA programs.
- Support program-specific guidance without bloating the system prompt.

## When to use

- Program structure, assessment year, mandatory modules, and study planning rules.
- Program-specific questions where curated knowledge helps orient the answer.

## Coverage (general)

- OEC departments: Finance (DF), Informatics (IFI), Economics (ECON), Business Administration
  (DBA).
- Use the full program names in the user's language. Internal IDs are for internal reference only.

## Resource selection (mandatory)

- Use only the reference files listed below. Do not assume unlisted optional program resources
  exist.

### BA resources

- If `study_level=BA` → always read `references/oec-ba-assessment.md`.
- If `study_level=BA` and `department=IFI` → read
  `references/oec-bsc-informatics.md`.
- If `study_level=BA` and `department` is `DF`, `ECON`, or `DBA` → read
  `references/oec-ba-business-economics.md`.
- If `study_level=BA` and `department` is unknown, ask a short clarification before reading
  program-specific resources (assessment is still safe to read).

### MA resources

- If the user indicates **MSc Quantitative Finance (MSc_QF)** → read
  `references/oec-msc-quant-finance.md` and do NOT treat this as `MAOEC`.
- If `study_level=MA` → read `references/oec-ma-business-economics.md`.
- If `study_level=MA` and the user is in Informatics / `department=IFI` → also read
  `references/oec-msc-informatics.md`.

Optional program resources not yet bundled:

- `oec-ba-finance.md`
- `oec-ba-business-admin.md`
- `oec-ba-economics.md`
- `oec-ma-finance.md`
- `oec-ma-business-admin.md`
- `oec-ma-economics.md`
- `oec-ma-management-economics.md`
- `oec-msc-quant-finance.md`

## Usage rules

- Treat all lists as curated orientation. For binding and up-to-date requirements, always verify
  with `course_data` and/or the relevant catalog doc-query tool.
- Minors must be checked in the course catalog using course-data tools.

## Out-of-scope program reminder

For study programs outside OEC or outside the supported list, use this disclaimer (translate to
the user's language):

I'm afraid that’s uncharted territory for me. My expertise lies in administrative and
organizational questions within the Faculty of Business, Economics and Informatics. For courses
or programs in other departments, I recommend checking the UZH Course Catalogue or the websites
of the respective faculties.
