# ueaiworkflow

经管类本科建模与写作 **AI 智能体辅助工作流**。

面向经管类本科课程的教改实践成果。

面向 *Claude Code* / *Codex CLI* / *Cursor* / *GitHub Copilot Chat* / *Aider* 等 AI 编程与研究助手使用。

## 这个工作流的目的

本工作流的核心目的是 **辅助本科学生学习经济研究的全过程**——而不是替学生完成研究。

学生在《贸易数据库与分析工具》和《经济建模与写作》两门课程中，面对真实经贸问题（关税冲击、数字基础设施、绿色金融、全球价值链等）时，要走完一条从兴趣到论文的完整路径。这条路径上每个环节都对学生构成具体的学习障碍：

| 学生学习障碍 | 本工作流提供的学习辅助 |
|---|---|
| 不知道怎么把"我想研究关税战"收窄成一个可执行的研究问题 | AI 在 stage 00 给出"研究对象 / 核心变量 / 可用数据 / 可能方法 / 结果展示"五字段拆解 + 5 项要学生独立核验的口径 |
| 不知道 UN Comtrade 该勾选哪些字段、HS 编码取四位还是六位 | AI 在 stage 01 给出每个字段的取值（Reporter=156、Cmd Code=8542 等）+ 可点击的检索 URL + 字段含义解释 |
| 看不懂 `.cmf` 文件每一行什么意思、`Newton convergence failed` 是什么报错 | AI 在 stage 02 给出带中文注释的 `.cmf` 模板、运行命令、3+ 类常见报错的解释与修复 |
| ViewSOL 里看到 `qgdp = -0.34%`，不知道怎么解读 | AI 在 stage 03 演示如何把每个数值翻译成"方向 + 量级 + 经济含义"三件套，并与 Caliendo–Parro 等文献量级对比 |
| 写论文时缺乏结构感，研究问题、文献、数据、结果、结论之间脱节 | AI 在 stage 04 按五维度给出大纲 + 每条要点的引用要求 + 学术诚信声明骨架 |
| AI 用过了之后说不清自己用了哪些、改了哪些 | AI 在 stage 05 自动整理使用日志（阶段 / 模型 / 提示词 / 接受–修改–拒绝） |

学生自己的工作（提出问题、跑数据库、本机跑 GEMPACK / Stata、独立判断、写论文正文）始终是学生自己完成的；AI 提供的是\textbf{学习理解的脚手架}——每一步该看什么、想什么、做什么。

## 这个工作流不做什么

- **不替学生跑模型**。GTAP/GEMPACK、Stata、R 都在学生自己电脑上运行；工作流只解释命令、解释报错、解释输出。
- **不伪造数据 / 编码 / 系数 / 数值**。`rules/ai-use-boundary.md` 明确禁止 AI 在不确定时凑数字；所有数字必须带 `[来源: evidence/results/...]` 标记，指向学生自己导出的真实文件。
- **不替学生写论文正文**。AI 在 stage 04 的输出是大纲与逐条要点，不是成稿正文。
- **不允许学生越过人工核验段**。每个阶段文件都有 `## 人工核验与修改` 段，学生不填工作流的 `/ueai-validate` 命令报失败。

## 覆盖的课程

- 《贸易数据库与分析工具》（UN Comtrade、WITS、GTAP/GEMPACK、IO 表、批处理）
- 《经济建模与写作》（选题→文献→数据→模型→结果→LaTeX 论文）

工作流的六阶段结构同样可推广至计量经济学、国际贸易实务、产业经济学、数字经济专题等课程，只需替换 `prompts/` 与 `templates/` 中的具体数据库与模型部分。

## 30 秒上手

```powershell
# 1. 进入课程项目目录（任意位置）
PS> cd D:\courses\trade-db\2026-spring\student-007

# 2. 把工作流仓库克隆为 .ueai 子目录
PS> git clone https://github.com/ALLBLUEUK/ueaiworkflow.git .ueai

# 3. 启动 AI 助手（任选其一）
PS> claude       # Claude Code 自动读 .ueai/AGENTS.md
PS> codex        # Codex CLI 原生支持 AGENTS.md
# 或在 Cursor / GitHub Copilot Chat 中把 .ueai/AGENTS.md 加入上下文

# 4. 启动一个课程项目
> /ueai-new
> 课程：贸易数据库与分析工具
> 题目：美国加征关税的宏观影响分析
> 研究问题：……
> slug: tariff-impact

# 5. 按阶段推进（每阶段 AI 写学习辅助 + 学生做核验/操作）
> /ueai-stage 00       # 问题拆解学习
> /ueai-stage 01       # 数据路径学习
> /ueai-stage 02       # 模型工具学习
> /ueai-stage 03       # 结果解释学习
> /ueai-stage 04       # 论文结构学习
> /ueai-stage 05       # AI 使用日志
> /ueai-review         # 教师 / 同伴评阅
> /ueai-archive        # 归档清单
> /ueai-validate       # 提交前完整性检查
```

每个 `/ueai-stage` 命令结束 AI 都会暂停并明确告诉学生"请在 PowerShell 中跑 X"或"请在 UN Comtrade 截图 Y"——学生完成后回到会话再输入下一个命令。完整端到端记录见 [`docs/工作流说明书.pdf`](docs/工作流说明书.pdf) 第 5 节。

## 仓库结构

```
ueaiworkflow/
├── AGENTS.md                ← AI 智能体主入口（所有助手必读）
├── README.md                ← 本文件
├── LICENSE                  ← MIT
├── CITATION.cff
├── .claude/
│   ├── commands/            ← Claude Code slash 命令（ueai-new/stage/review/archive/validate）
│   └── skills/ueai-*/SKILL.md  ← 6 个技能（每阶段一个）
├── .claude-plugin/          ← Claude Code 插件元数据
├── .github/copilot-instructions.md
├── templates/               ← 6 阶段 .md 骨架 + 归档清单
├── prompts/                 ← 具体提示词模板（按数据库 / 模型类型分文件）
├── rules/                   ← AI 使用边界、证据协议、评分量规、学术诚信
├── examples/tariff-impact/  ← 端到端示范项目（含完整 6 阶段填写）
└── docs/
    ├── 工作流说明书.tex / .pdf  ← 操作使用手册（含真实输入输出）
    └── demo-transcript.md       ← 一次完整运行的交互记录
```

## 引用

```
ueaiworkflow [CP/OL]. 2026. https://github.com/ALLBLUEUK/ueaiworkflow
```

## 许可

MIT，见 `LICENSE`。
