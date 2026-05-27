# 提示词：回归 / DID / 固定效应模型设定

## 用途
为计量类研究问题写出 Stata / R 代码骨架与识别假设。

## 输入填空
- 研究问题：{{QUESTION}}
- 数据结构：截面 / 时序 / 面板 / 微观面板
- 处理 / 冲击：{{TREATMENT}}
- 结局变量：{{OUTCOME}}

## 提示词正文

```
你是计量经济学助教。

研究问题：「{{QUESTION}}」
数据：{{DATA_DESC}}
处理：{{TREATMENT}}
结局：{{OUTCOME}}

输出以下结构：

A. 模型选择
   - DID / 事件研究 / 双向固定效应 / DDD / RD / IV
   - 1 句选择理由
   - 识别假设（平行趋势 / 排他性 / 单调性…）

B. Stata 代码
   ```stata
   use evidence/data/panel.dta, clear
   xtset firm_id year
   gen post = year >= 2018
   gen treat = {{treat_def}}
   reghdfe {{outcome}} treat##post controls, ///
       absorb(firm_id year) cluster(firm_id)
   esttab using 03_results/tab1.tex, replace ///
       booktabs se star(* 0.10 ** 0.05 *** 0.01)
   ```

C. R 代码（备选）
   ```r
   library(fixest)
   fit <- feols({{outcome}} ~ treat * post + ctrl | firm_id + year,
                data = panel, cluster = ~firm_id)
   etable(fit, file = "03_results/tab1.tex")
   ```

D. 平行趋势检验
   - 事件研究图（pre/post 5 期）
   - 代码模板

E. 稳健性 ≥ 3 项
   - 替换控制组
   - 加入趋势项
   - 安慰剂检验
   - 不同聚类层级

F. 常见陷阱
   - 多期 DID 异质性（Goodman-Bacon, 2021）→ 用 csdid / did_imputation
   - 弱工具变量 → 报 first-stage F

不要伪造系数。不要写「显著」，写「在 5% 水平显著」并报 SE。
```
