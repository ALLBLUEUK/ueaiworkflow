# GitHub Copilot Chat instructions

When the user works inside a repository that contains `AGENTS.md` at the root with the title `# AGENTS.md — ueaiworkflow`, treat that file as your **primary instruction set**.

Specifically:

1. Read `AGENTS.md` end-to-end before responding to any prompt.
2. Honor the six-stage workflow defined in §2.
3. When the user asks "scaffold a new project", "start a ueai project", "create a course paper folder", or types `/ueai-new`, follow `AGENTS.md §4` and write all stage files into a new sub-folder.
4. When the user asks for help on a specific stage, follow `AGENTS.md §5` — read the matching skill at `.claude/skills/ueai-<stage>/SKILL.md` and apply it verbatim.
5. Enforce `rules/ai-use-boundary.md` — no fabricated data, no skipping human verification, no writing student prose.

Output language: match the user's. Chinese in → Chinese out.

For Copilot-specific UX: when generating files, prefer `# file:` headers so the user can apply them with one click.
