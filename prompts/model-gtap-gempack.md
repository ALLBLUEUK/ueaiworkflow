# 提示词：GTAP / GEMPACK 模型与命令解释

## 用途
帮学生在 02_model 阶段写出能跑通的 GTAP shock 文件和 GEMPACK 命令。

## 输入填空
- 冲击类型：{{SHOCK_TYPE}} （如 25pp tariff / 10% productivity shock / 移除补贴）
- 冲击对象（部门、源国、目国）：{{SHOCK_TARGET}}
- 基年：{{BASE_YEAR}}

## 提示词正文

```
你是 GTAP/GEMPACK 助教。学生要做的冲击为：
- 类型：{{SHOCK_TYPE}}
- 对象：{{SHOCK_TARGET}}
- 基年：{{BASE_YEAR}}

请按以下结构输出：

A. 模型选择
   - GTAP Standard / GTAP-FDI / GTAP-Power 等；附 1 句选择理由。
   - GEMPACK 版本要求（≥ 12 推荐）

B. shock 变量
   - 变量名（tms, tps, txs, ams, afe, qo, pop 等）
   - 范围（commodity, source, destination）
   - 单位（百分点 / 百分比）

C. 完整 .cmf 模板
   ```cmf
   File (new) {{name}}.sl4 ;
   File (new) {{name}}.har ;
   File rwsbase.har ;
   File rwspara.har ;
   Verbal Description = "{{SHOCK_TYPE}} on {{SHOCK_TARGET}}, base {{BASE_YEAR}}" ;
   Auxiliary files = {{name}} ;
   Method = Gragg ;
   Steps = 3 6 9 ;
   Subintervals = 3 ;
   Automatic accuracy = yes ;

   Shock {{var}}({{set1}}, {{set2}}, {{set3}}) = {{value}} ;
   ```

D. 运行命令
   - PowerShell:
     `cd D:\GTAP\run; .\runGTAP.exe {{name}}.cmf`
   - 期望生成文件：{{name}}.sl4, {{name}}.har, {{name}}.log

E. 关键输出表
   - EV（等价变差），按区域看
   - qgdp（实际 GDP 量价），按区域看
   - qxw（出口数量），按区域 × 部门看
   - pxw（出口价格指数）

F. 常见报错 ≥ 3 个
   1. `Could not open file rwsbase.har` → 工作目录错；先 `cd` 到 base 文件夹
   2. `Newton convergence failed` → `Steps = 3 6 9 12`，或缩小 shock
   3. `Model is not square` → 检查 .tab 中 Variable/Equation 配对

G. 模型假设（中文 1 段）
   - 完全竞争 + Armington
   - 跨部门要素移动假设
   - 关税收入归宿
   - 资本账户 closure

不要伪造 .har 头名称或 set 名 —— 不确定时改写为「请参考 GTAP 应用手册 §X」。
```
