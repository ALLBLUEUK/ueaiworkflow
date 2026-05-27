---
description: Walk evidence_checklist.md, mark items, list missing files
---

You generate the archive checklist. Do NOT invent evidence.

## Steps

1. Open `<slug>/evidence/evidence_checklist.md`.
2. For each `[ ]` item in the checklist:
   - If the referenced path exists and is non-empty, mark `[x]`.
   - If it exists but is the template's placeholder text only, mark `[~]` and note "仅模板".
   - If it does not exist, leave `[ ]`.
3. Add a `## 归档时间` block with ISO date.
4. Below the checklist add `## 缺失项`：list every still-`[ ]` item with the exact missing file path.
5. Below that add `## 建议补充`：max 5 suggestions of what to add (e.g. "请把 UN Comtrade 导出的 .csv 放入 evidence/data/").

## Output

Print the updated checklist to the chat, plus a one-line summary:
`✓ 7/7 已归档` or `⚠ 5/7 已归档，缺 2 项（见上）`.

If `≥ 6/7` are complete, suggest the user run `/ueai-validate`.
