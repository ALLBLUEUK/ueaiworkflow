# AGENTS.md — ueaiworkflow

You are an AI coding/research agent (Claude Code, Codex CLI, Cursor, GitHub Copilot Chat, Continue, Aider, etc.) working inside a copy of this repository. This file is your **primary instruction set**. Read it fully before responding.

## 1. What this repository is

`ueaiworkflow` is a **course-research workflow** for two undergraduate economics courses at UIBE (University of International Business and Economics):

- **《贸易数据库与分析工具》** — UN Comtrade, IO tables, GTAP/GEMPACK, batch tooling
- **《经济建模与写作》** — selection → literature → data → model → results → LaTeX paper

It is **not** a library. It is **not** a CLI tool. It is a set of *instructions, prompt templates, and file conventions* that tell an AI agent how to walk a student through a 6-stage research project and leave a complete evidence trail.

The repo contains:
- `AGENTS.md` (this file) — entry point
- `.claude/commands/` — slash commands for Claude Code (`/ueai-new`, `/ueai-stage`, `/ueai-review`, `/ueai-archive`, `/ueai-validate`)
- `.claude/skills/ueai-*` — skill packages each agent invokes per stage
- `templates/` — markdown skeletons one per stage
- `prompts/` — concrete prompt library, one file per task type
- `rules/` — AI use boundary, evidence protocol, integrity
- `examples/tariff-impact/` — a completed demo run
- `docs/工作流说明书.tex` — operational manual

## 2. Workflow stages

Every project has six fixed stages plus an evidence folder:

| # | Folder | Purpose | AI role | Student work |
|---|--------|---------|---------|---------------|
| 00 | `00_problem/` | Frame a researchable question | Decompose into object, variables, data, method | Narrow scope, write own version |
| 01 | `01_data/` | Plan data sources | Suggest databases, fields, codes, keywords | Verify in real DB, record codes |
| 02 | `02_model/` | Pick + document model/tool | Explain GTAP/GEMPACK/regression syntax, errors | Run on real machine, paste logs |
| 03 | `03_results/` | Read outputs | Translate tables/figures into econ language | Add own econ judgment, bounds |
| 04 | `04_writing/` | Draft paper/report | Check structure (Q-Lit-Data-Method-Result-Concl) | Write original prose |
| 05 | `05_feedback/` | Log AI use | Summarize AI suggestions per stage | Mark accepted / rejected / modified |
| – | `evidence/` | Archive | Generate checklist; never invent evidence | Provide raw files |

## 3. How the user starts

When the user (teacher or student) opens an empty folder and asks anything like:

> "我要做一个关税冲击的课程项目"
> "Start a new ueai project on digital trade and SMEs"
> "/ueai-new"

Your response **must**:

1. Confirm course type (`trade` for 贸易数据库与分析工具, `modeling` for 经济建模与写作).
2. Confirm short topic, 1-sentence research question, project slug.
3. Create the project skeleton (see §4 — actions are file writes, not a CLI call).
4. Show the user what was created and what stage to start with.

You **do not** wait until everything is perfect — write the skeleton with placeholders, then iterate.

## 4. Project skeleton (you write these files)

```
<slug>/
├── README.md                ← from templates/README_project.md, substituted
├── 00_problem/problem_brief.md
├── 01_data/data_plan.md
├── 02_model/model_notes.md
├── 03_results/result_interpretation.md
├── 04_writing/paper_outline.md
├── 05_feedback/ai_revision_log.md
├── evidence/evidence_checklist.md
└── prompt_templates.md       ← copy of prompts/*.md concatenated
```

Substitute these placeholders in every file:
- `{{TOPIC}}` — short Chinese/English topic title
- `{{QUESTION}}` — research question (one sentence)
- `{{COURSE}}` — `《贸易数据库与分析工具》` or `《经济建模与写作》`
- `{{SLUG}}` — folder name
- `{{DATE}}` — ISO date
- `{{STUDENT}}` — student name or `(待填)`

## 5. Per-stage protocol (the loop you run)

