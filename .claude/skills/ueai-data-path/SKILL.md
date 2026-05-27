---
name: ueai-data-path
description: Generate a concrete data retrieval plan for an econ course project. Names actual databases, fields, HS/ISIC codes, year ranges. Triggers at stage 01 or /ueai-stage 01.
---

# Data path (stage 01)

## Databases you may reference

| Database | URL stub | Key fields | Years |
|---|---|---|---|
| UN Comtrade | comtradeplus.un.org | Reporter, Partner, Cmd Code (HS), Trade Flow, Trade Value (USD), Netweight (kg), Year | 1962– |
| WITS | wits.worldbank.org | wraps Comtrade + tariff (MFN/AVE) | 1988– |
| GTAP Database 11 | gtap.agecon.purdue.edu | 65 sectors × 141 regions, base year 2017 | 2017 |
| WIOD 2016 | wiod.org | IO 56 sectors × 44 economies | 2000–2014 |
| CEPII BACI | cepii.fr | cleaned Comtrade w/ harmonized HS | 1995– |
| China Customs (CCD) | (proprietary) | firm × HS8 × month | 2000–2016 |
| CNRDS / WIND / CEIC | by subscription | firm/macro panel | varies |

## What you produce

A filled `01_data/data_plan.md` with:

1. **数据库选择** — primary + fallback, with 1-sentence justification.
2. **字段清单** — exact column names you expect to retrieve (use the database's actual field names — Reporter, Cmd Code, Trade Value, not "country" / "code" / "amount").
3. **检索关键词与编码** — HS codes (use 4-digit or 6-digit), country ISO codes, year window.
4. **检索路径** — actual click path or API URL (e.g. `https://comtradeplus.un.org/TradeFlow?Frequency=A&...&cmdCode=8542&flowCode=X`).
5. **核验清单** — minimum 5 items the student must verify in the actual DB (HS code coverage, unit, exchange rate base, reporter vs partner mirror, year availability, etc.).

## Concrete examples to ground students

For **关税冲击 / 加征关税**:
- Primary: UN Comtrade (annual, HS6) — Reporter=China, Partner=USA, Trade Flow=Export, Cmd Code=84,85 chapters, 2017–2024
- Tariff data: WITS MFN + USTR Section 301 list
- HS chapters likely to bind: 84 (machinery), 85 (electronics), 73 (steel), 76 (aluminium)

For **数字基础设施**:
- Primary: ITU World Telecommunication/ICT Indicators; OECD Digital Economy Indicators
- China-only: NBS digital economy sub-indices, China Internet Network Information Center (CNNIC) reports

For **绿色金融 / FDI**:
- Firm-level: CSMAR green-finance items; CNRDS ESG
- Macro: World Bank WDI environmental indicators

## Output template

```markdown
# 数据路径

项目题目：{{TOPIC}}
对应课程：{{COURSE}}
研究问题：{{QUESTION}}

## 本阶段任务
记录数据库、字段、口径、检索过程和核验结果。

## AI辅助记录
- 使用时间：...
- 使用工具：...
- 使用提示词：prompts/data-path-comtrade.md（或 prompts/data-path-io-table.md）

### AI 建议的数据路径
**主数据源**：UN Comtrade Plus
- Reporter: 156 (China)
- Partner: 842 (USA)
- Trade Flow: Export (X)
- Commodity classification: HS 2017
- Cmd Code: 8542 等
- Year: 2018–2024
- 检索 URL: https://comtradeplus.un.org/TradeFlow?...

**辅助数据源**：WITS MFN tariff
- ...

### 核验清单（学生必须线下完成）
- [ ] HS 8542 是否覆盖目标产品（半导体 IC）
- [ ] 单位是否为美元名义值；是否需要平减
- [ ] Reporter 与 Partner 镜像是否一致
- [ ] 年度数据是否在 2024 年发布前可获取
- [ ] USTR 301 清单的 HS 映射版本

## 人工核验与修改
- 数据来源或课程材料核验：
- 教师要求对照：
- 人工修改说明：

## 本阶段产出
- 提交文件：01_data/data_plan.md
- 原始数据导出文件位置：evidence/data/
- 教师反馈：
```

## What you DO NOT do

- Do not paste real CSV data into the file. The data lives in `evidence/data/`.
- Do not invent HS codes. If unsure, list the chapter (2-digit) and ask the student to drill down.
- Do not skip the 核验清单 — it is the entire point of stage 01.
