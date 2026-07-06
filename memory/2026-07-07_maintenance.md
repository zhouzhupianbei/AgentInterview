# 2026-07-07 维护日志

## 基本信息
- **仓库**: zhouzhupianbei/AgentInterview
- **维护类型**: cron 定时增量更新
- **章节编号**: 6.22
- **执行时间**: 2026-07-07 03:00 CST（cron 触发）

## 采集数据
- **GitHub 仓库**: 10 个（5 大主题分组）
- **微信公众号文章**: 8 篇（4 大主题分组）
- **去重率**: GitHub 候选 50 → 与现有 415 比对 → 6 真新 → 28 个 `created:>2026-04-01` 互补 → 精选 10；微信抓取 35 篇 → 标题指纹去重 → 17 篇 → 2026-05 之后时效筛选 → 8 篇入选

## 主题分布
### GitHub 端
- MCP / Agent 工具协议（4）— `nduckmink/arkon` + `0xSteph/pentest-ai` + `anysearch-ai/anysearch-mcp-server` + `repoprompt/repoprompt-ce`
- RAG / 检索增强（2）— `nashsu/llm_wiki` + `Ar9av/obsidian-wiki`
- Agent 框架 / 多智能体（2）— `kellyvv/PhoneClaw` + `trypromptly/LLMStack`
- 上下文工程（1）— `open-gsd/gsd-pi`
- Agent Harness / Claude Code 生态（1）— `xbtlin/ai-berkshire`

### 微信公众号端
- Agent 评估（2）— 评估器占位符机制 / 全面评估 Agent 框架
- Claude Code（3）— 创建循环 / 大面积封号事件 / 核心工程师分享
- MCP 协议（1）— MCP 测试入门
- Agent 面试（2）— HR 破防 / AI 调用工具失败兜底

## 关键发现
1. **MCP 进入「行业垂直化」阶段**：本期 4 个 MCP 项目覆盖企业知识库（arkon）、安全测试（pentest-ai）、统一搜索（anysearch-mcp-server）、桌面编辑器（repoprompt-ce）四个垂直场景——MCP 不再是「Python SDK」那么简单，而是「行业接入协议层」
2. **Karpathy LLM Wiki 模式被工程化复现**：`nashsu/llm_wiki`（13.8k ⭐，跨平台桌面）+ `Ar9av/obsidian-wiki`（2.7k ⭐，Obsidian 集成）同期出现，意味着「AI 自动维护知识库」从概念验证走向产品化
3. **Claude Code 国内「极压环境」催生代理工具**：`fujibee/agmsg`（9 ⭐）+ 科技狐报道的大面积封号事件合力把「跨厂商 coding agent 编排」从高端需求变成企业刚需

## 文档变更
- `docs/06-资源汇总.md` 新增 6.22 章节，约 88 行（位于 6.21 备注之后、`## 📚 核心资源汇总` 之前）
- 沿用 trap #17 模板：markdown link + ⭐ + 主题分组 + 末尾备注 3 条
- 章节命名延续 6.X 数字编号（6.21 → 6.22）

## 异常处理
- **微信侧恢复正常**（trap #8b 消退）：7 个关键词全部命中率 100%，共抓到 35 篇去重后 17 篇，时效筛选后 8 篇
- **GitHub 候选大量重复**：现有 doc 已有 415 个 GitHub full_name，新抓取 50 候选只 6 个不在库内 → 用 `created:>2026-04-01` 时间窗查询互补得 28 个 → 精选 10 个
- **高质量候选验证**：trap #28 high-star re-fetch 通过，未发现 `full_name` 错位
- **`/tmp/` 临时文件**：按 trap #6e / #23 单次 cron 不清理

## 下次维护建议
- **关注 Karpathy LLM Wiki 生态扩散**：7 月中下旬可能有更多「AI 知识库自动化维护」项目出现，关注 `nashsu` 个人后续工作 + obsidian-wiki 是否被商业团队 fork
- **关注 MCP 垂直化进展**：是否能继续出现类似 `pentest-ai` 这种「行业 MCP server」，尤其是金融 / 医疗 / 法律三个传统行业的 MCP 化项目
- **关注 Coding Agent 国内版**：`xbtlin/ai-berkshire` 是首个明确的「价值投资方向 Coding Agent」，7 月底可能扩散到量化交易 / 投研 / 财报分析等领域
- **Claude Code 封号影响**：7 月科技狐报道的大面积封号事件后续发展，可能影响本期持续热度高的 Claude Code 关键词命中率，下次维护可关注（Agent 面试关键词里的相关信号）
