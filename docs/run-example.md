# Run Example

This example uses the trade data course scenario.

## Commands

```bash
git clone https://github.com/ALLBLUEUK/ueaiworkflow.git
cd ueaiworkflow
pip install .
ueai new "美国加征关税的宏观影响分析" "如何分析美国加征关税对中国出口福利和产业结构的影响" trade tariffimpact
ueai validate tariffimpact
ueai status tariffimpact
```

## Creation Output

```json
{
  "project": "tariffimpact",
  "created": [
    "00_problem/problem_brief.md",
    "01_data/data_plan.md",
    "02_model/model_notes.md",
    "03_results/result_interpretation.md",
    "04_writing/paper_outline.md",
    "05_feedback/ai_revision_log.md",
    "README.md",
    "prompt_templates.md",
    "evidence/evidence_checklist.md"
  ]
}
```

## Validation Output

```json
{
  "project": "tariffimpact",
  "complete": true,
  "missing": []
}
```

## Generated Project Tree

```text
tariffimpact/
  00_problem/problem_brief.md
  01_data/data_plan.md
  02_model/model_notes.md
  03_results/result_interpretation.md
  04_writing/paper_outline.md
  05_feedback/ai_revision_log.md
  evidence/evidence_checklist.md
  prompt_templates.md
  README.md
```

## Example Stage File

`00_problem/problem_brief.md` records:

```text
项目题目：美国加征关税的宏观影响分析
对应课程：贸易数据库与分析工具
研究问题：如何分析美国加征关税对中国出口福利和产业结构的影响
本阶段任务：把宽泛兴趣转化为可研究、可检验、可表达的课程任务。
```

## Example Evidence Checklist

`evidence/evidence_checklist.md` asks the teacher or student to archive:

```text
问题拆解：00_problem/problem_brief.md
数据路径：01_data/data_plan.md
模型与工具：02_model/model_notes.md
结果解释：03_results/result_interpretation.md
论文与报告：04_writing/paper_outline.md
AI反馈与人工修改：05_feedback/ai_revision_log.md
最终报告或论文：04_writing/final_report_or_paper.md
```

The example shows that the workflow creates a reproducible course project folder, checks required stage files, and produces an evidence checklist suitable for teaching reform closure materials.
