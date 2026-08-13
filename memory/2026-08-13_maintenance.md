# 2026-08-13 维护记录

## 维护概述

- **仓库**: zhouzhupianbei/AgentInterview
- **增量章节**: 6.27（上一节 6.26 为 2026-08-10）
- **GitHub 入选**: 12 个新项目（focus 在 MCP / Agent 工具协议 + Harness + LLM 微调）
- **微信入选**: 5 篇（应用 trap #13b 硬截止后）

## 关键工作流步骤

### Step 1: cd + pull + 检查 .gitignore
- 仓库干净（`git status --short` 空）
- `.gitignore` 不排除 `memory/` 和 `收集/`（与 trap #14c 一致）

### Step 2: 读现有 6.X 章节
- 最后章节 6.26 (2026-08-10)，下一节 6.27
- 模板严格沿用 6.26：`## 6.NN YYYY-MM-DD 增量更新` + `### 新增 GitHub 项目` + `### 新增微信公众号文章` + 备注

### Step 3: GitHub 5 std + 5 stage-2 查询
- 标准 query: 60 候选
- stage-2 time-window (`created:>2026-05-01`): 41 候选
- **去重后 34 个真新项目**（235 已入库 → dedup rate 67%）
- 高星 re-fetch (≥3000⭐): 6 个校验，差异最大 20 star，无错位

### Step 4: 精选 12 个项目
- 应用 trap #28 误判剔除: `comet-ml/opik-openclaw` + `xai-org/grok-build`
- 应用低质量剔除: `Oft3r/agentic-trading-desk` + `Env-Kit/envkit-releases` + `capture0x/AdStrike`
- 分类分布: MCP 7 / 微调 2 / 其他 3

### Step 5: 微信抓取 + trap #13b 硬截止
- 8 关键词 → 应用 2026-05-13 硬截止后 6/8 关键词整类砍掉
- 仅 `Agent面试` (3 篇) + `MCP Server` (1) + `MCP 工具` (1) + `Model Context Protocol` (1) 通过
- **MCP协议 直接调用 UnicodeEncodeError** — fallback 到 `MCP Server` 变体
- 最终 5 篇入库

### Step 6: patch `docs/06-资源汇总.md`
- 用 Python 整段插入到 `## 📚 核心资源汇总` anchor 前
- trap #21b 验证: anchor 唯一（1 处匹配）
- 全文无 Mermaid 代码块，无需全角字符清洗

### Step 7: 创建 `收集/` + `memory/`，精确 add + commit
- `收集/2026-08-13_收集.md`: 抓取 / 过滤 / 精选全过程
- `memory/2026-08-13_maintenance.md`: 本文件（按 7 步工作流记录）
- `git add` 用具体路径，不带 `-A`

## 应用的 trap 清单

| Trap | 应用情况 |
|------|---------|
| #6b (commit 后日志竞态) | 已用 Python 一次性写入，避免 log() 漏写 |
| #6c (cron 开头清理残留) | 开局 `git status --short` 已确认干净 |
| #7 (conda python 解释器) | 用 `/Users/lvguofei/miniconda3/bin/python3` 绝对路径 |
| #8 (微信静默限流) | 关键词间 `time.sleep(2.5)`，无硬封触发 |
| #9 (star 噪声过滤) | 0 个被过滤（双阈值均通过） |
| #11 (指纹去重) | 三重 fingerprint union 抽取 665 个，dedup 准确 |
| #12 (相关性打分) | `relevance_agent()` + 时间加分 + 反向惩罚 |
| #13 (微信 quality_score) | recency + trusted + promo 惩罚 |
| #13b (RECENCY_FLOOR 硬截止) | **关键**: 6/8 关键词硬砍，命中 5 篇真正新文 |
| #14 (AgentInterview 资源结构) | `docs/06-资源汇总.md` 6.X 编号延续，不用日期分区 |
| #14c (.gitignore 不排除 memory) | 3 个文件 (docs + 收集 + memory) 都进入 commit |
| #18 (中文短关键词歧义) | trap #13b 配套，命中率 + 时效性双校验 |
| #21b (大文件 Python append) | 文件 127k+ 字符，但用 patch+unique anchor 也成功 |
| #28 (full_name 错位) | 识别 `comet-ml/opik-openclaw` 为子项目，剔除 |
| #29 (GitHub 高去重率) | 标准 5 query → stage-2 `created:>2026-05-01` 时间窗互补 |
| #30 (高 star ≠ 数据错位) | re-fetch 确认 24k star 真实但描述异常仍剔除 |
| #37 (multi-file 改动纪律) | 单文件 patch + py 文件 fetch 脚本独立在 /tmp |
| #40 (微信标题 `|` 破坏 pipe 表) | GEO-Resources 才有，AgentInterview 不适用 |

## 提交哈希

- `34a99fa` — 补充 8 月中旬 MCP 工具链与 Agent 面试深水题资源
- 推送状态: ✅ 已推送到 `origin/main` (commit `968a880..34a99fa`)
