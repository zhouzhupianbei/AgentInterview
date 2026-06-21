# 2026-06-22 维护日志

## 概述
- 仓库: AgentInterview
- 维护范围: `docs/06-资源汇总.md` 追加 6.17 增量章节
- 新增: 10 个 GitHub 项目 + 10 篇微信公众号文章

## 抓取策略

### GitHub 搜索
- 8 个关键词 query，覆盖 Agent Harness / Claude Code / MCP / RAG / LLM 微调 / 上下文工程等
- 返回 28 个去重候选，按相关性打分（Agent / RAG / MCP / harness / context engineering 关键词加权 + 30 天内 push 加分 + 异常 star 过滤）
- 精选 10 个，按主题分组写入

### 微信公众号搜索
- 7 个关键词: Agent开发 / RAG系统 / LLM微调 / Prompt工程 / 上下文工程 / Agent评估 / MCP
- 每个关键词 5 条，共 35 条
- 主题命中率过滤 + 12 字指纹去重 + 每分类 cap 3 篇
- 最终命中 10 篇（按主题分组）

## 关键发现 / 趋势

1. **Agent Harness 从概念走向工程化**: 两本 Harness Books + how-claude-code-works 一并出现
2. **MCP 协议正式进入主流视野**: GitHub + 微信双侧同步爆发讨论
3. **上下文工程进入组件化**: NeoLabHQ/context-engineering-kit 提供 hand-crafted Skills
4. **Agent 评估持续成为高频话题**: 微信侧 3 篇命中，与 6.16 观察一致

## 修改文件
- `docs/06-资源汇总.md`: 追加 6.17 节（约 65 行）
- `收集/2026-06-22_收集.md`: 原始抓取记录
- `memory/2026-06-22_maintenance.md`: 本维护日志

## Commit 信息（计划）
- 主体: `补充 6 月下旬 Agent Harness / MCP / 上下文工程组件化资源`
- 副文: 列出关键主题 + 项目数 + 文章数