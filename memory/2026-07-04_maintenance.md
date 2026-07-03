# 2026-07-04 维护日志

## 基本信息
- **仓库**: zhouzhupianbei/AgentInterview
- **维护类型**: cron 定时增量更新
- **章节编号**: 6.21
- **执行时间**: 2026-07-04 03:00 CST（cron 触发）

## 采集数据
- **GitHub 仓库**: 7 个（4 大主题分组）
- **微信公众号文章**: 13 篇（7 大主题分组）
- **去重率**: GitHub 候选 74 → 13 → 7 入选；微信抓取 35 篇 → 去重后 13 篇

## 主题分布
### GitHub 端
- Agent Harness / Claude Code 生态（3）— `tigicion/dao-code` + `cobusgreyling/loop-engineering` + `alibaba/open-code-review`
- MCP / Agent 工具协议（2）— `tadata-org/fastapi_mcp` + `microsoft/mcp-for-beginners`
- RAG / 检索增强（1）— `NVIDIA/ChatRTX`
- 上下文工程（1）— `sci-m-wang/OpenCE`

### 微信公众号端
- Agent 开发（1）
- RAG 系统（2）
- Agent 评估（3）
- MCP 协议（1）
- Claude Code（2，含 InfoQ 7 月热点 + 果壳技术分析）
- 上下文工程（1）
- Agent 面试（3，含「拷打系列」「HR 破防」「CTO 简历」视角）

## 关键发现
1. **Coding Agent 国产基模化**：`tigicion/dao-code` 是少有的明确基于 DeepSeek-V4 的终端 coding agent，与 `pro-workflow`（6.18）等 Claude Code 系列形成「不同基模」的对照候选
2. **Loop Engineering 被命名化**：`cobusgreyling/loop-engineering` 把多 agent 循环编排提炼为 Loop Engineering 模式，受 Anthropic 工程实践启发，Agent 工程师面试考点从「单 agent」扩展到「多 agent 循环」
3. **MCP 进入「零侵入 + 教学化」双轨**：`tadata-org/fastapi_mcp`（零侵入接入）+ `microsoft/mcp-for-beginners`（跨语言教学课程）同期出现
4. **微信侧数据恢复正常**：6.20 因搜狗会话级硬封全部 0 响应（trap #8b），本次 7 个关键词全部命中率 100%，共抓到 13 篇去重后新文章

## 文档变更
- `docs/06-资源汇总.md` 新增 6.21 章节，约 66 行（位于 6.20 备注之后、`## 📚 核心资源汇总` 之前）
- 沿用 6.20 模板（markdown link + ⭐ + 主题分组 + 末尾备注 3 条）
- 章节命名延续 6.X 数字编号
- commit 风格：「补充 7 月初 Coding Agent 国产化与 MCP 教学化资源」

## 异常处理
- 微信侧恢复（无 hard block），不需要降级
- 高星候选 re-fetch 校验（trap #28）成功，`microsoft/mcp-for-beginners`（16.7k）等元数据准确
- `/tmp/` 临时文件留存（trap #23：某些 sandbox 拦截 `rm`/`find -delete`，按 trap #6e 直接放弃清理）

## 下次维护建议
- 关注 DeepSeek-V4 生态扩散：除 `tigicion/dao-code` 外，是否会出现其他基于国产基模的 coding agent（Qwen / 豆包 / 文心）
- Loop Engineering 模式如果获得主流厂商背书（如 Anthropic 官方文档明确推荐），可能成为新一波 harness 模板的母题
- 7 月中下旬关注 MCP 官方 registry（modelcontextprotocol/registry，6.20 已收录）的实际落地情况，是否出现更多 SDK / 教学资源