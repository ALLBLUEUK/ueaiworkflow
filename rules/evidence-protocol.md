# Rule: 证据归档协议

## 目录约定

每个 ueai 项目根目录下：

```
<slug>/
├── 00_problem/ … 05_feedback/        ← AI + 学生协同填写
├── evidence/
│   ├── data/                          ← 原始数据导出（.csv, .xlsx, .dta）
│   ├── model/                          ← 模型输入输出（.cmf, .sl4, .har, .do, .log）
│   ├── results/                        ← 加工后结果（.csv, .png, .tex 表）
│   ├── paper/                          ← 最终交付（.pdf, .docx, .zip 源码）
│   └── evidence_checklist.md           ← 自动生成的归档清单
└── prompt_templates.md                 ← 本项目使用的提示词副本
```

## 文件命名

- 数据：`<source>_<key>_<years>.<ext>`（例：`comtrade_chn_usa_2018-2024.csv`）
- 模型：`<scenario>_<model>.<ext>`（例：`tariff25pp_gtap.cmf`）
- 结果：`<scenario>_<metric>.<ext>`（例：`tariff25pp_ev_by_region.csv`）

## 必备项（最少 5/7）

参见 `templates/evidence_checklist.md`。

## 不可篡改原则

- evidence/ 下的原始文件不可被 AI 写入或修改。
- AI 仅向 `evidence/evidence_checklist.md` 写入勾选状态。
- 模型输出（.sl4, .har）应保留至少一次完整 log。

## 课程归档

学期末教师把每位学生 / 小组的整个 `<slug>/` 文件夹打包，命名 `<学号>_<slug>_<日期>.zip`，存入课程归档库。

## 项目结项归档

项目负责人将示范项目（`examples/tariff-impact/`）连同本仓库一并提交结项材料。
