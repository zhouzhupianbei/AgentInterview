# SDD 规范驱动开发 三级知识结构面试题

> 基于 10 篇微信文章整理的 SDD 知识体系  
> 更新时间：2026-03-23

---

## Level 1 主题一：SDD 核心概念

### Level 2 子主题 1.1：什么是 SDD

#### Level 3 知识点 1.1.1：SDD 定义与背景

📖 **核心概念**：
SDD（Specification-Driven Development，规范驱动开发）是 AI 时代的软件工程新范式。核心思想：先写规范（Specification），再让 AI 生成代码。规范是唯一的"事实来源"，代码是规范的自动化表达。SDD 不是对 AI 能力的否定，而是对 AI 使用方式的系统性升级——通过将规范提升为软件系统唯一的"事实来源"，从根本上解决传统开发中规范与代码不一致的问题。

❓ **常见面试题**：
1. 什么是 SDD？它的核心思想是什么？
2. SDD 与 TDD（测试驱动开发）有什么区别？

✅ **参考答案要点**：
- 定义：规范驱动开发，先写规范再生成代码
- 核心：规范是唯一"事实来源"，代码是规范的自动化表达
- 背景：AI 编程时代，解决 Vibe Coding 的不可控问题
- 与 TDD 区别：TDD 测试先行验证行为，SDD 规范先行定义约束

💻 **代码示例**：
```yaml
# SDD 规范示例
specification:
  name: 用户登录
  version: 1.0.0
  
  functional_requirements:
    - 支持邮箱/手机号登录
    - 登录失败 5 次锁定 30 分钟
    - 密码重置通过邮件验证
  
  constraints:
    - 响应时间 < 500ms (P95)
    - 密码加密：bcrypt
    - 会话有效期：24 小时
  
  acceptance_criteria:
    - 正确凭证 100% 登录成功
    - 错误凭证返回明确错误码
    - 锁定期间拒绝所有登录尝试
```

🔗 **关联文章**：
- [AI 时代的新开发模式:SDD 规范驱动开发是什么 - ForeverPx (2026-03-19)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9EOJRqBMnOlgrTVBnqK0BP9j1o2EcHdzptepWO62xbMM882kjBSPe8f77VYtz3iRuWxk0IVVNoyNkP9XUeK8-yv8mZHZpXYF__InARKEFEm2FNAooshwHfy8G4jGRqR3iGtO8ZSw3d4WBpsiuIn69aqMr2MTLIfuXyXCpETALffSrCDCayYmfpA..&type=2&query=SDD+开发)
- [SDD 规范驱动开发:AI 时代的软件工程新范式 - GoFrame 大魔王](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9ogQSlO2aZqZ9mX3U5SQXWHvijentAB1WwEcDEKgCCapnzLywINjh6DHGF8wAP9B7mQF1rA2wD5gTRDcjASA_UsEmm5AKqB6BgQDx0fjbXmq4YPFgVueJATRJxS79_Zn17HrznqJegFArnyPqaamqUxiN426p_t2iHiAbFUTZF91535pjGOOjYg..&type=2&query=SDD+开发)

📊 **难度标注**：⭐

---

#### Level 3 知识点 1.1.2：为什么需要 SDD

📖 **核心概念**：
SDD 解决 Vibe Coding 的四大问题：1) 代码不可控 → 规范作为约束；2) 结果不可预测 → 验收标准明确；3) 难以协作 → 规范即文档；4) 质量不稳定 → 规范驱动测试。SDD 通过将规范提升为"事实来源"，让 AI 生成的代码可控、可预测、可协作、高质量。

❓ **常见面试题**：
1. 为什么需要 SDD？它解决了什么问题？
2. SDD 如何解决 Vibe Coding 的局限性？

✅ **参考答案要点**：
- 问题 1：代码不可控 → 规范作为约束
- 问题 2：结果不可预测 → 验收标准明确
- 问题 3：难以协作 → 规范即文档
- 问题 4：质量不稳定 → 规范驱动测试
- 价值：让 AI 生成代码可控、可预测、可协作

