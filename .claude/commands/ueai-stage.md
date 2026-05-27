---
description: Run one of the six ueai workflow stages (00..05)
---

Argument: the stage number (`00`, `01`, `02`, `03`, `04`, `05`) or its English name.

## Stage map

| NN | Folder | Skill | Prompt source |
|----|--------|-------|---------------|
| 00 | `00_problem/problem_brief.md` | `ueai-problem-framing` | `prompts/problem-framing.md` |
| 01 | `01_data/data_plan.md` | `ueai-data-path` | `prompts/data-path-*.md` |
| 02 | `02_model/model_notes.md` | `ueai-model-explain` | `prompts/model-*.md` |
| 03 | `03_results/result_interpretation.md` | `ueai-result-interpret` | `prompts/result-interpret.md` |
| 04 | `04_writing/paper_outline.md` | `ueai-paper-structure` | `prompts/paper-structure.md` |
| 05 | `05_feedback/ai_revision_log.md` | (no skill — log only) | `prompts/ai-revision-log.md` |

## Loop (AGENTS.md §5)

1. **Locate project.** Find the most recent ueai project in the cwd (folder containing `00_problem/`). Confirm with user if ambiguous.
2. **Load.** Read the stage file, the matching skill (`Skill` tool if available, else read the SKILL.md), and `rules/ai-use-boundary.md`.
3. **Preserve.** Note any existing `## 人工核验与修改` content. Never overwrite.
4. **Generate.** Produce a substantive AI section:
   - Use real domain knowledge for the topic (e.g. for UN Comtrade: name the actual fields — Reporter, Partner, Cmd Code, Trade Value, Trade Quantity, Year).
   - Cite which prompt template you used.
   - Add timestamp + model name to `AI辅助记录` block.
5. **Write back.** Edit the file in place. Leave `## 人工核验与修改` untouched if it already has student content; otherwise leave the placeholder.
6. **Print:** file path, line range you wrote, and one next-step suggestion.
7. **Pause.** Ask the user one verification question (e.g. "Please confirm HS code 8542 covers your product before moving on.").

## Stage 05 special case

For `05_feedback/ai_revision_log.md`, instead of generating new content, **summarize** all `## AI辅助记录` blocks from stages 00–04 into a chronological log with model name, prompt source, accepted/modified/rejected status.

## Errors

- Project folder not found → ask user to run `/ueai-new` first.
- Skill file missing → fall back to prompts/*.md.
- Stage file missing → recreate from templates/ and warn.
