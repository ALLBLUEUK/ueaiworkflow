---
description: Lint a ueai project — stage completeness, evidence count, integrity
---

Run all checks below and produce a single pass/fail report.

## Checks

| # | Check | Pass criterion |
|---|-------|----------------|
| C1 | Six stage files exist | All six `<NN>_xxx/<file>.md` present |
| C2 | Each stage has AI section | Every file's `## AI辅助记录` has ≥ 1 non-placeholder line |
| C3 | Each stage has human verification | Every file's `## 人工核验与修改` has ≥ 1 filled line (`数据来源` etc. not empty) |
| C4 | Evidence checklist exists | `evidence/evidence_checklist.md` present |
| C5 | Evidence count | ≥ 5 of 7 checklist items marked `[x]` |
| C6 | AI revision log | `05_feedback/ai_revision_log.md` non-empty with chronological entries |
| C7 | No fabricated numbers | Scan stage files; for any % / numerical claim, require a citation marker `[来源: ...]` |
| C8 | Academic integrity statement | `04_writing/paper_outline.md` has a "## 学术诚信声明" block |

## Output

```
ueai-validate report — <slug> — {{DATE}}

C1 [✓/✗] Six stage files
C2 [✓/✗] AI sections complete (N/6)
...

VERDICT: [READY FOR SUBMISSION | NEEDS WORK]

Required fixes:
- ...
```

Be strict. If `C7` finds any numeric claim without `[来源: ...]`, fail it and list the offending lines.