🔗 **关联文章**：
- [规范驱动开发 (SDD) 在生产环境下的落地实践 - 毕方教练团](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9HzNntUEmMCq2AZEQmaLhMQAvZqpTa9wgQnFsGoH5fan2jYC-IuXMDiaoOV-fG6c0vpIbDlQvu9YyVb-zI1vHZ7XAT7eYMEK7iVcnOWrI4Tkj7w8SjHNM3y--XuyHLbKm0JV1F0jmV7flsREdE-KMCxcjbZefqa3zrvtyMsfclucCn9lOoZLP2Q..&type=2&query=SDD+开发)

📊 **难度标注**：⭐

---

#### Level 3 知识点 1.1.3：SDD 工作流

📖 **核心概念**：
SDD 工作流分为三步：1) 编写规范（功能需求、约束条件、验收标准、接口定义）；2) AI 生成代码（基于规范生成实现、自动生成测试用例、输出实现说明）；3) 验证与迭代（运行验收测试、对比规范与实际、修正规范或代码）。这是一个闭环流程，确保代码始终符合规范。

❓ **常见面试题**：
1. 描述 SDD 的完整工作流。
2. SDD 工作流中哪一步最关键？为什么？

✅ **参考答案要点**：
- 步骤 1：编写规范（功能需求、约束、验收标准、接口）
- 步骤 2：AI 生成代码（实现、测试、说明）
- 步骤 3：验证与迭代（测试、对比、修正）
- 最关键：步骤 1（规范质量决定代码质量）

💻 **代码示例**：
```python
# SDD 工作流示例
# 步骤 1: 编写规范 (spec.yaml)
specification:
  name: 快速排序
  input: "未排序的整数列表"
  output: "排序后的整数列表"
  constraints:
    - 时间复杂度：O(n log n) 平均
    - 空间复杂度：O(log n)
  acceptance_criteria:
    - 空列表返回空列表
    - 单元素列表返回原列表
    - 重复元素正确处理

# 步骤 2: AI 生成代码
# "根据以上规范，实现快速排序，包含测试用例"

# 步骤 3: 验证
# 运行测试，对比规范与实际输出
```

