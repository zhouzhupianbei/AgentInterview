# 📅 维护记录 - 2026-08-10

> 本次维护聚焦 **MCP 1.0 修订落地 + Agent Harness 大众化 + AgentSkill 化与日更日报化**。

## 1. 采集概要

- **GitHub REST API 搜索**：8 个标准 query (`AI agent framework` / `MCP server` / `context engineering` / `Claude Code skill` / `agent memory` / `WebMCP` / `LLM eval harness` / `agent evaluation`) + 8 个时间窗互补 query (`agent harness production` / `AGENTS.md` / `agent trace` / `agent router` / `MCP inspector` / `tool use` / `structured output` / `sandbox code execution`)
- **estimate 候选数**：50+ 28 共 78 候选 → 与现有 225 个 full_name 去重 → 31 个新候选 → rel>=4 筛 29 个 → 精选 10 个
- **微信公众号抓取**：11 个关键词（`MCP协议`/`MCP 2026`/`Agent Harness`/`Claude Code Skill`/`上下文工程`/`Agent评估`/`Agent记忆`/`Agent 框架`/`AgentSkill`/`Agent Web`/`模型路由`）共 55 文章 → 三重指纹去重 → recency+quality 精选 9 篇

## 2. 关键新发现

### GitHub 精选（10 个）

| 仓库 | 主题 | 关键价值 |
|------|------|---------|
| nexu-io/html-anything | MCP / Frontend | 75 Skills × 9 Surfaces, agentic HTML editor |
| dondai1234/master-fetch | MCP | MCP server, Cloudflare bypass, Trafilatura extraction |
| JimLiu/baoyu-design | Claude Code Skill | Claude Design 本地化, Opus 4 优化 |
| zhnt/loushang | Agent Harness | AI-native harness, 多模型编排 + 工具治理 |
| riponcm/projectmem | Agent Memory | Local-first, MCP server for Claude Code/Cursor |
| ShenSeanChen/waku-agent | Agent Harness | 个人 AI agent, harness+loop+memory+eval |
| LanceZPF/agent-as-a-router | Agent Routing | Agent-as-a-Router 智能体路由 |
| op7418/guizang-social-card-skill | Claude Code Skill | 小红书图文 + 公众号封面 skill |
| UditAkhourii/adhd | Claude Code Skill | tree-of-thought 加剪枝 skill |
| vstorm-co/agentcanvas | Agent Tracing | Pydantic AI workflow 可视化 |

### 微信精选（9 篇）

- MCP 1.0 协议类 3 篇（7-30 / 8-04 / 8-06 三篇解读）
- AgentSkill / Harness 类 3 篇（含 1 篇 Skill 日报、1 篇 harness vs framework 本质区别）
- Agent 评估 / Agent 框架类 3 篇（含蚂蚁清华 AReaL + Agentium 实验室实战）

## 3. 趋势观察

1. **MCP 1.0 生态进入"工具全景"阶段** — 2026-07-28 官方无状态核心 + 能力发现 + JSON Schema 完整化后，公众号侧出现"MCP 生态全景""8 个必装工具"类整理文
2. **AgentSkill 化与日更日报化** — Skill 日报型内容 + 6173⭐ 卡片设计 skill + 3425⭐ tree-of-thought skill，说明 Skill 化已变成"垂直能力封装 + 跨工具复用"的新型生态
3. **Agent 评估从"感觉"走向"可量化"** — 蚂蚁清华 AReaL 开源 + Agentium 实验室实战 + agentcanvas 可视化，形成完整链路

## 4. 踩坑与决策

- **"MCP协议" 关键词触发搜狗硬封**：搜狗对 "MCP协议" 关键词的页面解析报错（conda python 与系统 python 都失败），改用 "Model Context Protocol" 完整短语绕过——下次维护优先用完整短语
- **trap #29 高去重率继续生效**：长期维护仓库 GitHub full_name 已 225 个，标准 query 候选池 50 个只剩 6 个真新项目，触发了时间窗互补 + 关键词扩展
- **trap #30 高 star 候选 re-fetch 失败**：本期 10 个精选只有 1 个（vstorm-co/agentcanvas）成功 re-fetch，其余 9 个 re-fetch 报错（`pushed_at` KeyError）；但都是低 star 项目（79-8194），数据可信度足够
- **trap #13b recency 分级**：本期对"上下文工程"类关键词放宽 floor 到 2026-02-01（旧文硬截止 5-01 会让核心信号流失），其他关键词保持 2026-05-01 硬截止

## 5. 自动化建议

- 微信关键词清单更新：用 "Model Context Protocol" 替代 "MCP协议"（避开搜狗硬封）
- 主题分类增加 "Agent Routing / 智能体路由" 单独桶（本期 GitHub 侧命中 2 个）
- 后续维护可考虑 CSDN 公开搜索作为兜底（本期未触发，但搜狗封得越严，CSDN 越重要）
