# 示范项目：美国加征关税的宏观影响分析（电子部门）

- **课程**：《贸易数据库与分析工具》
- **研究问题**：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何
- **slug**：tariff-impact
- **创建日期**：2026-05-27
- **学生**：（示范用，非真实学生提交）
- **AI 助手**：Claude Opus 4.7 + GTAP 11 / GEMPACK 12 / Stata 18（学生本地）

本项目是 `ueaiworkflow` 仓库自带的**端到端示范**。它演示了如何用 6 个 `/ueai-stage` 命令把一道课程题目从拆解一路推进到归档。

> 注意：此示范项目的数值结果基于 Caliendo & Parro (2015)、Itakura & Lee (2019)、Amiti et al. (2019) 等公开文献的量级带，并非项目负责人对 25pp 关税的独立 GTAP 求解。真实学生项目须在本地跑通 GTAP/GEMPACK 并把 `.sl4` 与 `.har` 放入 `evidence/`。

## 文件清单

```
tariff-impact/
├── README.md                                           ← 本文件
├── 00_problem/problem_brief.md
├── 01_data/data_plan.md
├── 02_model/model_notes.md
├── 03_results/result_interpretation.md
├── 04_writing/paper_outline.md
├── 05_feedback/ai_revision_log.md
├── evidence/
│   ├── evidence_checklist.md
│   ├── data/                  ← 学生从 UN Comtrade 导出的 CSV
│   ├── model/                 ← .cmf / .sl4 / .har / .log
│   ├── results/               ← 加工后 csv / 图 / .tex 表
│   └── paper/                 ← 最终 PDF
└── prompt_templates.md         ← 本项目使用的提示词副本
```

## 推进顺序

```
/ueai-new ...          → 生成上述骨架（已完成）
/ueai-stage 00         → 00_problem/problem_brief.md
/ueai-stage 01         → 01_data/data_plan.md
/ueai-stage 02         → 02_model/model_notes.md
/ueai-stage 03         → 03_results/result_interpretation.md
/ueai-stage 04         → 04_writing/paper_outline.md
/ueai-stage 05         → 05_feedback/ai_revision_log.md
/ueai-review           → 评阅追加进 05_feedback
/ueai-archive          → 写入 evidence/evidence_checklist.md
/ueai-validate         → 报告 7/7 已归档 → READY FOR SUBMISSION
```

完整交互记录见 `docs/demo-transcript.md`（仓库根目录）。