🔗 **关联文章**：
- [规约驱动开发 (SDD):AI 编码时代的开发方法论新探索 - 技术知行之路 (2026-03-21)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9s8oZp8wkwhiz97rwarzvvos1pS8eqdSBynKQMmjEQFyrq0RJE22ATjNRVD5Fv5DQc9S7KwfiYXg5fn2L2KOtRqjYlv6mJ0VPnhAao3ljhf-YzWC7znlOPSINpceNVhJGjXnyO8dDPB-xr2XYxopPT12h0rEtY_vNmYU7-vqA4slCy6umSSPEsg..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐

---

### Level 2 子主题 1.2：SDD vs 传统开发

#### Level 3 知识点 1.2.1：SDD vs TDD

📖 **核心概念**：
SDD 与 TDD 的核心区别：TDD（测试驱动开发）是测试先行，验证代码行为；SDD 是规范先行，定义系统约束。TDD 关注"代码是否正确"，SDD 关注"代码是否符合规范"。最佳实践是 SDD + TDD 结合使用：先用 SDD 定义规范，再用 TDD 验证实现。

❓ **常见面试题**：
1. SDD 与 TDD 有什么区别？
2. SDD 和 TDD 可以结合使用吗？如何结合？

✅ **参考答案要点**：
- TDD：测试先行，验证代码行为
- SDD：规范先行，定义系统约束
- 区别：TDD 关注"是否正确"，SDD 关注"是否符合规范"
- 结合：先用 SDD 定义规范，再用 TDD 验证实现

🔗 **关联文章**：
- [SDD 编程:AI 时代的规范驱动开发 - 编程广角镜 (2026-02-05)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9NPXG1-WQMwmig8sJqUhr9pHgIhqWeiEZ8eD6FdNrr8klalNNYWkKopKNWg9LWd968SmX3wG6zx-buZLzJWRuVp8_GJEQcvrSfJn0nMfamf-NucpRi7fgc5VltwzZcBbpzn4HRWyrp1AaR1vma_tKrXKid3Who3WN8QKsw-bwd8SFW6cwuUnkdA..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐

---

#### Level 3 知识点 1.2.2：SDD 工具生态

📖 **核心概念**：
SDD 的主要工具包括：Spec Kit（GitHub 推出的规范驱动开发工具包）、Superpowers（规范生成与验证框架）、Speckit（结构化规范编写工具）。这些工具帮助开发者编写可执行的规范，并自动验证代码是否符合规范。但目前的工具生态还不够成熟，需要融合多个工具的能力。

❓ **常见面试题**：
1. 列举 3 个 SDD 相关工具。
2. 当前 SDD 工具生态存在什么问题？

✅ **参考答案要点**：
- 工具 1：Spec Kit（GitHub 出品）
- 工具 2：Superpowers（规范生成与验证）
- 工具 3：Speckit（结构化规范编写）
- 问题：工具生态不成熟，没有直接上手即用的完整框架
- 建议：融合 Speckit 和 Superpowers 的能力

🔗 **关联文章**：
- [SDD 开发框架汇总 - AI 大模型情报局](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9L3eX0P-P2kZx2K3yn9El-FMr8BUyD2wLG1NE0_vKlM_m-wMRKXDh2CKv9VfSHcuAe7qcW-pf-fDVy0kioNQKEy1A7jszH4qkzRdizVk7kVHid1JvsCfa_uNcmzND1lHtsWO_Ljzb6zuaMFXilTtrpXpYcop89IsDZaAKi8yeaWfYl_Q5RRZQjg..&type=2&query=SDD+开发)
- [拥抱 SDD 规范驱动开发但 Spec Kit 并非银弹 - AI 大模型情报局](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9L3eX0P-P2kZx2K3yn9El-FMr8BUyD2wLG1NE0_vKlM_m-wMRKXDh2P4kcuF34enfms-Zov4aRYUkpg1fn3daxJ6XytEKujNIAp12I_WCkbl4CK0mzlBFYUWbOfRQn8ileYyc97gzpGk0V_gVORiknlwUTB-LANPCU-uVrIoyPCRj3x9Nw6p-Fg..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐

---

### Level 2 子主题 1.3：SDD 黄金原则

#### Level 3 知识点 1.3.1：SDD 黄金 16 条原则（精选）

📖 **核心概念**：
SDD 黄金 16 条原则是 Vibe Coding 时代 SDD 开发的核心指南。精选 5 条：1) 规范先行，代码后置；2) 规范必须是可执行的；3) 验收标准必须量化；4) 规范即文档，文档即规范；5) 让 AI"消失"，让规范可见。这些原则确保 SDD 落地有效，真正可控、可复现、可规模化。

❓ **常见面试题**：
1. 列举 SDD 黄金 16 条原则中的 5 条。
2. 为什么说"规范必须是可执行的"？

✅ **参考答案要点**：
- 原则 1：规范先行，代码后置
- 原则 2：规范必须是可执行的（能自动验证）
- 原则 3：验收标准必须量化（可测量）
- 原则 4：规范即文档，文档即规范（一致性）
- 原则 5：让 AI"消失"，让规范可见（关注规范而非 AI）
- 价值：真正可控、可复现、可规模化

