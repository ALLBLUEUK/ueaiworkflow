# UEAI Workflow

AI assisted workflow for undergraduate economics courses that combine data work, modeling, reporting, and evidence archiving.

This repository is the software and workflow output of the UIBE undergraduate teaching reform project:

`数字经济与AI背景下经管类课程能力链条构建与教学协同机制探索`

Project number: `2025QN009`

Maintainer: Jia Ningyuan, School of International Trade and Economics, UIBE.

## What it does

`ueai` creates a structured course project for undergraduate economics tasks. It turns one course question into six linked folders:

1. problem framing
2. data path
3. model and tool notes
4. result interpretation
5. report or paper writing
6. AI feedback and human revision log

The workflow is designed for courses such as:

- `贸易数据库与分析工具`
- `经济建模与写作`
- other undergraduate economics courses that require data, modeling, and written reports

## Install

```bash
git clone https://github.com/ALLBLUEUK/ueaiworkflow.git
cd ueaiworkflow
python -m pip install -e .
```

## Start a course project

```bash
ueai new "美国加征关税的宏观影响分析" ^
  --course trade ^
  --question "如何分析美国加征关税对中国出口、福利和产业结构的影响" ^
  --output course-projects/tariff-impact
```

The command creates:

```text
00_problem/problem_brief.md
01_data/data_plan.md
02_model/model_notes.md
03_results/result_interpretation.md
04_writing/paper_outline.md
05_feedback/ai_revision_log.md
prompt_templates.md
evidence/evidence_checklist.md
```

## Check progress

```bash
ueai status course-projects/tariff-impact
ueai validate course-projects/tariff-impact
```

## Use with an AI coding assistant

This repository includes `AGENTS.md`, Claude plugin metadata, commands, skills, rules, and reviewer prompts. In Codex CLI, clone the repository into a project and keep `AGENTS.md` in the project root. In Claude Code, install it as a local plugin or copy the `skills`, `rules`, and `commands` folders into a project plugin directory.

Useful command prompts:

- `/ueai-new`: create a new course project
- `/ueai-review`: review a course paper or report using the teaching workflow

## Teaching use

For `贸易数据库与分析工具`, the workflow supports:

- UN Comtrade data path notes
- input output table notes
- GEMPACK and GTAP operation notes
- policy shock and welfare explanation
- group report evidence archiving

For `经济建模与写作`, the workflow supports:

- topic narrowing
- literature logic
- data and model plan
- result interpretation
- paper structure review
- AI feedback and human revision log

## Evidence for teaching reform closure

This repository can be submitted as the software or workflow evidence for the project output:

`经管类本科建模与写作AI智能体辅助软件及课程工作流`

Recommended evidence package:

- GitHub repository link
- generated course project sample
- AI prompt templates
- use manual PDF
- screenshots or exported logs from course use
- anonymized student output list

## Privacy

Do not commit student names, student IDs, grades, raw submissions, private course data, or unpublished paper drafts. Store those materials in local private evidence folders and use anonymized summaries in the repository.
