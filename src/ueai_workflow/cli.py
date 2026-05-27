from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

from .templates import COURSES, PROMPTS, STAGES


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\u4e00-\u9fff]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "course_project"


def write_if_missing(path: Path, text: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def stage_text(title: str, course: str, question: str, stage: dict[str, str]) -> str:
    return f"""# {stage["title"]}

项目题目：{title}

对应课程：{course}

研究问题：{question}

## 本阶段任务

{stage["description"]}

## AI辅助记录

使用时间：

使用工具：

使用提示词：

AI反馈摘要：

## 人工核验与修改

数据来源或课程材料核验：

教师要求对照：

人工修改说明：

## 本阶段产出

提交文件：

课堂展示或讨论记录：

教师反馈：
"""


def evidence_text(title: str, course: str, question: str) -> str:
    rows = [
        ("问题拆解", "00_problem/problem_brief.md"),
        ("数据路径", "01_data/data_plan.md"),
        ("模型与工具", "02_model/model_notes.md"),
        ("结果解释", "03_results/result_interpretation.md"),
        ("论文与报告", "04_writing/paper_outline.md"),
        ("AI反馈与人工修改", "05_feedback/ai_revision_log.md"),
        ("最终报告或论文", "04_writing/final_report_or_paper.md"),
    ]
    body = "\n".join(f"- [ ] {name}：`{file}`" for name, file in rows)
    return f"""# 课程成果归档清单

项目题目：{title}

对应课程：{course}

研究问题：{question}

## 归档项目

{body}

## 教学评价口径

学生需要说明数据来源、变量口径、模型逻辑、结果含义、AI反馈摘要和人工修改过程。

## 结项佐证口径

本清单可用于归档作业、小组报告、课程论文、AI辅助评阅记录和课堂反馈材料。
"""


def prompts_text() -> str:
    chunks = ["# AI提示词模板\n"]
    for key, prompt in PROMPTS.items():
        chunks.append(f"## {key}\n\n{prompt}\n")
    return "\n".join(chunks)


def new_project(args: argparse.Namespace) -> int:
    course_key = args.course_option or args.course or "generic"
    if course_key not in COURSES:
        raise SystemExit(f"Unknown course: {course_key}")
    question = args.question_option or args.question
    if not question:
        raise SystemExit("Missing research question. Use positional question or --question.")
    output = args.output_option or args.output
    course = COURSES[course_key]
    project_dir = Path(output or slugify(args.title)).resolve()
    project_dir.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    for stage in STAGES:
        path = project_dir / stage["file"]
        if write_if_missing(path, stage_text(args.title, course, question, stage)):
            created.append(str(path.relative_to(project_dir)))

    extra_files = {
        "README.md": f"""# {args.title}

对应课程：{course}

研究问题：{question}

本目录由 `ueai new` 创建，用于本科经管类课程的AI辅助数据、模型、写作和佐证归档工作流。
""",
        "prompt_templates.md": prompts_text(),
        "evidence/evidence_checklist.md": evidence_text(args.title, course, question),
    }
    for rel, text in extra_files.items():
        if write_if_missing(project_dir / rel, text):
            created.append(rel)

    print(json.dumps({"project": str(project_dir), "created": created}, ensure_ascii=False, indent=2))
    return 0


def status_project(args: argparse.Namespace) -> int:
    project_dir = Path(args.project).resolve()
    rows = []
    for stage in STAGES:
        path = project_dir / stage["file"]
        exists = path.exists()
        size = path.stat().st_size if exists else 0
        rows.append(
            {
                "stage": stage["id"],
                "title": stage["title"],
                "file": stage["file"],
                "exists": exists,
                "bytes": size,
            }
        )
    print(json.dumps({"project": str(project_dir), "stages": rows}, ensure_ascii=False, indent=2))
    return 0


def show_prompts(_: argparse.Namespace) -> int:
    print(prompts_text())
    return 0


def validate_project(args: argparse.Namespace) -> int:
    project_dir = Path(args.project).resolve()
    missing = [stage["file"] for stage in STAGES if not (project_dir / stage["file"]).exists()]
    evidence = project_dir / "evidence" / "evidence_checklist.md"
    if not evidence.exists():
        missing.append("evidence/evidence_checklist.md")
    result = {"project": str(project_dir), "complete": not missing, "missing": missing}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueai",
        description="Undergraduate economics AI workflow for data, modeling, writing, and evidence archiving.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new", help="Create a course project workflow.")
    new.add_argument("title", help="Project or paper title.")
    new.add_argument("question", nargs="?", help="Research question or course task.")
    new.add_argument("course", nargs="?", choices=sorted(COURSES), help="Course key.")
    new.add_argument("output", nargs="?", help="Output directory.")
    new.add_argument("--course", dest="course_option", choices=sorted(COURSES))
    new.add_argument("--question", dest="question_option", help="Research question or course task.")
    new.add_argument("--output", dest="output_option", help="Output directory.")
    new.set_defaults(func=new_project)

    status = sub.add_parser("status", help="Show workflow stage status.")
    status.add_argument("project")
    status.set_defaults(func=status_project)

    validate = sub.add_parser("validate", help="Validate required workflow files.")
    validate.add_argument("project")
    validate.set_defaults(func=validate_project)

    prompts = sub.add_parser("prompts", help="Print built-in prompt templates.")
    prompts.set_defaults(func=show_prompts)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
