# {{TOPIC}}

- **课程**：{{COURSE}}
- **研究问题**：{{QUESTION}}
- **slug**：{{SLUG}}
- **创建日期**：{{DATE}}
- **学生**：{{STUDENT}}

## 阶段链条

```
00_problem  →  01_data  →  02_model  →  03_results  →  04_writing  →  05_feedback
                                                              │
                                                              ↓
                                                         evidence/
```

## 如何推进

在已安装 `ueaiworkflow` 仓库（即看到本文件）的 AI 助手中，依次执行：

```
/ueai-stage 00     # 问题拆解
/ueai-stage 01     # 数据路径
/ueai-stage 02     # 模型与工具
/ueai-stage 03     # 结果解释
/ueai-stage 04     # 论文与报告
/ueai-stage 05     # AI 反馈与人工修改
/ueai-review       # 评阅模式
/ueai-archive      # 归档清单
/ueai-validate     # 完整性检查
```

每阶段 AI 会写入对应 `.md` 文件并暂停等你完成 `人工核验与修改`。