🔗 **关联文章**：
- [Vibe Coding 时代 SDD 开发的黄金 16 条原则 - AGI 知路 (2026-02-25)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9tj9LWJTfXH_YdKvwISn_0OEImQD998Dlqn3Jx5Jee_KBAW8xCRjLX8VYnKa_oX3OYxshFZDbQOVwgzg-U19W-FoAhFL0NZbRyNsQykyH5BEoUop9kIKDNDOLgMPhK-vlkU6E9ZfdFr_EMEyKJgP4IK_pqTLEX0CBSfzfHCbr48CFW6cwuUnkdA..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐⭐

---

#### Level 3 知识点 1.3.2：高质量规范示例

📖 **核心概念**：
高质量规范必须包含：功能需求（做什么）、约束条件（边界条件）、验收标准（如何验证）、接口定义（输入输出）。规范必须是结构化的、可执行的、量化的。好的规范能让 AI 生成符合预期的代码，减少迭代次数。

❓ **常见面试题**：
1. 高质量规范必须包含哪些要素？
2. 写出一个用户登录的 SDD 规范。

✅ **参考答案要点**：
- 要素 1：功能需求（做什么）
- 要素 2：约束条件（边界条件、性能要求）
- 要素 3：验收标准（如何验证，必须量化）
- 要素 4：接口定义（输入输出）
- 关键：结构化、可执行、量化

💻 **代码示例**：
```yaml
specification:
  name: 用户登录
  functional_requirements:
    - 支持邮箱/手机号登录
    - 登录失败 5 次锁定 30 分钟
  constraints:
    - 响应时间 < 500ms (P95)
    - 密码加密：bcrypt
  acceptance_criteria:
    - 正确凭证 100% 登录成功
    - 错误凭证返回明确错误码
  interface:
    input:
      - credential: string (email or phone)
      - password: string
    output:
      - success: boolean
      - token: string (if success)
      - error_code: string (if failed)
```

🔗 **关联文章**：
- [麻辣小龙虾公司 SDD 开发范式实战 - 健哥有道 (2026-03-11)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9DK9dmMkM41XQ2_CghYTGlPTjdL2y9PQCSWPdjmWFXnHbxjI94_v7uD4a0sGqtOiYKjXVXRr-820fUyZAGDZt4f048tkeoA9dX1MSU9J9mXtXqbEw90zRyQw3pN4S5j6_KW1d9kOrrOPc12SEyD33HQgtqxDE9fToq-5G1ferj1-rCDCayYmfpA..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐

---

## Level 1 主题二：SDD 实战应用

### Level 2 子主题 2.1：SDD 落地实践

#### Level 3 知识点 2.1.1：SDD 在生产环境的落地

📖 **核心概念**：
SDD 在生产环境的落地实践包括：1) 从简单模块开始（如 API 接口）；2) 建立规范模板库（减少重复工作）；3) 集成 CI/CD（自动验证规范）；4) 团队培训（统一规范编写标准）。关键是要循序渐进，不要一开始就追求完美规范。

❓ **常见面试题**：
1. 如何在生产环境落地 SDD？
2. SDD 落地过程中可能遇到哪些挑战？

✅ **参考答案要点**：
- 步骤 1：从简单模块开始（API 接口、工具函数）
- 步骤 2：建立规范模板库（减少重复工作）
- 步骤 3：集成 CI/CD（自动验证规范）
- 步骤 4：团队培训（统一规范编写标准）
- 挑战：1) 规范编写成本高；2) 团队习惯改变；3) 工具支持不足

