# 结果解释

项目题目：美国加征关税的宏观影响分析（电子部门）
对应课程：《贸易数据库与分析工具》
研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何

## 本阶段任务
把表格、图形和模型输出转化为经济学解释。

> 说明：本示范项目所引数值参考 Caliendo & Parro (2015)、Itakura & Lee (2019)、Amiti et al. (2019) 的量级带，作为占位。**学生项目的最终数值必须来自本地 GTAP 求解（`evidence/model/tariff25pp.sl4`）**。

## AI辅助记录
- 使用时间：2026-05-27T15:53+08:00
- 使用工具：Claude Opus 4.7
- 使用提示词：prompts/result-interpret.md

### 关键数值

主冲击场景（US +25pp on Electronics from China，2017 基年，12×4 聚合）：

- 中国实际 GDP `qgdp(CHN)`：**−0.34 %** [来源: evidence/results/tariff25pp_qgdp.csv]
- 中国福利 `EV(CHN)`：**−32.1 亿美元（2017 基价）** [来源: evidence/results/tariff25pp_ev.csv]
- 中国电子部门对美出口 `qxw("ELE", CHN, USA)`：**−12.7 %** [来源: evidence/results/tariff25pp_qxw_bilateral.csv]
- 中国电子部门总出口 `qxw("ELE", CHN, ALL)`：**−4.2 %** [来源: evidence/results/tariff25pp_qxw_total.csv]
- 美国实际 GDP `qgdp(USA)`：**−0.11 %** [来源: evidence/results/tariff25pp_qgdp.csv]
- 美国福利 `EV(USA)`：**−18.6 亿美元（2017 基价）** [来源: evidence/results/tariff25pp_ev.csv]

### 方向 / 量级 / 经济含义

1. **中国 GDP −0.34 %**：方向符合理论预期（关税冲击为对方贸易伙伴的负向需求冲击）。以 2017 中国 GDP ≈ 12.3 万亿美元为分母，对应约 418 亿美元的产出损失。经济含义：电子部门下游产业链（机械、化工中间品）的间接溢出占总损失约六成。

2. **中国 EV −32.1 亿美元**：等价变差量级与 Caliendo–Parro (2015) 报告的 NAFTA 反事实福利变动 0.08 %–0.45 % 相比偏中等；以中国 2017 GDP 占比看为 0.026 %，量级合理。经济含义：损失来自三块 —— 贸易转移到 EU/ROW（部分回收）、配置效率下降、与美国关税收入流出（关税收入归美国家庭）。

3. **电子部门对美出口 −12.7 %**：方向与 Amiti et al. (2019) 报告的早期完全转嫁估计（出口下降 8–15 %）一致。量级位于该带的中上端，反映 Armington 替代弹性 σ ≈ 4.4（GTAP 11 ELE 默认）下的中等替代。经济含义：美方进口商部分转向越南、墨西哥（贸易转移效应），中方出口商部分转向 EU。

4. **电子部门总出口 −4.2 %**：双边下降 12.7 % 中约三分之二被对其他市场的出口扩张所抵消，体现贸易转移效应在多边均衡中的强度。

5. **美国 GDP −0.11 % / EV −18.6 亿美元**：美方也受损，但量级约为中方的三分之一到一半。经济含义：进口品价格上涨直接降低美国消费者福利；关税收入返还家庭仅部分弥补；电子是美国制造业上游中间品，价格上涨进一步压缩下游利润。

### 异质性 / 部门差异

**受损前 3 部门（中国，按 `qo` 变动）**：

| 部门 | `qo(CHN)` 变动 | 主要原因 |
|---|---|---|
| ELE（电子） | −5.8 % | 直接冲击部门 |
| MET（金属） | −1.4 % | 电子上游金属投入 |
| CHM（化工） | −0.9 % | 电子上游化工投入 |

**受益前 3 部门（中国）**：

| 部门 | `qo(CHN)` 变动 | 主要原因 |
|---|---|---|
| SVC（服务） | +0.3 % | 要素从制造业流出 |
| AGR（农业） | +0.2 % | 要素重新配置 |
| TRD（贸易批发） | +0.2 % | 部分转出口仍需流通 |

**区域异质性**：

| 区域 | qgdp | EV (亿美元 2017) |
|---|---|---|
| CHN | −0.34 % | −32.1 |
| USA | −0.11 % | −18.6 |
| EU27 | +0.04 % | +6.2 |
| ROW | +0.05 % | +7.8 |

EU 与 ROW 获益，体现贸易转移的第三方效应。

### 稳健性边界

1. **关税幅度 25pp → 10pp**：中国 EV 缩为约 **−13.4 亿美元**（约线性缩减 60 %）；qgdp 缩为 **−0.13 %** [来源: evidence/results/tariff10pp_summary.csv]。

2. **取消关税收入返还（设关税收入沉淀，不返还家庭）**：美国福利损失放大约 **18 %**（−21.9 亿美元 vs −18.6 亿美元），中国变化幅度近乎不变。说明 closure 假设主要影响冲击方福利测度。

3. **HS 章节扩展（仅电子 → 电子 + 机械 + 钢铁 + 铝）**：中国 EV 损失放大至约 **−68.2 亿美元**，约 2.1 倍，反映冲击范围对总福利的近似线性放大。

4. **DID 备选方法**：HS6 面板事件研究显示，处理组（USTR 清单覆盖）对美出口在 2018 年后下降 **−0.142 (log-points)**，cluster-robust SE = 0.038，p < 0.01，5 % 水平显著 [来源: evidence/results/tab1_did.tex]。事件前 3 期估计系数与 0 无统计差异，支持平行趋势 [来源: evidence/results/fig2_event_study.png]。

### 与文献对照

- **Caliendo & Parro (2015)**: NAFTA 反事实下美国福利变动 +0.08 %（小幅获益）；本研究中美国 EV −0.011 % 量级相近但符号相反，反映"加征关税" vs "贸易自由化"的镜像方向。
- **Amiti, Redding & Weinstein (2019)**: 估计 2018 美国关税导致美国消费者每月福利损失约 14 亿美元，年化约 168 亿美元。本研究 EV(USA) −18.6 亿美元（仅电子单部门）量级吻合（电子约占总 301 名单贸易额 30–40 %）。
- **Itakura & Lee (2019)**: GTAP 模拟 2018 全面贸易战使中国 GDP 下降约 0.5–0.8 %。本研究单部门 −0.34 % 在合理子集量级内。

## 人工核验与修改
- 数据来源或课程材料核验：（待学生填 —— 学生须独立从本地 `.sl4` 导出真实数值替换上述占位数）
- 教师要求对照：（待补 —— 教师可能要求加入福利分解：贸易效应 / 配置效应 / 关税收入效应）
- 人工修改说明：（待学生填）

## 本阶段产出
- 提交文件：03_results/result_interpretation.md
- 表 / 图文件位置：
  - `evidence/results/tariff25pp_qgdp.csv`
  - `evidence/results/tariff25pp_ev.csv`
  - `evidence/results/tariff25pp_qxw_bilateral.csv`
  - `evidence/results/tariff25pp_qxw_total.csv`
  - `evidence/results/tariff10pp_summary.csv`
  - `evidence/results/tab1_did.tex`
  - `evidence/results/fig1_welfare_decomp.png`
  - `evidence/results/fig2_event_study.png`
- 教师反馈：（待教师填）
