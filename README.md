# UZH AI Buddy Skills

LibreChat native skill source repo for AI Buddy and EducationAI.

## Layout

```text
skills/
  aibuddy/<skill-id>/SKILL.md
  eduai/<skill-id>/SKILL.md
skills-manifest.yaml
scripts/validate-skills.py
```

Each direct child of `skills/<source>/` is one LibreChat skill. The directory name is the stable skill id used by deployment seed config.

## Branches

- `dev`: development sync source
- `stg`: staging sync source, promoted from `dev`
- `prd`: production sync source, promoted from `stg`

Do not rename source ids or skill directories after LibreChat has synced them without a migration plan. LibreChat mirror identity depends on source id plus skill path.

## Validation

Run before pushing:

```bash
python3 scripts/validate-skills.py
```

Validation checks manifest coverage, skill structure, frontmatter, referenced files, unsafe paths, duplicate skill names, size limits, and common secret patterns.
