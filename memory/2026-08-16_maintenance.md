# 2026-08-16 维护记录

## 维护概述

- **仓库**: zhouzhupianbei/AgentInterview
- **增量章节**: 6.28（上一节 6.27 为 2026-08-13）
- **GitHub 入选**: 10 个新项目
- **微信入选**: 6 篇

## 关键工作流步骤

### Step 1: cd + pull + 解决冲突
- `git pull` 报 `memory/2026-08-13_maintenance.md` 有 add/add 冲突（上次 cron 另一端未推送）
- 解决冲突（保留 HEAD 端已推送信息）+ merge commit `12076df` + `git push` 推送
- 修复后仓库干净

### Step 2: 读现有 6.X 章节
- 最后章节 6.27 (2026-08-13)，下一节 6.28
- 模板严格沿用 6.27

### Step 3: GitHub 5 std + 5 stage-2 查询
- 标准 query: 60 候选
- stage-2 time-window (`created:>2026-05-01`): 41 候选
- **去重后 20 个真新项目** (247 已入库 → dedup rate 77%)
- 高星 re-fetch (≥3000⭐): 1 个校验 (`MakazhanAlpamys/Soup` 真实, 7 月项目, 持续活跃)

### Step 4: 精选 10 个项目
- skip-list（trap #28 已知错位 + 兄弟会话标记）剔除 5 个
- recency (pushed_at >= 2026-05-16) 过滤剩 10 个
- 应用 trap #20 重分类：`aws-samples/sample-well-architected-skills-and-steering` 从「其他」归到「Agent Harness」(topics 含 claude-code/cursor/codex)
- 分类分布: MCP 3 / Harness 2 / LLM 微调 1 / 其他 4

### Step 5: 微信抓取 + trap #13b 硬截止 + bug fix
- 9 关键词 → 主题命中率 9/9 全通过
- RECENCY_FLOOR (2026-05-16) 应用后 **6 个关键词整类砍掉** (RAG系统 / MCP Server / MCP 工具 / 上下文工程 / Agent评估 / Agent面试)
- 修复 quality_score bug: `source_account` → `source` (normalized field) — 修复前 InfoQ 文章 q=-3 (老文扣分), 修复后 q=+8
- `MCP协议` UnicodeEncodeError → fallback 到 `MCP Server` / `MCP 工具` (但都被 50% 老文硬砍)
- 最终 6 篇入库（Agent开发 3 + Claude Code 3）

### Step 6: Python append 6.28 章节
- trap #21b: docs/06-资源汇总.md 1604 行 → Python append 而非 patch
- anchor `## 📚 核心资源汇总` 唯一 (1 处)
- +7512 chars / +48 行

### Step 7: 收集 + memory + commit + push
- `收集/2026-08-16_收集.md`: 抓取 / 过滤 / 精选全过程
- `memory/2026-08-16_maintenance.md`: 本文件
- `git add` 用具体路径，不带 `-A`

## 应用的 trap 清单

| Trap | 应用情况 |
|------|---------|
| #6b (commit 后日志竞态) | Python 一次性写入，无竞态 |
| #6c (cron 开头清理残留) | 开头 `git status --short` 发现冲突, 解决后再维护 |
| #7 (conda python 解释器) | 用 `/Users/lvguofei/miniconda3/bin/python3` 绝对路径 |
| #8 (微信静默限流) | 关键词间 `time.sleep(2.5)`，无硬封触发 |
| #9 (star 噪声过滤) | 0 个被过滤（双阈值均通过） |
| #10 (jisu JSON 字段名) | 字段正确使用：`source_account`/`publish_time` |
| #11 (指纹去重) | 三重 fingerprint union 抽取 694 个, dedup 准确 |
| #12 (相关性打分) | `relevance_agent()` + recency + 反向惩罚 |
| #13 (quality_score) | **bug fix**: source 字段读取修正后, InfoQ q=+8 |
| #13b (RECENCY_FLOOR 硬截止) | **关键**: 6/9 关键词因 50%+ 老文硬砍, 命中 6 篇真正新文 |
| #14 (AgentInterview 资源结构) | `docs/06-资源汇总.md` 6.X 编号延续, 不用日期分区 |
| #18 (中文短关键词歧义) | trap #13b 配套, 命中率 + 时效性双校验 |
| #20 (miscategorize) | `aws-samples/...` 从「其他」归到「Agent Harness」(topics 含 claude-code) |
| #21b (大文件 Python append) | 文件 1408 行 → Python append 而非 patch |
| #28 (full_name 错位) | skip-list 主动排除 `comet-ml/opik-openclaw` |
| #29 (GitHub 高去重率) | 标准 5 query → stage-2 `created:>2026-05-01` 时间窗互补 |
| #30 (高 star ≠ 数据错位) | re-fetch `MakazhanAlpamys/Soup` 确认 1570 stars 真实 |
| #32 (微信分级 RECENCY_FLOOR) | 未应用分级放宽, 接受本期微信偏少 |

## 提交哈希（待 push 后回填）

## 推送状态（待验证）