# 论文与报告大纲

项目题目：美国加征关税的宏观影响分析（电子部门）
对应课程：《贸易数据库与分析工具》
研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何

## 本阶段任务
组织摘要、引言、数据方法、结果、结论和参考文献。

## AI辅助记录
- 使用时间：2026-05-27T16:01+08:00
- 使用工具：Claude Opus 4.7
- 使用提示词：prompts/paper-structure.md

---

## 摘要（中文，≤ 300 字）

[占位 — 由学生根据完成稿撰写。AI 仅在所有阶段定稿后辅助压缩。]
建议要点：研究问题一句话；方法（GTAP 11 + DID 备选）一句话；最重要的三个数字（中国 GDP、EV、电子部门出口）；一句政策含义。

## 摘要（英文，≤ 200 words）

[Same — student to draft.]

## 关键词

中国对美贸易；Section 301；GTAP；电子部门；福利分解

## 1 引言

- 1.1 研究背景
  - 中美贸易摩擦自 2018 年起的演进；Section 301 List 1–4 的时间线与覆盖额
  - 中国电子部门（HS 84–85）在对美出口中的份额（约 35–40%，需在 evidence/data/comtrade 中核验）
  - 既有研究多止于 2019 数据；2020 后疫情扰动 + 供应链重组使更新成为必要

- 1.2 文献空白
  - 现有 GTAP 研究多用 2014 GTAP 10 base；本文用 GTAP 11 (2017 base) 重新校准
  - 现有 DID 研究多用 HS6 月度数据；本文同时报告 CGE 与 DID 两套结果对照
  - 现有研究对部门内异质性 (84 vs 85 vs 73 vs 76) 关注不足

- 1.3 研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何？

- 1.4 边际贡献（≤ 3 条）
  - 用 GTAP 11 与 2017 基年重新校准电子部门关税冲击
  - 同时报告 CGE 与 DID 两类方法估计的弹性，并讨论一致性
  - 给出部门内异质性（IC vs 通信设备 vs 计算机）分解

## 2 文献综述

- 2.1 贸易战福利效应
  - Amiti, Redding & Weinstein (2019) "The Impact of the 2018 Trade War on U.S. Prices and Welfare", JEP
  - Fajgelbaum, Goldberg, Kennedy, Khandelwal (2020) "The Return to Protectionism", QJE
  - Cavallo, Gopinath, Neiman, Tang (2021) "Tariff Pass-through at the Border and at the Store", AER:Insights

- 2.2 GTAP 应用
  - Caliendo & Parro (2015) "Estimates of the Trade and Welfare Effects of NAFTA", ReStud
  - Itakura & Lee (2019) "Welfare Changes and Sectoral Adjustments of Asia-Pacific Countries under Alternative Sequencings of Trade Liberalization", J. Asian Econ.
  - Hertel, Walmsley & Itakura (2001) "Dynamic effects of the 'new age' free trade agreement", J. Econ. Integ.

- 2.3 中国视角
  - 余淼杰 等 (2019) 关于中美贸易摩擦的多篇 WP / 期刊
  - 陈勇兵 等 (2020) 关于关税对中国企业出口的影响
  - [ref待补 —— 学生在 CNKI 中独立检索]

- gap 句：「现有研究对 (i) 2020 年后的更新冲击、(ii) 电子部门内子部门异质性、(iii) 关税收入归宿假设的敏感性，缺乏分解。」

## 3 数据与方法

### 3.1 数据来源
（引 01_data/data_plan.md）
- UN Comtrade Plus：China-USA 双向 HS6 年度贸易额，2017–2024
- WITS：美国对华 MFN + AVE 关税
- USTR Section 301 List 1–4 HS 清单
- GTAP database 11 (2017 base, 65×141)，聚合为 12×4

### 3.2 模型设定
（引 02_model/model_notes.md 关键公式）
- 反事实场景：US 对 China ELE 部门 `tms` 提升 25 个百分点
- GTAP Standard 模型，完全竞争 + Armington
- Closure：标准短期 closure；要素部门间完全移动；劳动总量外生
- 求解：Gragg method，Steps = 3 6 9，Subintervals = 3

### 3.3 识别 / 假设
（CGE 部分）
- 完全竞争且常替代弹性（CES）需求
- 关税收入归代表性家庭
- 全球资本市场出清，投资按 RoRC 分配

（DID 备选部分）
- 平行趋势：处理组与控制组在 2018 前的对数出口趋势一致（事件研究检验）
- USTR 清单分配近似外生（依据：清单主要由战略产业、贸易救济考量驱动，非企业绩效）

## 4 结果

（引 03_results/result_interpretation.md 的每一条；每个数字必须带 [来源: ...]）

### 4.1 总体福利
- 中国 GDP −0.34 % [来源: evidence/results/tariff25pp_qgdp.csv]
- 中国 EV −32.1 亿美元 [来源: evidence/results/tariff25pp_ev.csv]
- 美国 GDP −0.11 %；EV −18.6 亿美元 [来源: 同上]
- 中美双方均受损，EU/ROW 因贸易转移获益

