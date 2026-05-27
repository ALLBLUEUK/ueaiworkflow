---
name: ueai-evidence-archive
description: Walk the evidence checklist, count what's archived, list missing files. Triggers at /ueai-archive or end of stage 05.
---

# Evidence archive

## The 7-item checklist

Every project's `evidence/evidence_checklist.md` tracks these:

| # | Item | Where it lives |
|---|---|---|
| 1 | 问题拆解 | `00_problem/problem_brief.md` |
| 2 | 数据路径 | `01_data/data_plan.md` + raw exports under `evidence/data/` |
| 3 | 模型与工具 | `02_model/model_notes.md` + run artefacts under `evidence/model/` |
| 4 | 结果解释 | `03_results/result_interpretation.md` + tables/figures under `evidence/results/` |
| 5 | 论文与报告 | `04_writing/paper_outline.md` + final pdf under `evidence/paper/` |
| 6 | AI反馈与人工修改 | `05_feedback/ai_revision_log.md` |
| 7 | 最终报告或论文 | `evidence/paper/final.pdf` (or .docx) |

## What "complete" means

- Item is `[x]` if BOTH the markdown stage file AND the `evidence/<sub>/` raw artefact exist non-empty.
- Item is `[~]` if only the markdown is present but raw artefacts are missing (allowed for items 1, 6).
- Item is `[ ]` if neither is present.

## What you do

1. Open `evidence/evidence_checklist.md`.
2. For each item, do the check above. Update the `[ ]` → `[x]` / `[~]`.
3. Append a `## 归档时间` block with ISO date.
4. Append a `## 缺失项` list of remaining `[ ]` items.
5. Append a `## 建议补充` block — up to 5 specific files to add.

## Output discipline

- Do not delete student-written sections of the checklist.
- Do not fabricate evidence — if a file is missing, mark missing, don't invent.
- The final summary line must include a fraction: `5/7 已归档` etc.

## Used by

`/ueai-archive` slash command.
