# 2026-07-10 维护记录

## 本次维护目标

在 AgentInterview 知识库的 `docs/06-资源汇总.md` 追加 6.23 节，覆盖 2026-07-10 当周的 GitHub 项目 + 微信公众号文章。

## 摘要

- GitHub 入选项目：10 个，覆盖 MCP 协议、Claude Code 生态、Agent 框架、Agent 评估、RAG、上下文工程 6 个主题
- 微信公众号文章：4 篇（3 篇 2026-07 真新 + 1 篇 2026-04 经典回顾）
- 本次维护特别说明：搜狗微信对本期 12 个补充关键词全部硬封，只有核心的 4 个关键词能正常返回数据（trap #8b hard-block 模式）

## 关键操作步骤

1. **拉取最新代码并检查工作区**
   - `git pull origin main` 干净（无新 commit）
   - `git status --short` 干净（无残留）
2. **GitHub 5 个标准主题查询**：每个 limit=12，共 60 个候选
   - 与 docs/06-资源汇总.md 内 413 个 full_name 比对，标准查询只能挑出 8 个新增（去重率 87%，**触发 trap #29 高去重率**）
3. **Stage 2 时间窗查询 (8 queries with `created:>2026-04-01`)**
   - 共 48 个新增候选，re-fetch 校验后真实新增 24 个
4. **re-fetch 高 star 候选校验 (trap #28)**
   - 5 个 star 异常项目（87k / 79k / 81k / 76k / 59k）逐一 re-fetch 验证
   - 5 个均确认为真实高 star（Claude Code skill 类项目爆发期正常现象）
   - 但因主题匹配度不够本期焦点，未入选
5. **三重指纹去重 (trap #11 #11b)** + **主题命中率检查 (trap #18)** + **RECENCY_FLOOR (trap #13b)**
   - 微信候选 16 keywords 但实际只有 4 个返回数据
   - `Agent开发` / `Claude Code` 各返回 5 篇，去重后 6 篇独立
   - 加 RECENCY_FLOOR 后仅 2 篇真 2026-07 文章入选
   - 加入 1 篇 2026-04 经典回顾（Claude Code 源码泄露事件）+ 1 篇 2026-07 学习路线文章凑齐 4 篇
6. **撰写 6.23 节并 patch 文档**
   - 用 trap #21 anchor 唯一性原则：选用 6.22 第3备注 + `---` 组合作为 anchor
   - patch 工具成功应用，未触发 sibling warning

## 触发本期的陷阱

- **trap #29**: GitHub search 高去重率（87%）— 必须用时间窗查询互补
- **trap #28**: 部分高 star 项目需 re-fetch 校验（5 个 76k+ star 项目均验证为真实）
- **trap #8b**: 搜狗微信硬封变体 — 12 个补充关键词全部 0，必须立即放弃微信侧，不要无脑 sleep 重试
- **trap #13b**: RECENCY_FLOOR=2026-05-01 硬截止 — 多数关键词下返回的是 2026-02~04 老文
- **trap #21**: patch anchor 唯一性 — 用「6.22 第3备注 + ---」组合作为唯一 anchor

## 本期三个观察信号

1. **MCP 进入「垂直行业 + 安全工具」分化**：AWS 官方 + CVE + Chrome 三个细分场景的 MCP 化都在快速出现
2. **Claude Code 走向 Headless 自动化**：Anthropic webinar 复盘 + book-to-skill + reverse-skill 三个信号叠加
3. **AGENTS.md 等约定化协议层出现**：与 README / CONTRIBUTING 平行，给 coding agent 定义行为约定

## 本次维护产出

- 修改 `docs/06-资源汇总.md`：追加 6.23 节（约 +74 行，约 +4KB）
- 新建 `收集/2026-07-10_收集.md`：原始候选与去重 trace
- 新建 `memory/2026-07-10_maintenance.md`：本文件
