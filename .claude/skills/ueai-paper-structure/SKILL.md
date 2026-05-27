---
name: ueai-paper-structure
description: Build/check the five-dimension structure of an undergrad econ paper. Outputs an outline, never the final prose. Triggers at stage 04 or /ueai-stage 04.
---

# Paper structure (stage 04)

## Five-dimension rubric

| Dim | Section | Required content |
|---|---|---|
| 1 研究问题 | 引言末段 | one-sentence Q, why it matters, what's new |
| 2 文献逻辑 | 文献综述 | ≥ 5 refs, explicit gap, ≤ 800 字 |
| 3 数据方法 | 数据 + 方法 | DB names, time window, identification or model assumption |
| 4 结果解释 | 结果 | every reported number has direction + magnitude + meaning + citation |
| 5 结论建议 | 结论 | bounded; explicit "本研究不能说明…" |

Plus mandatory:
- 摘要 (中英) ≤ 300 字
- 关键词 3–6 个
- 参考文献 (GB/T 7714 或 APA)
- 学术诚信声明（含 AI 使用说明）

## What you produce

A filled `04_writing/paper_outline.md` — **outline + bullet evidence per section**, NOT finished prose.

Structure:

```markdown
# 论文与报告大纲

项目题目：{{TOPIC}}
对应课程：{{COURSE}}
研究问题：{{QUESTION}}

## 摘要（中文，≤ 300 字）
[占位 — 由学生根据完成稿撰写。AI 仅在所有阶段定稿后辅助压缩。]

## 摘要（英文，≤ 200 words）
[same]

## 关键词
- 关税冲击；GTAP；福利分解；电子产业；中国

## 1 引言
- 1.1 研究背景：中美贸易摩擦演进、Section 301 时间线
- 1.2 文献空白：现有研究多聚焦 2018–2019，缺 2020+ 数据
- 1.3 研究问题：{{QUESTION}}
- 1.4 边际贡献（≤ 3 条）
  - 用 GTAP 11 base year 2017 重新校准
  - 聚焦电子部门
  - 分解福利来源

## 2 文献综述
- 2.1 贸易战福利效应：Amiti et al. (2019), Fajgelbaum et al. (2020) ...
- 2.2 GTAP 应用：Caliendo & Parro (2015), Itakura & Lee (2019) ...
- 2.3 中国视角：陈勇兵 等 (2020), 余淼杰 (2019) ...
- gap 句："现有研究对 (i) 部门异质性、(ii) 中长期回应缺乏分解"

## 3 数据与方法
- 3.1 数据来源（引 01_data/data_plan.md）
- 3.2 模型设定（引 02_model/model_notes.md 关键公式）
- 3.3 识别 / 假设：完全竞争、Armington、关税收入返还家庭

## 4 结果
（引 03_results/result_interpretation.md 的每一条；每个数字必须带 [来源: ...]）
- 4.1 总体福利
- 4.2 部门差异
- 4.3 稳健性

## 5 结论与政策含义
- 5.1 主要发现（≤ 3 条）
- 5.2 边界：本研究不能说明 ...
- 5.3 政策含义（≤ 3 条，每条附假设）

## 参考文献
（学生填，至少 12 条；外文 ≥ 5）

## 学术诚信声明
本研究的数据检索、模型设定、结果解释和论文写作过程中，使用了 AI 辅助工具 {{MODEL}}。
AI 提示词模板、AI 反馈摘要与人工修改记录见 05_feedback/ai_revision_log.md。
研究问题确立、数据核验、模型选择、结果判读和最终文本由作者本人负责。

## AI辅助记录
- 使用时间：...
- 使用工具：...
- 使用提示词：prompts/paper-structure.md
- AI反馈摘要：[本大纲]

## 人工核验与修改
- 数据来源或课程材料核验：
- 教师要求对照：
- 人工修改说明：
```

## What you DO NOT do

- Do not write the abstract, introduction, or any prose section in full. Bullet points only.
- Do not invent references. Quote real ones the student can verify; if uncertain, mark `[ref待补]`.
- Do not omit the 学术诚信声明 block — it is mandatory.
- Do not skip the citation markers in §4.