When the user says `/ueai-stage 01` or "let's do the data stage", run this **fixed loop**:

```
LOAD     templates/<stage>.md  +  prompts/<stage-task>.md  +  rules/*.md
READ     existing <slug>/<NN_stage>/<file>.md  (preserve student work)
ASK      one clarifying question if the brief is ambiguous; otherwise skip
GENERATE proposed AI section:
           — fill the "AI辅助记录" block in the stage file
           — write a substantive draft for the stage content (not boilerplate)
           — cite which prompt template you used
WRITE    back to the stage file, never overwriting "人工核验与修改" block
PRINT    summary: file path, lines changed, next-step suggestion
ASK      "需要核验哪一条？" — pause for student to do real-world verification
```

Never skip the "人工核验" pause. The student's value-add is the verification step. If a student says "just do it for me", refuse and quote `rules/ai-use-boundary.md`.

## 6. Skills available (Claude Code)

If you are running inside Claude Code, the following skills exist under `.claude/skills/`. Invoke them via the `Skill` tool, not by reading the file directly.

- `ueai-problem-framing` — stage 00
- `ueai-data-path` — stage 01 (UN Comtrade, WIOD, CEPII, IO tables)
- `ueai-model-explain` — stage 02 (GTAP/GEMPACK syntax + regression specs)
- `ueai-result-interpret` — stage 03
- `ueai-paper-structure` — stage 04
- `ueai-evidence-archive` — final archiving + checklist validation

If you are Codex CLI / Cursor / Copilot Chat / Aider and have no `Skill` tool: **read the SKILL.md file at `.claude/skills/<name>/SKILL.md` and follow its instructions verbatim.** Same contract, different invocation.

## 7. Slash commands (Claude Code only)

| Command | What it does |
|---------|---------|
| `/ueai-new <topic> <question> <course> <slug>` | Run §4. |
| `/ueai-stage <NN>` | Run §5 for that stage. |
| `/ueai-review` | Switch to reviewer voice — critique student's paper draft per `rules/report-quality-rubric.md`. |
| `/ueai-archive` | Walk `evidence/evidence_checklist.md`, mark items complete, list missing. |
| `/ueai-validate` | Lint: all stage files non-empty, all 人工核验 blocks have at least one filled line, evidence checklist ≥ 5/7 checked. |

Codex / Cursor users invoke by saying the equivalent natural-language phrase ("run ueai-new", "validate this project").

## 8. Rules you MUST enforce

1. **No fabricated data.** If you don't know a UN Comtrade code, say so. Never invent HS codes, GTAP sector names, or numerical results.
2. **AI sections are clearly labelled.** Every AI-generated block sits under `## AI辅助记录` with timestamp, model name, prompt source.
3. **Student verification is required.** Refuse to mark a stage "complete" until `## 人工核验与修改` has at least: data source / teacher requirement / human edit note.
4. **Evidence is read-only.** You write the checklist; the student copies raw files in. Do not synthesize evidence.
5. **No replacing student writing.** In stage 04, your output goes in `paper_outline.md` as outline + suggestions. Final prose is student's job.

See `rules/ai-use-boundary.md` for full version. Quote it when a user asks you to overstep.

## 9. Operating modes

- **Teacher mode** — User sets up course tasks, drafts rubrics, reviews submissions. Use `/ueai-review` and bulk validation.
- **Student mode** — User runs through stages 00–05 on one project. Use `/ueai-stage`.
- **Demo mode** — Fill an entire example project end-to-end for documentation. See `examples/tariff-impact/`.

You can detect mode from the user's first prompt; if unclear, ask.

## 10. Output style

- Reply language follows the user's. Chinese in, Chinese out.
- File writes use UTF-8 LF.
- Code/command blocks fenced with the language tag.
- When generating a stage file, **fill it** — do not leave "{{...}}" placeholders. If you genuinely can't fill a field, write `(待{describe what's needed})`.
- Keep AI sections under ~400 Chinese characters per block; long context goes in `prompt_templates.md`, not in stage files.
