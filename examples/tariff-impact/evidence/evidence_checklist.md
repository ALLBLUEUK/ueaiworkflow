# 课程成果归档清单

项目题目：美国加征关税的宏观影响分析（电子部门）
对应课程：《贸易数据库与分析工具》
研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何

## 归档项目

- [x] 1. 问题拆解：`00_problem/problem_brief.md`
- [~] 2. 数据路径：`01_data/data_plan.md` + `evidence/data/` *(示范项目仅提供数据计划；学生须导出 CSV)*
- [~] 3. 模型与工具：`02_model/model_notes.md` + `evidence/model/` *(示范项目仅提供 .cmf 模板与 .bat；学生须在本地跑通并归档 .sl4/.har/.log)*
- [~] 4. 结果解释：`03_results/result_interpretation.md` + `evidence/results/` *(示范数值为占位；学生须用本地求解数值替换)*
- [x] 5. 论文与报告：`04_writing/paper_outline.md`
- [x] 6. AI 反馈与人工修改：`05_feedback/ai_revision_log.md`
- [ ] 7. 最终报告或论文：`evidence/paper/final.pdf` *(示范项目不提供最终成稿)*

## 教学评价口径

学生需要在论文 / 报告中说明：
1. 数据来源（数据库名称、年份、字段、检索路径）
2. 变量口径（HS 编码、国家口径、单位、平减基期）
3. 模型逻辑（假设、识别策略、敏感性参数）
4. 结果含义（方向、量级、经济解释）
5. AI 反馈摘要与人工修改过程

## 结项佐证口径

本清单可用于归档作业、小组报告、课程论文、AI 辅助评阅记录和课堂反馈材料。

## 归档时间

2026-05-27（示范项目归档；状态：4/7 完整 + 3/7 占位等学生本地核验）

## 缺失项

- 7. `evidence/paper/final.pdf` — 示范项目不含成稿。真实学生须用 LaTeX 编译后归档。

## 建议补充

1. 把 UN Comtrade 检索结果导出 `.csv` 放入 `evidence/data/`
2. 把 GTAP 求解的 `.sl4` 与 `.har` 文件放入 `evidence/model/`
3. 用 ViewSOL 把 `qgdp`, `EV`, `qxw` 导出为 CSV，放入 `evidence/results/`
4. 把数据库与 ViewSOL 截图放入 `evidence/data/screenshots/` 与 `evidence/model/screenshots/`
5. 完稿 LaTeX 编译生成 `evidence/paper/final.pdf`
