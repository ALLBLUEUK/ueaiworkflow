# 模型与工具

项目题目：美国加征关税的宏观影响分析（电子部门）
对应课程：《贸易数据库与分析工具》
研究问题：2018 年以来美国对华加征关税对中国电子部门出口与宏观福利的影响如何

## 本阶段任务
记录工具命令、模型设定、报错处理和输出解释。

## AI辅助记录
- 使用时间：2026-05-27T15:46+08:00
- 使用工具：Claude Opus 4.7
- 使用提示词：prompts/model-gtap-gempack.md

### 工具与版本

- GTAP Standard model（GEMPACK 12.0 编译的 `gtap.tab`）
- GTAP database 11，基年 2017，聚合为 12 部门 × 4 区域
- GTAPAgg2（用于部门 / 区域聚合）
- GEMPACK 12.0（`tablo.exe`, `gemsim.exe`, `runGTAP.exe`）
- ViewSOL / ViewHAR（结果查看）
- LaTeX (TeX Live 2023, `booktabs`, `estout`)

### 输入文件

```
02_model/
├── aggregation.cmf          ← 65→12 部门、141→4 区域聚合命令
├── tariff_shock_25pp.cmf    ← 主冲击命令文件
├── tariff_shock_10pp.cmf    ← 稳健性：温和冲击
├── runGTAP.bat              ← 批处理运行脚本
└── README.md                ← 本笔记
```

依赖（不在 git，学生本地）：

```
evidence/model/base/
├── rwsbase.har              ← GTAP 11 base 数据（聚合后）
├── rwspara.har              ← 弹性参数
└── gtap.tab                 ← 标准 GTAP 模型 .tab
```

### 核心命令

**聚合（先跑一次）：**

```cmf
! 02_model/aggregation.cmf
! 把 GTAP 11 base 从 65×141 聚合到 12×4
File (new) base12x4.har ;
File (new) para12x4.har ;
SET REG # 4 regions # (CHN, USA, EU27, ROW) ;
SET COMM # 12 sectors # (AGR, OIL, FBT, TEX, CHM, MET, ELE, OTH_MFG, UTL, TRD, TRN, SVC) ;
! ... GTAPAgg2 自动生成 mapping 表 ...
```

**主冲击：**

```cmf
! 02_model/tariff_shock_25pp.cmf — US 对 China Electronics 加征 25 个百分点关税
File (new) tariff25pp.sl4 ;
File (new) tariff25pp.har ;
File rwsbase = evidence\model\base\base12x4.har ;
File rwspara = evidence\model\base\para12x4.har ;
File gtapsets = evidence\model\base\sets12x4.har ;
Verbal Description = "US +25pp tariff on imports of ELE from China, 2017 base, 12x4 agg" ;
Auxiliary files = tariff25pp ;
Method = Gragg ;
Steps = 3 6 9 ;
Subintervals = 3 ;
Automatic accuracy = yes ;
accuracy detail = 6 ;

! 关税以 power form 给出：tms = 1 + Δτ
! 25pp 增量等价于 tms 提升 25%（在 ad valorem 等价意义上）
Shock tms("ELE", "CHN", "USA") = 25 ;
```

**运行：**

```bat
:: 02_model/runGTAP.bat
@echo off
cd /d %~dp0
set GTAP=C:\GEMPACK12\GTAP\v11

runGTAP.exe tariff_shock_25pp.cmf > tariff25pp.log 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo GTAP run failed. See tariff25pp.log
    pause
    exit /b %ERRORLEVEL%
)

runGTAP.exe tariff_shock_10pp.cmf > tariff10pp.log 2>&1
echo Done. Outputs in tariff25pp.{sl4,har} and tariff10pp.{sl4,har}
```

**PowerShell 等价：**

```powershell
cd D:\courses\trade-db\examples\tariff-impact\02_model
.\runGTAP.bat
```

### 预期输出

| 文件 | 含义 | 关注字段 |
|------|------|----------|
| `tariff25pp.sl4` | 求解文件（百分比变化） | 用 ViewSOL 打开 |
| `tariff25pp.har` | 更新后的头文件 | `qgdp`, `EV`, `qxw`, `pxw`, `tot`, `qpd` |
| `tariff25pp.log` | GEMPACK 运行日志 | 检查 `Newton converged` |

