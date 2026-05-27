from __future__ import annotations


PROMPTS = {
    "problem": (
        "请将下列经管类课程问题拆解为研究对象、核心变量、可用数据、"
        "可能方法、结果展示方式和需要人工核验的口径：{question}"
    ),
    "data": (
        "请围绕下列研究问题列出可用数据库、字段、检索关键词、年份范围、"
        "国家地区口径和需要核验的限制：{question}"
    ),
    "model": (
        "请解释下列模型或工具输出的经济含义，重点说明变量方向、部门差异、"
        "政策冲击路径和结果边界：{result}"
    ),
    "paper": (
        "请按研究问题、文献逻辑、数据方法、结果解释、结论建议五个维度"
        "检查以下课程论文结构：{outline}"
    ),
    "revision": (
        "请根据AI反馈和人工修改稿整理课程论文修改说明，说明修改依据、"
        "保留内容和调整内容：{feedback}"
    ),
}


STAGES = [
    {
        "id": "00_problem",
        "title": "问题拆解",
        "file": "00_problem/problem_brief.md",
        "description": "把宽泛兴趣转化为可研究、可检验、可表达的课程任务。",
    },
    {
        "id": "01_data",
        "title": "数据路径",
        "file": "01_data/data_plan.md",
        "description": "记录数据库、字段、口径、检索过程和核验结果。",
    },
    {
        "id": "02_model",
        "title": "模型与工具",
        "file": "02_model/model_notes.md",
        "description": "记录工具命令、模型设定、报错处理和输出解释。",
    },
    {
        "id": "03_results",
        "title": "结果解释",
        "file": "03_results/result_interpretation.md",
        "description": "把表格、图形和模型输出转化为经济学解释。",
    },
    {
        "id": "04_writing",
        "title": "论文与报告",
        "file": "04_writing/paper_outline.md",
        "description": "组织摘要、引言、数据方法、结果、结论和参考文献。",
    },
    {
        "id": "05_feedback",
        "title": "AI反馈与人工修改",
        "file": "05_feedback/ai_revision_log.md",
        "description": "归档AI反馈摘要、人工选择、修改说明和最终版本。",
    },
]


COURSES = {
    "trade": "贸易数据库与分析工具",
    "writing": "经济建模与写作",
    "generic": "经管类本科课程",
}
