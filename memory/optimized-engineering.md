# AI 工程化 三级知识结构面试题

> 基于 10 篇微信文章整理的 AI 工程化知识体系  
> 更新时间：2026-03-23

---

## Level 1 主题一：AI 工程化核心概念

### Level 2 子主题 1.1：什么是 AI 工程化

#### Level 3 知识点 1.1.1：AI 工程化定义

📖 **核心概念**：
AI 工程化不是对 AI 技术的升级，而是对 AI 落地逻辑的重构。它将软件工程的标准化、自动化、可复用思维融入 AI 全生命周期，让 AI 从"实验室玩具"变成"生产级应用"。核心模块：DataOps（数据运营）、MLOps（机器学习运营）、DevOps（开发运营）。

❓ **常见面试题**：
1. 什么是 AI 工程化？
2. AI 工程化的核心模块有哪些？

✅ **参考答案要点**：
- 定义：对 AI 落地逻辑的重构，非技术升级
- 核心：标准化、自动化、可复用
- 模块：DataOps、MLOps、DevOps
- 目标：让 AI 从实验室走向生产

🔗 **关联文章**：
- [AI 工程化：不止于技术，更是汽车行业智能化的必经之路 - Rational (2026-02-02)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bFhT7mSgUo82zZZ2YjZrZUVqXa8Fplpd9njKTHBjYXGHtvrDPzHZP7gtiMTp_9D9UlpclwM_MePl8hEBFrY_8eJIAvhMWhqOMMZsdc92gPygBt7U2uDKs0cIBO04EO7RbP3hmBdDtRMCkjsrNP8oNt-uxBHkDPyx3oxecyuYJ93KHmN9E287Rrd-_g6d4YxBwhLW3rpeasK4O8fIRwtipOg..&type=2&query=AI+工程化)

📊 **难度标注**：⭐

---

#### Level 3 知识点 1.1.2：AI 工程化五个维度

📖 **核心概念**：
AI 工程化的五个维度：1) 数据工程（数据采集、清洗、标注）；2) 模型工程（训练、微调、评估）；3) 部署工程（推理优化、服务化）；4) 监控工程（性能监控、漂移检测）；5) 安全工程（权限控制、审计日志）。别再只聊 prompt 了，工程化才是真正壁垒。

❓ **常见面试题**：
1. AI 工程化包含哪五个维度？
2. 为什么说"别再只聊 prompt 了"？

✅ **参考答案要点**：
- 维度 1：数据工程（采集、清洗、标注）
- 维度 2：模型工程（训练、微调、评估）
- 维度 3：部署工程（推理优化、服务化）
- 维度 4：监控工程（性能监控、漂移检测）
- 维度 5：安全工程（权限控制、审计）
- 原因：prompt 只是表层，工程化才是壁垒

🔗 **关联文章**：
- [AI 工程化的五个维度：别再只聊 prompt 了 - 猫切 Web 开发 (2026-03-12)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bFhT7mSgUo82zZZ2YjZrZUVqXa8Fplpd9v6mTkJM8Rlk47MHBnqar_xVMtXcN8UWTZZKaFVigLxOsJ5deVgdEvmf4jx0WLQLkbW0ujtGye4doUY5kqoFXlRuhtbgSZ-Hs-fSRTEivxSaSDvwvUZiLVOmDGVodPhh4TMeEaokpZTHZvamY5Q0u81cC-Flw8F2KSUtRwZIW4mH1AfaFW2DefQ..&type=2&query=AI+工程化)

📊 **难度标注**：⭐⭐

---

### Level 2 子主题 1.2：AI 工程化技术栈

#### Level 3 知识点 1.2.1：Python+ .NET 黄金组合

📖 **核心概念**：
AI 工程化落地的最优解是"Python 做模型研发，.NET 做工程化落地"。Python 生态丰富（PyTorch、TensorFlow、LangChain），适合模型研发；.NET 性能稳定、企业级支持好，适合生产部署。这已成为众多企业 AI 落地的首选路径。

❓ **常见面试题**：
1. 为什么推荐 Python+.NET 组合？
2. Python 和.NET 在 AI 工程化中各有什么优势？

✅ **参考答案要点**：
- Python 优势：生态丰富，模型研发首选
- .NET 优势：性能稳定，企业级支持好
- 组合：Python 研发 + .NET 部署
- 价值：兼顾创新与稳定

