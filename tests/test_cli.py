from pathlib import Path

from ueai_workflow.cli import main


def test_new_and_validate(tmp_path: Path) -> None:
    project = tmp_path / "tariff"
    rc = main(
        [
            "new",
            "tariff impact",
            "--course",
            "trade",
            "--question",
            "How do tariffs affect exports?",
            "--output",
            str(project),
        ]
    )
    assert rc == 0
    assert (project / "00_problem" / "problem_brief.md").exists()
    assert (project / "evidence" / "evidence_checklist.md").exists()
    assert main(["validate", str(project)]) == 0


def test_prompts_command() -> None:
    assert main(["prompts"]) == 0


def test_new_positional_form(tmp_path: Path) -> None:
    project = tmp_path / "positional"
    rc = main(["new", "tariff impact", "How do tariffs affect exports?", "trade", str(project)])
    assert rc == 0
    assert (project / "prompt_templates.md").exists()
    assert main(["validate", str(project)]) == 0
