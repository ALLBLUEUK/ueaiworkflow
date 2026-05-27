---
name: ueai-result-interpret
description: Translate model output (tables, figures, log files) into undergrad-readable economic interpretation. Triggers at stage 03 or /ueai-stage 03.
---

# Result interpretation (stage 03)

## What you read

Whatever the student attached to `evidence/results/`. Common artefacts:

| File | What's in it |
|---|---|
| `tariffshock.sl4` viewed via ViewSOL | percentage changes in macro vars (qgdp, EV, qxw, pxw, ...) by region & sector |
| `tab1_did.tex` / `.csv` from `esttab` | regression table (coeff, se, R²) |
| `fig1_decomp.png` | welfare decomposition bar chart |
| log files | run-time messages |

## What you produce

A filled `03_results/result_interpretation.md` with:

1. **关键数值** — pull 3–6 numbers verbatim from outputs with **citation marker** `[来源: evidence/results/xxx]`.
2. **方向 / 量级 / 经济含义** — for each number give all three.
3. **部门差异 / 异质性** — name top + bottom 3 sectors / groups.
4. **稳健性边界** — when does the result flip / weaken? (sample, specification, shock size).
5. **与文献的对话** — 1–2 sentences placing the magnitude relative to existing literature, e.g. "Caliendo & Parro (2015) 报告 0.4% 的福利损失，我们的 0.7% 在合理范围"。

## Interpretation discipline

- **Never** state a percentage without sign and unit. "GDP 下降 0.3 个百分点" not "GDP -0.3".
- **Always** cite. Every number needs `[来源: evidence/results/<file>]`.
- Distinguish **方向** (sign) / **量级** (magnitude relative to GDP, exports, etc.) / **经济含义** (which agent loses, through what channel).
- For regression: coefficient + significance + cluster-robust SE + economic-magnitude line ("一个标准差的提升对应 Y 增加 X%").

## Output template

```markdown
# 结果解释

项目题目：{{TOPIC}}
对应课程：{{COURSE}}
研究问题：{{QUESTION}}

## 本阶段任务
把表格、图形和模型输出转化为经济学解释。

## AI辅助记录
- 使用时间：...
- 使用工具：...
- 使用提示词：prompts/result-interpret.md

### 关键数值
- 中国 GDP 量价分解中 `qgdp` 变动 **-0.34%** [来源: evidence/results/sl4_qgdp.csv]
- 中国 EV（等价变差）**-32.1 亿美元 (2017 基价)** [来源: evidence/results/sl4_ev.csv]
- 电子部门出口 `qxw("Electronics","China")` **-12.7%** [来源: evidence/results/sl4_qxw.csv]

### 方向 / 量级 / 经济含义
- GDP 下降方向符合理论预期；量级在 Caliendo–Parro 量级带内。
- EV 损失主要由出口部门福利下降驱动。
- 电子部门冲击最大；钢铁次之；服务业受益（贸易转移效应）。

### 异质性
- 受损前三部门：Electronics, Steel, Machinery
- 受益前三部门：Services, Agriculture, Light manufacturing

### 稳健性边界
- 关税幅度由 25pp 改为 10pp 时，GDP 影响缩为约 -0.13%。
- 取消关税收入回家庭的假设，福利损失扩大约 18%。
- HS 章节扩展到 84+85+73+76，结果增量小于 5%。

### 与文献对照
- Caliendo & Parro (2015) 报告 NAFTA 反事实福利变动约 0.08%–0.45%；本研究 0.34% 在合理量级。

## 人工核验与修改
- 数据来源或课程材料核验：
- 教师要求对照：
- 人工修改说明：

## 本阶段产出
- 提交文件：03_results/result_interpretation.md
- 表/图文件位置：evidence/results/
```

## What you DO NOT do

- Do not invent numbers if the student hasn't attached outputs. Instead, fill a TODO row and prompt the student to attach `evidence/results/<filename>`.
- Do not write policy recommendations here — those go in stage 04 (writing).
- Do not exceed 3 decimal places for course-level results.
