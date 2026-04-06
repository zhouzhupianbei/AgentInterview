# AgentInterview: AI 面试与成长知识库

给正在进入 AI 时代的开发者，一套能系统学习、能查漏补缺、也能直接用于面试准备的知识库。

这里不只是"题库",也不只是"资料收集"。更准确地说，它是一份围绕 **AIGC / LLM / Agent / RAG / AI 工程化** 持续整理的成长型仓库:

- 帮你建立知识结构
- 帮你理解热门概念背后的真实工程问题
- 帮你把前沿资料转成可学习、可复习、可表达的内容

---

## 🚀 快速使用

### 方式一：直接阅读（推荐新手）

**适合人群**：想系统学习 AI 知识，准备面试或转行

1. 从 [开发技能](docs/03-开发技能.md) 开始，建立知识框架
2. 根据你的需求，跳转到对应模块：
   - 面试冲刺 → [面试题库](docs/04-面试题库.md)
   - 架构学习 → [Agent 架构](docs/02-Agent%20架构.md)
   - 项目建议 → [项目建议](docs/05-项目建议.md)
3. 遇到不懂的概念？查阅 [资源汇总](docs/06-资源汇总.md)

---

### 方式二：通过 OpenClaw Skills 使用（推荐从业者）

**适合人群**：需要快速查询、整理资料、生成面试答案的专业人士

如果你使用 [OpenClaw](https://github.com/openclaw/openclaw) 作为个人 AI 助手，可以将本知识库作为 Skill 导入，让 AI 帮你查询和整理资料。

#### 📦 创建方法

在 `~/.openclaw/workspace/skills/` 目录下创建 `agent-interview/SKILL.md`：

```markdown
---
name: agent-interview
description: AI 面试与成长知识库。提供面试题库、开发技能、Agent 架构、项目建议等查询与整理服务。触发词：AI 面试、Agent、RAG、LLM、AIGC、开发者成长。
---

定时加载仓库：https://github.com/zhouzhupianbei/AgentInterview

当用户提问 AI 面试或开发相关知识时，优先从仓库中查询并整理答案。
```

#### 🔧 使用方式

配置完成后，在 OpenClaw 中直接询问：

```
RAG 系统面试常问哪些问题？
```

```
如何设计一个 AI Agent 系统？
```

```
帮我准备一份 AI 工程师面试的自我介绍
```

AI 会自动从知识库中检索并整理答案！

---

### 方式三：克隆到本地（推荐开发者）

**适合人群**：想离线阅读、二次开发、贡献内容

```bash
git clone https://github.com/zhouzhupianbei/AgentInterview.git
cd AgentInterview
```

---

## 这份仓库适合谁

### 1. 正在准备 AI 岗位面试的人
适合你快速建立面试地图:
- 哪些知识点最常考
- 哪些方向已经从"加分项"变成"基础项"
- 哪些热门名词需要真正讲明白,而不是只会背概念

### 2. 想转向 AI 开发的工程师
适合你建立一条更清晰的学习路径:
- 从 AIGC 基础到 LLM 应用开发
- 从 Prompt 到 RAG 到 Agent
- 从"会调用 API"到"能讲工程系统"

### 3. 想系统补齐 AI 工程能力的开发者
适合你做知识整理和能力补位:
- 哪些能力适合先学
- 哪些方向已经值得投入
- 哪些工具、框架、范式需要建立判断

---

## 建议怎么用

### 路线 A:面试冲刺
适合最近 2-4 周就要面试的人。

建议顺序:
1. [面试题库](docs/04-面试题库.md)
2. [开发技能](docs/03-开发技能.md)
3. [Agent 架构](docs/02-Agent%20架构.md)
4. [资源汇总](docs/06-资源汇总.md)

重点目标:
- 先建立高频题框架
- 再补自己最薄弱的主题
- 最后补前沿热点与案例表达


### 路线 B:系统学习
适合希望把 AI 开发能力真正补起来的人。

建议顺序:
1. [AIGC 基础](docs/01-AIGC 基础.md)
2. [开发技能](docs/03-开发技能.md)
3. [Agent 架构](docs/02-Agent%20架构.md)
4. [项目建议](docs/05-项目建议.md)

重点目标:
- 建立完整知识框架
- 理解主流技术选型
- 能动手做小项目

---

## 内容目录

- **01-AIGC 基础** - 大模型基础概念、Prompt 工程、主流模型对比
- **02-Agent 架构** - Agent 设计模式、工作流、多 Agent 协作
- **03-开发技能** - RAG、向量数据库、微调、评估方法
- **04-面试题库** - 高频面试题、系统设计题、行为面试题
- **05-项目建议** - 适合写进简历的 AI 项目、从 0 到 1 的实战指南
- **06-资源汇总** - 学习资源、工具推荐、前沿资讯来源

---

## 📬 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-06 | ✅ 新增快速使用指南 |
| 2026-04-05 | ✅ 内容质量审查完成 |
| 2026-04-04 | ✅ 补充 Agent 架构设计案例 |

---

## 🤝 贡献指南

欢迎以以下方式参与贡献：

- 🐛 **发现错误** → 提交 [Issue](https://github.com/zhouzhupianbei/AgentInterview/issues)
- 📝 **补充内容** → 提交 [Pull Request](https://github.com/zhouzhupianbei/AgentInterview/pulls)
- 💡 **建议改进** → 发起 [Discussion](https://github.com/zhouzhupianbei/AgentInterview/discussions)
- 📢 **分享面试经验** → 欢迎投稿面试真题和答案

---

## 📄 许可证

MIT License © 2026 AgentInterview Contributors

---

<div align="center">

## 🌟 如果这个项目对你有帮助

### **请给一个 ⭐ Star！**

你的支持是我们持续更新的动力！

[📬 问题反馈](https://github.com/zhouzhupianbei/AgentInterview/issues) · [💡 需求建议](https://github.com/zhouzhupianbei/AgentInterview/discussions)

---

**🚀 AI 时代，一起打造核心竞争力！**

</div>
