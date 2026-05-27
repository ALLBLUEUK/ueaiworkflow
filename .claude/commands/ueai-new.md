---
description: Scaffold a new ueai course-research project (6 stages + evidence)
---

You are starting a new ueaiworkflow project. Follow AGENTS.md §4 exactly.

## Input

Parse the user's message for:
- `课程` or `course` — must be `贸易数据库与分析工具` (`trade`) or `经济建模与写作` (`modeling`)
- `题目` or `topic` — short title
- `研究问题` or `question` — one-sentence research question
- `slug` — folder name (kebab-case, ASCII)

If any are missing, ask ONCE for the missing fields, then proceed.

## Steps

1. Verify current working directory is appropriate (ask user to confirm if unclear).
2. Create directory `<slug>/` and the 6 stage subfolders + `evidence/`.
3. For each template in `templates/`:
   - Read template
   - Substitute `{{TOPIC}}`, `{{QUESTION}}`, `{{COURSE}}`, `{{SLUG}}`, `{{DATE}}`
   - Write to `<slug>/<NN_xxx>/<file>.md`
4. Copy `prompts/*.md` concatenated into `<slug>/prompt_templates.md` with a TOC.
5. Print a tree of created files and the suggested next command (`/ueai-stage 00`).

## Rules

- Do not fill AI content yet — only the placeholder substitutions. AI content comes from `/ueai-stage NN`.
- Do not write into `evidence/` except the checklist file from the template.
- If `<slug>/` already exists with non-empty stage files, stop and ask whether to overwrite.

## Output format

```
✓ Created <slug>/
  ├── README.md
  ├── 00_problem/problem_brief.md
  ├── ... (6 stages)
  └── evidence/evidence_checklist.md

Next: /ueai-stage 00
```
