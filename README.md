# AIGC 时代开发者面试指南

> **副标题**：面向 AI 开发者的一站式面试准备资源  
> **版本**：v1.3  
> **更新时间**：2026 年 3 月 22 日 (自动更新)

[![GitHub stars](https://img.shields.io/github/stars/zhouzhupianbei/AgentInterview?style=for-the-badge)](https://github.com/zhouzhupianbei/AgentInterview)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg?style=for-the-badge)](https://github.com/zhouzhupianbei/AgentInterview/blob/main/LICENSE)
[![Issues](https://img.shields.io/github/issues/zhouzhupianbei/AgentInterview?style=for-the-badge)](https://github.com/zhouzhupianbei/AgentInterview/issues)
[![2026 Updates](https://img.shields.io/badge/2026-MCP%2C%20GraphRAG%2C%20Deep%20Agents-green?style=for-the-badge)](./docs/06-资源汇总.md#610-2026-新技术与标准)

---

## 📖 项目介绍

本项目是一份专为 AIGC 时代开发者打造的面试指南，涵盖 AI Agent、大模型应用开发、AIGC 核心技术等热门领域的面试干货。内容源自一线大厂面试真题、开源社区精华资源以及行业从业者的实战经验。

### 适用人群

- 🎯 求职 AI 算法岗/开发岗的应届生
- 🎯 希望转型 AI 开发的传统软件工程师
- 🎯 准备面试 AIGC 相关岗位的在职开发者
- 🎯 想了解 AIGC 面试考点的技术管理者

### 核心内容

```
AgentInterview/
├── README.md                 # 本文件
├── docs/
│   ├── 01-AIGC 基础.md        # AIGC 核心概念与主流模型
│   ├── 02-Agent 架构.md       # AI Agent 设计模式与实战
│   ├── 03-开发技能.md         # AI 开发者必备技能栈
│   ├── 04-面试题库.md         # 分类面试题与参考答案
│   ├── 05-项目建议.md         # 适合写进简历的 AIGC 项目
│   └── 06-资源汇总.md         # 学习路线与优质资源
├── examples/
│   ├── simple-agent.py       # 简单 Agent 示例代码
│   ├── prompt-templates.md   # 常用 Prompt 模板
│   └── rag-demo.py           # RAG 实现示例
└── SUMMARY.md                # 项目完成情况说明
```

---

## 🚀 快速开始

### 面试准备路径

```
第 1 周：AIGC 基础 → 大模型原理 → Prompt 工程
第 2 周：Agent 架构 → RAG 技术 → 工具调用
第 3 周：项目实战 → 算法刷题 → 模拟面试
第 4 周：简历优化 → 行为面试 → 薪资谈判
```

### 如何使用本项目

1. **基础薄弱** → 从 `docs/01-AIGC 基础.md` 开始系统学习
2. **紧急面试** → 直接刷 `docs/04-面试题库.md` 高频题目
3. **项目缺失** → 参考 `docs/05-项目建议.md` 快速搭建作品集
4. **查漏补缺** → 查看 `docs/06-资源汇总.md` 深入学习

---

## 📚 核心资源来源

本项目参考了以下优质开源项目：

| 项目 | Stars | 简介 | 更新 |
|------|-------|------|------|
| [WeThinkIn/AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book) | 3.3k+ | AIGC 算法岗面试宝典，涵盖大模型、AI Agent、深度学习等 | 持续更新 |
| [adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide) | 2.6k+ | AI Agent 开发指南，LangGraph 实战，转行大模型 | 2026 新增 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 20k+ | 构建状态化 Agent 的图框架 | 2026 重点 |
| [modelcontextprotocol](https://github.com/modelcontextprotocol) | 8k+ | Model Context Protocol 开放标准 | 2026 新标准 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 12k+ | 基于知识图谱的 RAG 系统 | 2026 热点 |

---

## 🎯 2026 新增内容

### 新技术专题

- **MCP (Model Context Protocol)**：2026 年工具集成新标准
- **GraphRAG**：微软知识图谱增强检索
- **Deep Agents**：LangChain 深度 Agent 框架
- **Agentic RAG**：Agent 自主决策的 RAG 系统

### 更新内容

- 框架对比：LangChain vs LangGraph vs CrewAI vs AutoGen
- 多 Agent 模式：Supervisor、Hierarchical、Workflow
- 部署优化：vLLM 2026 新特性、推理成本优化
- 面试题库：新增 20+ 道 2026 前沿技术题

### 🔄 自动更新 (v1.2 新增)

本项目支持自动更新机制，定期同步最新行业资源：

**本次更新 (2026-03-22) - v1.3**：
- ✅ 新增 **前沿开发模式** 章节 (docs/03-开发技能.md)
  - Vibe Coding（氛围编程）深度解析 + 三级知识结构
  - SDD 规范驱动开发方法论 + 黄金 16 条原则
  - AI 编辑器对比 (Cursor/Trae/通义灵码) + 2026 新动态
- ✅ 新增 **微信公众号精选** 资源 (docs/06-资源汇总.md)
  - 前沿开发模式：30 篇 (Vibe Coding, SDD, Cursor)
  - AI 工程化：10 篇
  - RAG 实战：10 篇
  - Agent 设计：10 篇
- ✅ 新增 **三级知识结构面试题** (docs/04-面试题库.md)
  - 基础题 20 道 + 进阶题 20 道 + 高级题 10 道 + 实战题 5 道
  - 每题包含：题目、知识点、答案、代码、关联文章
- ✅ 完整文章列表：`memory/wechat-articles.json` (60 篇)
- ✅ 优化内容：`memory/optimized-vibecoding.md`、`memory/optimized-sdd.md`
- ✅ 更新报告：`memory/agent-interview-updates-2026-03-22.md`

---

## 🎯 面试考点地图

### AIGC 基础（必考）

- Transformer 架构详解
- Attention 机制原理
- GPT/BERT/LLaMA 等主流模型对比
- Tokenization 方法
- 位置编码（RoPE、ALiBi）

### AI Agent（高频）

- Agent 核心组件（规划、记忆、工具）
- ReAct、CoT、ToT 等推理模式
- Function Calling / Tool Use
- **MCP 协议**（2026 新）
- 多 Agent 协作框架
- **LangGraph 状态机**（2026 重点）
- Agent 评估与优化

### RAG 技术（热点）

- 向量数据库选型
- 检索优化（混合检索、重排序）
- **GraphRAG**（2026 新）
- **Agentic RAG**（2026 新）
- 长文档处理策略

### 开发技能（实战）

- Prompt Engineering 技巧
- 模型微调（LoRA、QLoRA）
- 推理优化与部署（vLLM、TGI）
- **Deep Agents 架构**（2026 新）

---

## 💡 使用建议

1. **不要死记硬背**：理解原理 > 背诵答案
2. **动手实践**：每个知识点配合代码实现
3. **模拟面试**：找同伴进行 mock interview
4. **持续更新**：AIGC 领域变化快，保持学习

---

## 📬 反馈与贡献

欢迎通过以下方式参与项目共建：

- 🐛 发现错误 → 提 Issue
- ✨ 补充内容 → 提 PR
- 💬 面试经验分享 → 欢迎投稿

---

**祝你面试顺利，拿到心仪的 Offer！🎉**