🔗 **关联文章**：
- [Python 搞模型，.NET 落地:AI 工程化首选.NET - .net 架构师大佬 (2026-03-19)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bFhT7mSgUo82zZZ2YjZrZUVqXa8Fplpd9v4f5KPJ1387dOcBcn4goh3KN96dZSsTCOOkM6k-VpkdYwD52NFUpVV1qBJKyDw7BeqpqU0G-7y0SAxqB5OfO27tiIk6wB9raxrk6MgMp1TV5jiK0VK1MmtNRGMG7xLkYjfFQsfjp49rUvBA1PhGGHkQliH_YzUeIRcgcFhjXE8nm0CtGSSkZQQ..&type=2&query=AI+工程化)

📊 **难度标注**：⭐⭐

---

#### Level 3 知识点 1.2.2：Java+AI 工程化趋势

📖 **核心概念**：
Spring AI Alibaba 引领 Java+AI 工程化新范式，像混合动力汽车的双引擎系统，将传统 Java 生态与大模型能力完美融合。企业转型成功率提升 47%。Java 优势：企业级生态、稳定性高、人才储备足。

❓ **常见面试题**：
1. Java 在 AI 工程化中有什么优势？
2. Spring AI Alibaba 是什么？

✅ **参考答案要点**：
- Java 优势：企业级生态、稳定性高、人才足
- Spring AI Alibaba：Java+AI 新范式
- 比喻：像混合动力汽车双引擎
- 数据：企业转型成功率提升 47%

🔗 **关联文章**：
- [Java+AI 工程化趋势：像混合动力汽车一样双引擎驱动 - 小黄学算法 (2026-03-20)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bFhT7mSgUo82zZZ2YjZrZUVqXa8Fplpd9H0CnWyaW_Fj0rs2pa60p-PfD0LrEXoS0kTjAMmXCbbu_xMPgLk-bQO5kpv1ls7SBCdrVocqjpnyK2iQYMnoBXr6_hpApj2Q-wdOany9a6DHiyCMp2lsZLaDN9dgrU-oamG1xMfdo1W04pjprLN6QeYNMkE0Tad_QBvv0YZQdGoP1AfaFW2DefQ..&type=2&query=AI+工程化)

📊 **难度标注**：⭐⭐

---

## Level 1 主题二：AI 工程化实战

### Level 2 子主题 2.1：从 Vibe Coding 到 Harness Engineering

#### Level 3 知识点 2.1.1：AI 工程化演进路径

📖 **核心概念**：
AI 工程化演进路径：2024 Vibe Coding（直觉驱动）→ 2025 SDD（规范驱动）→ 2026 Harness Engineering（系统驾驭）。Harness Engineering 核心：让开发者成为"AI 驾驭者"，关注系统设计>代码实现，产品感>编程技能。

❓ **常见面试题**：
1. AI 工程化的演进路径是什么？
2. 什么是 Harness Engineering？

✅ **参考答案要点**：
- 路径：Vibe Coding → SDD → Harness Engineering
- Harness Engineering：系统驾驭，AI 驾驭者
- 核心：系统设计>代码实现
- 趋势：从直觉到规范到系统

🔗 **关联文章**：
- [AI 工程化的五个维度：别再只聊 prompt 了 - 猫切 Web 开发 (2026-03-12)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bFhT7mSgUo82zZZ2YjZrZUVqXa8Fplpd9v6mTkJM8Rlk47MHBnqar_xVMtXcN8UWTZZKaFVigLxOsJ5deVgdEvmf4jx0WLQLkbW0ujtGye4doUY5kqoFXlRuhtbgSZ-Hs-fSRTEivxSaSDvwvUZiLVOmDGVodPhh4TMeEaokpZTHZvamY5Q0u81cC-Flw8F2KSUtRwZIW4mH1AfaFW2DefQ..&type=2&query=AI+工程化)

📊 **难度标注**：⭐⭐⭐

---

## 📊 面试题汇总

### 基础题（⭐）
1. 什么是 AI 工程化？
2. AI 工程化的核心模块有哪些？
3. AI 工程化包含哪五个维度？

### 进阶题（⭐⭐）
4. 为什么推荐 Python+.NET 组合？
5. Java 在 AI 工程化中有什么优势？
6. Spring AI Alibaba 是什么？

### 高级题（⭐⭐⭐）
7. AI 工程化的演进路径是什么？
8. 什么是 Harness Engineering？

---

**生成时间**：2026-03-23  
**文章来源**：10 篇 AI 工程化微信文章
