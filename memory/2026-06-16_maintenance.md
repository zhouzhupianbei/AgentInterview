# Maintenance Log - 2026-06-16

## 概要

- **仓库**: zhouzhupianbei/AgentInterview
- **更新文件**:
  - `docs/06-资源汇总.md`（新增 6.16 节）
  - `收集/2026-06-16_收集.md`（新建原始资料汇总）
- **新增 GitHub 项目**: 10 个
- **新增微信文章**: 10 篇
- **上一次维护**: 2026-06-13（间隔 3 天）

## 本次主题

聚焦 2026 年 6 月中旬的三大新热点：

1. **Agent 框架多语言生态快速扩张** — Go（trpc-agent-go）/ Java（agents-flex）/ PHP（neuron-ai）三个非 Python 的 Agent 框架出现在高活跃榜单，说明 agentic AI 正在走出"Python 单一生态"，进入企业后端语言主流视野。
2. **Agent 评估成为产业化关键瓶颈** — 微信公众号 2026-06 集中爆发 Agent 评估话题（拆解 Anthropic 体系 / AWS EvalKit / 从 0 到 1 评估体系），与 GitHub 端 lmnr（Laminar）等观测平台热度一致——"没评估就没规模化"正在成为行业共识。
3. **Prompt 工程范式正在被反思** — 6.16 节收录的"Prompt 工程 的第四份讣告"虽然标题挑衅，但反映了一种新共识——纯 prompt 调优已让位于上下文工程 / Agent Harness / 结构化输出（如 BAML）等更高阶抽象。

## 详细变更

### docs/06-资源汇总.md
- 新增 6.16 节：2026-06-16 增量更新
  - 6.16.1 Agent 框架与运行时：4 个项目（trpc-agent-go、agents-flex、dynamiq、neuron-ai）
  - 6.16.2 RAG / 检索增强：2 个项目（agentic-rag-for-dummies、Verba）
  - 6.16.3 LLM 微调：2 个项目（LLM-Finetuning-Toolkit、xTuring）
  - 6.16.4 LLM 评估 / 可观测性：1 个项目（lmnr）
  - 6.16.5 上下文工程 / Prompt 学习：1 个项目（prompt-in-context-learning）
  - 6.16.6 微信公众号文章：10 篇（Agent 3 + RAG 1 + 上下文 2 + Prompt 1 + 评估 2 + 综合 1）

### 收集/2026-06-16_收集.md
- 新建原始资料汇总
- 包含 GitHub 检索概览表（46 候选 → 通过相关性 + 链接去重 → 10 精选）
- 包含微信公众号检索概览（40 篇原始 → 32 篇指纹去重 → 24 篇时间过滤 + AI面试剔除 → 10 篇精选）

## 涉及 GitHub 主题

agent, llm, rag, langchain, llamaindex, peft, lora, fine-tuning, agent-evaluation, agent-observability, agent-framework, context-engineering, prompt-engineering, rag-pipeline, java-agent, go-agent, php-agent

## 维护工具与脚本

- GitHub REST API 直调（`urllib.request`），未使用 `gh search repos`
- `jisu-wechat-article/search.py` 通过 conda 解释器绝对路径 `/Users/lvguofei/miniconda3/bin/python3` 调用
- 关键词抓取间隔 2.5s，8 个关键词全部正常返回（无静默限流）
- 链接去重：从 `docs/06-资源汇总.md` 抽取所有 `https://github.com/...` 链接（共 127 个），过滤重复
- 微信去重：标题归一化指纹（前 12 字符）+ 全标题双重比对
- 可疑过滤：`age_days < 180 and stars > 30000` → 自动剔除（如 gsd-build/get-shit-done 64k⭐ 在本批）

## 下次维护建议

- 关注 **AWS Agent-EvalKit / Anthropic 评估体系** 等评估基础设施开源动向
- 跟踪 **trpc-agent-go** 等非 Python Agent 框架是否进入企业生产案例
- 监控 **prompt-in-context-learning** 等综合性资源汇总的 star 增速