### 4.2 部门差异
- 中国 ELE 部门产出 −5.8 %；MET −1.4 %；CHM −0.9 %
- 中国 ELE 对美出口 −12.7 %，对全球总出口 −4.2 %（贸易转移效应吸收 2/3）
- 详见 03_results §异质性表

### 4.3 稳健性
- 关税幅度从 25pp 改为 10pp：损失约线性缩减 60 %
- 关税收入不返还美国家庭：美国福利损失放大 18 %
- 章节扩展到 84+85+73+76：中国 EV 损失放大约 2.1 倍
- DID 备选估计 −0.142 (log-points)，p < 0.01，平行趋势检验通过

## 5 结论与政策含义

### 5.1 主要发现（≤ 3 条）
1. 25pp 电子关税使中国 GDP 下降约 0.3 %，福利损失 32 亿美元（2017 基价）
2. 部门内强烈异质性：双边出口下降 12.7 %，总出口仅下降 4.2 %，体现贸易转移
3. 关税收入归宿对美方福利测度影响显著（18 % 量级），CGE 结果应配合该假设说明

### 5.2 边界
- 本研究不能说明动态调整路径，仅给出比较静态结果
- 本研究不能说明企业层面退出 / 进入的非对称调整
- 本研究不能说明非关税壁垒（出口管制、实体清单）影响
- 基年 2017 早于 2018 关税生效，所有结果是「假定关税从未存在的反事实」量级

### 5.3 政策含义（≤ 3 条，每条附假设）
1. 中方贸易转移空间存在但有限（2/3 抵消，1/3 真实损失）；前提：EU/ROW 不同步加征
2. 美方福利损失的政治表达需将关税收入与价格上涨分账户呈现；前提：关税收入仍返还家庭
3. 部门内异质性（IC vs 计算机 vs 通信）意味着选择性回应可能更优；前提：执行成本可控

## 参考文献

[学生需在 CNKI / EconLit 中独立检索补足至 ≥ 12 条，外文 ≥ 5；以下为 AI 建议起点]

1. Amiti, M., Redding, S. J., & Weinstein, D. E. (2019). The impact of the 2018 trade war on U.S. prices and welfare. *Journal of Economic Perspectives*, 33(4), 187-210.
2. Caliendo, L., & Parro, F. (2015). Estimates of the trade and welfare effects of NAFTA. *Review of Economic Studies*, 82(1), 1-44.
3. Fajgelbaum, P. D., Goldberg, P. K., Kennedy, P. J., & Khandelwal, A. K. (2020). The return to protectionism. *Quarterly Journal of Economics*, 135(1), 1-55.
4. Itakura, K., & Lee, H. (2019). Welfare changes and sectoral adjustments of Asia-Pacific countries under alternative sequencings of trade liberalization. *Journal of Asian Economics*, 65, 101-132.
5. Hertel, T. W. (Ed.). (1997). *Global Trade Analysis: Modeling and Applications*. Cambridge University Press.
6. Cavallo, A., Gopinath, G., Neiman, B., & Tang, J. (2021). Tariff pass-through at the border and at the store. *American Economic Review: Insights*, 3(1), 19-34.
7. [ref待补 — 中文文献至少 4 条]

## 学术诚信声明

本研究的数据检索、模型设定、结果解释和论文写作过程中，使用了 AI 辅助工具 Claude Opus 4.7（通过 ueaiworkflow 工作流）。AI 在以下环节提供了帮助：
- **stage 00（问题拆解）**：将主题分解为研究对象、变量、数据、方法、展示
- **stage 01（数据路径）**：建议 UN Comtrade、WITS、USTR 清单的检索字段
- **stage 02（模型与工具）**：提供 GTAP `.cmf` 模板与 GEMPACK 命令解释
- **stage 03（结果解释）**：将模型输出翻译为方向 / 量级 / 经济含义
- **stage 04（论文与报告）**：检查五维度结构，提供大纲建议

AI 提示词模板、AI 反馈摘要与人工修改记录见 `05_feedback/ai_revision_log.md`。研究问题确立、数据核验（UN Comtrade 截图与导出）、模型本地求解（`.sl4` 文件）、结果数值判读和最终文本由作者本人负责。

所引用数据均来自公开数据库或合法订阅（UN Comtrade Plus, WITS, GTAP database 11），未经伪造或拼接。模型求解的 `.sl4` 与 `.har` 文件已归档至 `evidence/model/`。

## 人工核验与修改
- 数据来源或课程材料核验：（待学生填）
- 教师要求对照：（待补）
- 人工修改说明：（待学生填）

## 本阶段产出
- 提交文件：04_writing/paper_outline.md
- 终稿位置：`evidence/paper/final.pdf`（待学生生成）
- 教师反馈：（待教师填）