关注的求解结果（学生在 ViewSOL 中导出到 CSV）：

```
qgdp(CHN, USA, EU27, ROW)          ← 实际 GDP 变化（%）
EV(CHN, USA, EU27, ROW)            ← 等价变差（百万美元）
qxw("ELE", CHN→USA)                ← 中国 ELE 部门对美出口数量
qxw("ELE", CHN→ALL)                ← 中国 ELE 部门总出口
按 12 部门看 qgdp 与 qxw 的部门分解
```

### 常见报错与对策

1. **`*** Could not open file rwsbase.har`**
   - 原因：`.cmf` 中相对路径解析失败
   - 修复：在 `.cmf` 中改为绝对路径 `File rwsbase = D:\courses\...\base12x4.har ;`

2. **`*** Newton convergence failed at step N`**
   - 原因：25pp 冲击较大，单步线性化误差累积
   - 修复：`Steps = 3 6 9 12` 增加细分，或 `Subintervals = 5`
   - 备选：先跑 `tariff_shock_10pp.cmf` 验证设置正确，再上 25pp

3. **`*** Model is not square`**
   - 原因：`.tab` 中 Variable / Equation 数量不配
   - 修复：检查是否误改了 `gtap.tab`；恢复标准版

4. **`*** Singular matrix at row XXX`**
   - 原因：聚合后某部门份额为 0
   - 修复：调整聚合方案，或在 GTAPAgg2 中合并空部门

### 模型假设

1. **完全竞争 + Armington**：进口品按来源国差异化；Armington 弹性使用 GTAP 11 默认值。
2. **关税收入归代表性家庭**：所有关税收入返还给进口国（美国）的代表性家庭，进入其消费。
3. **要素 closure**：劳动与资本部门间完全移动；劳动总量外生固定（标准短期 closure）。
4. **储蓄–投资**：全球资本市场出清；区域投资按 RoRC 分配。
5. **基年校准误差**：2017 年关税基础数据来自 GTAP 11，与 USTR 实际清单的覆盖率可能不完全一致（核验项见 stage 01）。

### 备选方法：行业 DID（如果学生无 GEMPACK 访问）

```stata
* 02_model/did_section301.do — 用 UN Comtrade HS6 面板做事件研究
use evidence/data/comtrade_chn_usa_hs6_panel.dta, clear

xtset hs6_id year
gen post = year >= 2018
merge m:1 hs6 using evidence/data/ustr_301_lists_hs.dta, ///
    keepusing(on_list1 on_list2 on_list3 on_list4a) nogen
gen treat = (on_list1 + on_list2 + on_list3 + on_list4a) > 0

reghdfe ln_trade_value treat##post, ///
    absorb(hs6_id year) cluster(hs6_id)
esttab using ../03_results/tab1_did.tex, ///
    replace booktabs se star(* 0.10 ** 0.05 *** 0.01)

* 事件研究
gen relyear = year - 2018
forvalues k = -3/5 {
    local kk = `k' + 100
    gen evt`kk' = treat * (relyear == `k')
}
reghdfe ln_trade_value evt97 evt98 evt99 evt101-evt105, ///
    absorb(hs6_id year) cluster(hs6_id)
coefplot, vertical drop(_cons) yline(0) xline(4)
graph export ../03_results/fig2_event_study.png, replace
```

## 人工核验与修改
- 数据来源或课程材料核验：（待学生填 —— 学生须在本地跑通 `runGTAP.bat` 并把 `.sl4`/`.har`/`.log` 放入 `evidence/model/`）
- 教师要求对照：（待补 —— 教师指定的 closure 若为长期，须调整资本与劳动的可移动性）
- 人工修改说明：（待学生填）

## 本阶段产出
- 提交文件：02_model/model_notes.md
- 运行截图 / 日志位置：
  - `evidence/model/tariff25pp.sl4`
  - `evidence/model/tariff25pp.har`
  - `evidence/model/tariff25pp.log`
  - `evidence/model/screenshots/viewsol_qgdp.png`
- 教师反馈：（待教师填）
