# 数据路径

项目题目：美国加征关税的宏观影响分析（电子部门）
对应课程：《贸易数据库与分析工具》
研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何

## 本阶段任务
记录数据库、字段、口径、检索过程和核验结果。

## AI辅助记录
- 使用时间：2026-05-27T15:38+08:00
- 使用工具：Claude Opus 4.7
- 使用提示词：prompts/data-path-comtrade.md + prompts/data-path-io-table.md

### AI 建议的数据路径

#### A. 主数据源：UN Comtrade Plus（年度、HS 2017）

| 字段 | 取值 |
|---|---|
| Reporter | `156` (China) |
| Partner | `842` (USA) |
| Trade Flow | `X` (Export) 与 `M` (Import) 镜像核验 |
| Classification | HS 2017 |
| Cmd Code | `8542`, `8517`, `8471`, `8473`, `8504`, `8528`；并提取整章 `84` 与 `85` 汇总 |
| Frequency | `A`（年度） |
| Period | `2017`–`2024` |
| Custom variables | `Trade Value (US$)`, `Netweight (kg)`, `Trade Quantity` |

检索 URL 示例（UN Comtrade Plus 公开数据）：
```
https://comtradeplus.un.org/TradeFlow
  ?Frequency=A
  &Classification=HS
  &CommodityCodes=8542,8517,8471
  &Reporter=156
  &Partner=842
  &Flow=X
  &Period=2017,2018,2019,2020,2021,2022,2023,2024
```

导出文件：`evidence/data/comtrade_chn_usa_electronics_2017-2024.csv`

#### B. 辅助数据源 1：WITS Tariff

- Source: World Bank WITS, https://wits.worldbank.org/
- Indicator: `MFN AHS Simple Average`, `Effectively Applied Tariff (AVE)`
- Reporter: USA (840)
- Partner: CHN (156)
- 年度 2017—2024
- Cmd Code: 6 位 HS（含 USTR 301 清单子集）
- 导出文件：`evidence/data/wits_usa_tariff_on_chn_2017-2024.csv`

#### C. 辅助数据源 2：USTR Section 301 列表与 HS 映射

- 来源：USTR 官网公开 List 1–4 PDF + 中科院 SE-Trade 整理的 HS 转换表（学生在 List 1–4 PDF 中独立核验）
- 关键日期：
  - List 1：2018-07-06 生效，500 亿美元
  - List 2：2018-08-23 生效，160 亿美元
  - List 3：2018-09-24 生效，2000 亿美元
  - List 4A：2019-09-01 生效；List 4B 推迟
- 导出文件：`evidence/data/ustr_301_lists_hs.csv`

#### D. 模型基年数据：GTAP database 11

- 由 GTAP Center (Purdue) 订阅；UIBE 国贸学院应有授权。
- 基年 2017，65 sectors × 141 regions。
- 学生需将 65 部门聚合为约 12 部门，区域聚合至 China / USA / EU27 / ROW（4 区域版常用于课程作业）。
- 聚合脚本：`02_model/aggregation.cmf`（在 stage 02 生成）
- 头文件不在本仓库；学生通过 GTAPAgg2 工具导出。

### 核验清单（学生必须线下完成）

- [ ] **HS 编码覆盖**：8542 (集成电路)、8517 (通信)、8471 (计算机) 是否覆盖学生关心的「电子部门」？是否需要加 8473 (零部件)、8504 (变压器)、8528 (显示器)？
- [ ] **单位一致**：UN Comtrade `Trade Value` 为美元名义值；用于 CGE 校准需平减到 2017 基价（用 US PPI 或 PCE deflator）。
- [ ] **镜像核验**：China-as-Reporter 与 USA-as-Reporter (Imports from China) 是否量级一致？差距 > 10% 须说明（一般 USA imports > China exports 由 CIF/FOB + 转口贸易导致）。
- [ ] **2024 年度发布**：UN Comtrade 2024 年度数据若于 2026 年仍不完整，须用 Comtrade Monthly 累计或回退到 2023。
- [ ] **USTR 清单映射版本**：USTR 原文用 HTSUS 10 位，学生在 List 1–4 中独立核验如何聚合到 HS6。
- [ ] **GTAP Electronics 部门口径**：GTAP 11 的 `ele` 部门合并了 HS 84 部分子章节与 85 全章；学生在 GTAP 11 sectoral concordance 中核验。
- [ ] **基年汇率**：GTAP 校准用 2017 美元；学生统一用 IMF IFS 2017 平均汇率。

## 人工核验与修改
- 数据来源或课程材料核验：（待学生填 —— 须截图 UN Comtrade 检索页与 WITS 关税页存入 `evidence/data/screenshots/`）
- 教师要求对照：（待补 —— 教师指定的部门聚合若为 4 部门（农业 / 制造 / 服务 / 其他）须修改聚合 .cmf）
- 人工修改说明：（待学生填）

## 本阶段产出
- 提交文件：01_data/data_plan.md
- 原始数据导出文件位置：`evidence/data/`
  - `comtrade_chn_usa_electronics_2017-2024.csv`
  - `wits_usa_tariff_on_chn_2017-2024.csv`
  - `ustr_301_lists_hs.csv`
  - `screenshots/comtrade_query.png`
  - `screenshots/wits_tariff_query.png`
- 教师反馈：（待教师填）
