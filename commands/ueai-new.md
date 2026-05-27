---
description: Start a new undergraduate economics course project.
---

# /ueai-new

Create a new course project using the `ueai` workflow.

Ask the user for:

- course name
- working title
- research question
- expected output: weekly assignment, group report, or course paper

Then run:

```bash
ueai new "<title>" --course generic --question "<question>" --output "<folder>"
```

After scaffolding, guide the user through:

1. `00_problem/problem_brief.md`
2. `01_data/data_plan.md`
3. `02_model/model_notes.md`
4. `03_results/result_interpretation.md`
5. `04_writing/paper_outline.md`
6. `05_feedback/ai_revision_log.md`

For public evidence, remove student names, student IDs, and raw grade information.
