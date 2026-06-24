# 2026-06-25 维护日志

## 基本信息
- **仓库**: zhouzhupianbei/AgentInterview
- **维护类型**: cron 定时增量更新
- **章节编号**: 6.18
- **执行时间**: 2026-06-25 03:00 CST（cron 触发）

## 采集数据
- **GitHub 仓库**: 11 个（6 大主题分组）
- **微信公众号文章**: 9 篇（4 大主题分组）
- **去重率**: 候选 72 → 71 唯一 → 32 已存在链接去重 → 11 入选

## 主题分布
### GitHub 端
- Agent Harness / Claude Code 生态（4）
- Agent 框架 / 多智能体（1）
- LLM 微调 / 模型训练（2）
- RAG / 检索增强（2）
- Agent 评估 / 可观测性（1）
- MCP / Agent 工具协议（1）

### 微信公众号端
- Agent 开发（3）
- MCP / Agent 工具（3）
- Agent 评估（2）
- RAG 系统（1）

## 关键发现
1. **Harness 工具化加速**：`get-shit-done` 64k+ stars + `pro-workflow` + `agentic-harness-patterns-skill` + `ai-coding-project-boilerplate` 一并出现，标志 harness 从「概念」走向「可即用包」
2. **Java Agent 框架补位**：`opensolon/solon-ai` 是当前罕见的生产级 Java Agent 框架，对 Java 栈候选人加分项明确
3. **微调可行性预检**：`can-i-finetune-this` 解决了「我能不能微调」的工程问题，与 `LLM-Finetuning` peft 教程形成上下游
4. **Agent 评估平台化**：`future-agi/future-agi`（Apache 2.0）一次性提供 6 大能力，与微信端「Agent 评估 4 条小技巧」形成对照

## 文档变更
- `docs/06-资源汇总.md` 新增 6.18 章节，220 行
- 沿用 6.17 模板（markdown link + ⭐ + emoji）
- 章节命名延续 6.X 数字编号（与 AgentInterview 历史风格一致，与 GEO-Resources 的日期命名不同）
- commit 风格：「补充 6 月下旬 Harness 工具化与 Java Agent 生态资源」

## 异常处理
- 无

## 下次维护建议
- 关注 Harness Skills 的「npx skills add」安装方式是否有新平台扩展（如 Gemini CLI / Codex CLI）
- Java Agent 框架生态可能在 6-7 月迎来更多候选，关注 SolonAI 的 star 增长
- Agent 评估赛道从「文章」走向「平台」（future-agi 模式），后续可能涌现更多类似项目
