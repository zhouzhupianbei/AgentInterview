# 2026-07-01 maintenance

## 本次维护摘要
- 仓库: zhouzhupianbei/AgentInterview
- 章节: 6.20 (2026-07-01 增量更新)
- GitHub 项目: 10 个 (7 MCP / Agent 工具协议 + 2 RAG + 1 Agent 评估)
- 微信公众号文章: 0 篇 (搜狗搜索会话级限流回退)

## 关键观察
1. MCP 进入「官方化 + 多语言 SDK」阶段: registry (6.9k) + go-sdk (Google 4.7k) + csharp-sdk (Microsoft 4.4k) 6 月底齐发
2. Microsoft 官方背书 MCP: microsoft/mcp (3.4k) 以 catalog 形式托管官方 server 实现
3. Agent 可观测性进入 20k+ 主流梯队: comet-ml/opik (20.1k) 显著高于 6.18 节的 Langfuse / LangSmith

## 流程
- 关键词: agent framework LLM, RAG retrieval, LLM fine-tuning LoRA, agent evaluation observability, AI engineering prompt, MCP model context protocol server
- 微信关键词: Agent开发, RAG系统, Agent评估, MCP协议, Claude Code, 上下文工程, Agent面试 (全部返回 items=[])
- 去重方法: 链接抽取 + 标题前 12 字符指纹
- 主题过滤: 期望主题词命中 ≥ 60%
- 评分: rel ≥ 3 入候选 (AgentInterview 主题宽阈值)
- 微信回退: 搜狗限流 7 个关键词 0 数据，按 trap #8 跳过微信侧增量

## 已知问题
- 搜狗微信搜索接口本会话完全不可用 (ok=True, items=0 持续 30 秒后仍 0)
- 下次维护建议: 改用 Web 搜索 (browser/web_search) 替代 jisu-wechat-article