🔗 **关联文章**：
- [规范驱动开发 (SDD) 在生产环境下的落地实践 - 毕方教练团](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9HzNntUEmMCq2AZEQmaLhMQAvZqpTa9wgQnFsGoH5fan2jYC-IuXMDiaoOV-fG6c0vpIbDlQvu9YyVb-zI1vHZ7XAT7eYMEK7iVcnOWrI4Tkj7w8SjHNM3y--XuyHLbKm0JV1F0jmV7flsREdE-KMCxcjbZefqa3zrvtyMsfclucCn9lOoZLP2Q..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐⭐

---

#### Level 3 知识点 2.1.2：SDD 开发者角色转变

📖 **核心概念**：
SDD 让开发者角色发生转变：从"写代码"转向"写规范"，从"调试代码"转向"调试规范"，从"实现功能"转向"定义约束"。SDD 不是让开发者"消失"，而是让开发者的工作向上迁移——更关注"为什么"（Why）而非"怎么做"（How）。

❓ **常见面试题**：
1. SDD 如何改变开发者角色？
2. 为什么说 SDD 让开发者的工作"向上迁移"？

✅ **参考答案要点**：
- 转变 1：写代码 → 写规范
- 转变 2：调试代码 → 调试规范
- 转变 3：实现功能 → 定义约束
- 向上迁移：从"怎么做"（How）转向"为什么"（Why）
- 价值：让 AI 处理实现细节，人类专注系统设计

🔗 **关联文章**：
- [麻辣小龙虾公司 SDD 开发范式实战 - 健哥有道 (2026-03-11)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9DK9dmMkM41XQ2_CghYTGlPTjdL2y9PQCSWPdjmWFXnHbxjI94_v7uD4a0sGqtOiYKjXVXRr-820fUyZAGDZt4f048tkeoA9dX1MSU9J9mXtXqbEw90zRyQw3pN4S5j6_KW1d9kOrrOPc12SEyD33HQgtqxDE9fToq-5G1ferj1-rCDCayYmfpA..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐

---

### Level 2 子主题 2.2：SDD 与 AI 协作

#### Level 3 知识点 2.2.1：SDD 本质：人与 AI 协作的可靠性

📖 **核心概念**：
SDD 的目的并非让开发更繁琐，而是让人与 AI 协作更具可靠性、更可预测。通过规范作为"中间语言"，人类表达意图，AI 生成代码，规范作为验证标准。这解决了 Vibe Coding 中"不知道代码怎么跑起来"的问题，让 AI 生成的代码可控、可解释、可维护。

❓ **常见面试题**：
1. SDD 的本质是什么？
2. SDD 如何提高人与 AI 协作的可靠性？

✅ **参考答案要点**：
- 本质：人与 AI 协作的可靠性机制
- 方法：规范作为"中间语言"
- 流程：人类表达意图 → 规范 → AI 生成代码 → 规范验证
- 价值：可控、可预测、可解释、可维护

🔗 **关联文章**：
- [AGI SDD 规范驱动开发：本质到底是什么？- JeffckyShare (2026-03-02)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9xR1Ubita78zeUer-cpizM0O4BcTBjWzRGB5I5jcIg3nqqhOaKQa4LJGMGebcV4mNNjMNPia9gPr5Ir_mvH_mBqaRk8aHTKwydeZzIuNMRf2B_exskxtMcTe_GJsKb1DbIjinh-BbatIE9oh9z6JVX0RYnVw2NEr_N4yA3w57_Vm00NVofL2iDw..&type=2&query=SDD+开发)

📊 **难度标注**：⭐⭐⭐

---

## 📊 面试题汇总

### 基础题（⭐）
1. 什么是 SDD？它的核心思想是什么？
2. SDD 与 TDD 有什么区别？
3. SDD 解决了 Vibe Coding 的哪些问题？
4. 高质量规范必须包含哪些要素？

### 进阶题（⭐⭐）
5. 描述 SDD 的完整工作流。
6. SDD vs TDD，如何结合使用？
7. 列举 3 个 SDD 相关工具。
8. SDD 黄金 16 条原则中的 5 条是什么？
9. SDD 如何改变开发者角色？
10. SDD 如何提高人与 AI 协作的可靠性？

### 高级题（⭐⭐⭐）
11. 如何在生产环境落地 SDD？
12. SDD 落地过程中可能遇到哪些挑战？如何解决？
13. 为什么说 SDD 是 AI 时代的软件工程新范式？

---

## 📈 学习建议

1. **入门**：理解 SDD 核心概念，对比 TDD
2. **实践**：编写 3-5 个规范示例（API、函数、模块）
3. **工具**：尝试 Spec Kit 或类似工具
4. **落地**：在小项目中应用 SDD 工作流
5. **进阶**：结合 Vibe Coding，理解从 Vibe 到 SDD 的演进

---

## 🔗 与 Vibe Coding 的关系

```
Vibe Coding (直觉驱动)
    ↓ 发现问题：不可控、不可预测
SDD (规范驱动)
    ↓ 解决问题：规范作为约束
Harness Engineering (系统驾驭)
```

- Vibe Coding：快速原型，但不可控
- SDD：规范先行，确保可控
- Harness Engineering：系统驾驭，工程化落地

---

**生成时间**：2026-03-23  
**文章来源**：10 篇 SDD 微信文章  
**下一步**：阅读 `memory/optimized-cursor.md` 学习 AI 编辑器对比
