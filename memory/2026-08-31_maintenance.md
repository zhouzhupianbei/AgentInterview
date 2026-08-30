# 2026-08-31 维护记录

## 维护概述

- **仓库**: zhouzhupianbei/AgentInterview
- **增量章节**: 6.29（上一节 6.28 为 2026-08-16）
- **GitHub 入选**: 10 个新项目
- **微信 + 海外媒体入选**: 8 篇

## 关键工作流步骤

### Step 1: cd + pull + 状态检查
- `git pull origin main` 成功，无冲突
- `git status --short` 干净
- 上一节 6.28 (2026-08-16)，下一节 6.29

### Step 2: GitHub 10 个查询 + dedup
- 标准 5 query × limit=12 = 60 候选
- 时间窗 5 query (`created:>2026-06-01`) × limit=12 = 31 额外候选
- 总候选: 91
- 去重 (vs 257 已入库 full_name): 31 个真新项目 (dedup rate 66%)
- 相关性打分 (rel>=4): 31 通过
- 高星 re-fetch (>=3000⭐): 4 个 (`mongodb-developer/GenAI-Showcase` 4261⭐ / `OpenBMB/AgentVerse` 5117⭐ / `trigaten/Learn_Prompting` 4728⭐) + skip `comet-ml/opik-openclaw` (trap #28)

### Step 3: 精选 10 个项目
- 分类: Agent Harness 4 / MCP 3 / Agent 框架 1 / RAG 1 / 评估 1
- trap #20 重新分类: `calmrocks/ai-engineer-notebooks` 从「其他」归到「Agent 框架 / 多智能体」(topics 含 ai-engineering / forward-deployed-engineer / llmops)

### Step 4: 微信抓取 + trap #13b + trap #32
- 8 个关键词 (Agent开发 / Claude Code / MCP协议 / Agent评估 / 上下文工程 / RAG系统 / 大模型 / AI Agent)
- **RECENCY_FLOOR 分级** (trap #32):
  - 严 (2026-07-01): Agent开发 / Claude Code / MCP协议
  - 中 (2026-05-01): Agent评估 / 上下文工程 / AI Agent
  - 宽 (2026-03-01): RAG系统 / 大模型
- 微信侧保留 4 篇 (Agent开发 3 + Agent评估 1)
- Claude Code / MCP协议 / 上下文工程 命中文章均 < 2026-05（trap #13b 硬砍）

### Step 5: web_search 兜底
- 搜狗微信 Claude Code / MCP 关键词严重老化（最新 2026-04），触发 web_search 兜底
- query 1: "2026年8月 Claude Code Agent Harness 工程实践 微信公众号"
- query 2: "2026年8月 MCP server Claude Code 实战 教程 公众号"
- 4 篇海外技术媒体入选 (Tenten AI / DEV Community / Markaicode / Web Pulse)
- **章节头部明确标注 web_search 来源** (trap #8c 诚实标注渠道)

### Step 6: Python append 6.29 章节
- trap #21b: docs/06-资源汇总.md 1652 行 → Python append 而非 patch
- anchor `## 📚 核心资源汇总` 唯一 (1 处)
- +7559 chars / +59 行

### Step 7: 收集 + memory + commit + push
- `收集/2026-08-31_收集.md`: 抓取 / 过滤 / 精选全过程
- `memory/2026-08-31_maintenance.md`: 本文件
- `git add` 用具体路径，不带 `-A`

## 应用的 trap 清单

| Trap | 应用情况 |
|------|---------|
| #6c (cron 开头清理残留) | 开头 `git status --short` 干净 |
| #7 (conda python 解释器) | `/Users/lvguofei/miniconda3/bin/python3` 绝对路径 |
| #8 (微信静默限流) | 关键词间 `time.sleep(2.5)`，无硬封触发 |
| #8c (web_search primary fallback) | **触发**: 微信 Claude Code/MCP 严重老化, web_search 兜底补足 |
| #10 (jisu JSON 字段名) | 字段正确使用：`source_account`/`publish_time` |
| #11 (指纹去重) | 三重 fingerprint union 抽取 792 个, dedup 准确 |
| #12 (相关性打分) | `relevance_agent()` + recency + 反向惩罚 |
| #13 (quality_score) | 微信 trusted 5 + recency 4 加分 |
| #13b (RECENCY_FLOOR 硬截止) | **关键**: Claude Code/MCP/上下文工程 命中文章全 < 2026-05, 整类砍掉 |
| #14 (AgentInterview 资源结构) | `docs/06-资源汇总.md` 6.X 编号延续, 不用日期分区 |
| #18 (中文短关键词歧义) | trap #13b 配套, 命中率 + 时效性双校验 |
| #20 (miscategorize) | `calmrocks/...` 从「其他」归到「Agent 框架」(topics 重分类) |
| #21b (大文件 Python append) | 文件 1652 行 → Python append 而非 patch |
| #28 (full_name 错位) | skip-list 主动排除 `comet-ml/opik-openclaw` |
| #29 (GitHub 高去重率) | 标准 5 query → stage-2 `created:>2026-06-01` 时间窗互补 (66% 去重率) |
| #30 (高 star ≠ 数据错位) | 4 个高星候选 re-fetch 全部一致, 确认真实 |
| #32 (微信分级 RECENCY_FLOOR) | **关键**: 8 关键词分 3 级 floor, 严/中/宽分别 2026-07-01 / 2026-05-01 / 2026-03-01 |
| #40 (WeChat 标题 `|` 破坏 pipe 表) | 写 description 时替换 `|` 为 `/` 防 markdown 表格破坏 |

## 本期补充统计

- GitHub 新项目: 10 个 (Agent Harness 4 / MCP 3 / Agent 框架 1 / RAG 1 / 评估 1)
- 微信文章: 4 篇 (Agent开发 3 + Agent评估 1)
- web_search 海外媒体: 4 篇 (Claude Code Harness + MCP 生产部署)
- 主题聚焦: Agent Harness 标准化 + MCP 跨域协议 + Claude Code MCP 生产化
- 关键信号: HarnessRouter 协议化 + x64dbg-MCP 行业垂直化 + Harness Engineering Phase 1~7 方法论