---
name: ueai-model-explain
description: Explain econ models/tools — GTAP, GEMPACK, regression (Stata/R), DID, IO — at undergrad level. Names actual command syntax, file paths, error messages. Triggers at stage 02 or /ueai-stage 02.
---

# Model & tools (stage 02)

## Tools you may explain

| Tool | Typical artefact | Where errors live |
|---|---|---|
| GEMPACK (`tablo.exe`, `gemsim.exe`, `runGTAP.exe`) | `.tab` (model), `.cmf` (command), `.sl4` (solution), `.har` (header array) | `.log` and console |
| GTAP database 11 | base data .har, parameters .prm | `runGTAP` window |
| Stata | `.do`, `.dta`, `.smcl` log | `_rc` return code |
| R / RStudio | `.R`, `.Rmd`, `.RData` | console traceback |
| Python (pandas, statsmodels, linearmodels) | `.py`, `.ipynb` | traceback |
| LaTeX (TeX Live, `tabular`, `booktabs`, `estout`) | `.tex` → `.pdf` | `.log` |
| Excel + Power Query | `.xlsx` | (light) |

## What you produce

A filled `02_model/model_notes.md` with:

1. **工具与版本** — name and version (e.g. `GEMPACK 12.0`, `Stata 18 SE`).
2. **输入文件** — list every input artefact with relative path inside the project.
3. **核心命令** — exact command lines or .do/.R snippets the student will run.
4. **预期输出** — what files appear, what columns/coefficients to expect.
5. **常见报错** — at least 3 likely errors with diagnosis.
6. **模型假设** — for econometric models, the identifying assumption stated in plain Chinese.

## Concrete patterns

### GTAP shock setup (most common stage-02 case)

```
! tariff-shock.cmf — increase US tariff on imports of HS chapter 85 from China by 25 pp
File (new) tariffshock.sl4 ;
File (new) tariffshock.har ;
File rwsbase.har ;
File rwspara.har ;
Verbal Description = "US 25pp tariff on imports of electronics from China, 2017 base" ;
Auxiliary files = tariffshock ;
Method = Gragg ;
Steps = 3 6 9 ;
subintervals = 3 ;
automatic accuracy = yes ;
Shock tms("Electronics", "China", "USA") = 25 ;
```

Common errors:
- `*** Could not open file XXX.har` → check `cd` was set to the model folder.
- `*** Model is not square` → forgot to close a `Variable` or `Equation` block in the `.tab`.
- `*** Newton convergence failed` → reduce shock size or increase subintervals.

### Stata regression (DID)

```
* did-tariff.do
use evidence/data/firm_panel.dta, clear
xtset firm_id year
gen post = year >= 2018
gen treat = exposed_to_301 == 1
reghdfe lnvalue treat##post, absorb(firm_id year) cluster(firm_id)
esttab using 03_results/tab1_did.tex, replace booktabs se star(* 0.10 ** 0.05 *** 0.01)
```

### IO / completion coefficient calc

Use Leontief inverse $(I-A)^{-1}$. In Stata: `mata: L = luinv(I-A)`. In Python:
```python
import numpy as np
L = np.linalg.inv(np.eye(n) - A)
```

## Output template

```markdown
# 模型与工具

项目题目：{{TOPIC}}
对应课程：{{COURSE}}
研究问题：{{QUESTION}}

## 本阶段任务
记录工具命令、模型设定、报错处理和输出解释。

## AI辅助记录
- 使用时间：...
- 使用工具：...
- 使用提示词：prompts/model-gtap-gempack.md（或 model-regression.md）

### 工具与版本
- GEMPACK 12.0 / GTAP database 11
- TeX Live 2023, latexmk

### 输入文件
- 02_model/tariff-shock.cmf
- 02_model/runGTAP.bat
- evidence/data/comtrade_ch_us_2018-2024.csv

### 核心命令
```cmf
! tariff-shock.cmf
File (new) tariffshock.sl4 ;
...
Shock tms("Electronics", "China", "USA") = 25 ;
```

### 预期输出
- `tariffshock.sl4` — solution
- `tariffshock.har` — updated headers; relevant headers: `qgdp`, `qxw`, `EV`
- 关注 China 的 EV、qgdp、qxw（出口数量），按部门看 Electronics、Steel

### 常见报错
1. `Could not open file rwsbase.har` → 检查工作目录；`cd D:\GTAP\base` 后再运行。
2. `Newton convergence failed` → `Steps = 3 6 9 12` 增加细分步数。
3. ...

### 模型假设
- 完全竞争 + Armington 弹性
- 全局 Walras 平衡
- 关税收入回到代表性家庭

## 人工核验与修改
- 数据来源或课程材料核验：
- 教师要求对照：
- 人工修改说明：

## 本阶段产出
- 提交文件：02_model/model_notes.md
- 运行截图/日志位置：evidence/model/
```

## What you DO NOT do

- Do not invent coefficients or numbers — those come from stage 03 after the model actually runs.
- Do not write a multi-equation derivation unless explicitly asked.
- If the student lacks GEMPACK access, suggest the GTAP-in-Excel or a partial-equilibrium fallback (SMART, WITS).
