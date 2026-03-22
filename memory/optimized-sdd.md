# SDD 规范驱动开发 专题优化

## Level 1: SDD 核心概念与范式

### Level 2: SDD 定义与起源

#### Level 3: 什么是 SDD 规范驱动开发 ⭐

**📖 核心概念**
SDD（Specification-Driven Development，规范驱动开发）是 AI 时代的软件工程新范式。核心思想：先写规范（Specification），再让 AI 生成代码。规范是唯一的"事实来源"，代码是规范的自动化表达。SDD 不是对 AI 能力的否定，而是对 AI 使用方式的系统性升级。

**❓ 常见面试题**
1. SDD 与 Vibe Coding 的本质区别是什么？
2. 为什么 AI 时代需要 SDD？

**✅ 参考答案要点**
- Vibe Coding：直觉驱动，代码不可控
- SDD：规范先行，代码可预测
- 核心价值：解决 AI 项目 67% 失败率问题
- 范式转变：从"写代码"到"写规范"

**🔗 关联文章**
- [SDD 编程:AI 时代的规范驱动开发 - 编程广角镜](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9NPXG1-WQMwmig8sJqUhr9pHgIhqWeiEZ8eD6FdNrr8klalNNYWkKopKNWg9LWd968SmX3wG6zx-buZLzJWRuVp8_GJEQcvrSfJn0nMfamf-NucpRi7fgc5VltwzZcBbpzn4HRWyrp1AaR1vma_tKrXKid3Who3WN8QKsw-bwd8SFW6cwuUnkdA..&type=2&query=SDD+开发)
- [AI 时代的新开发模式:SDD 规范驱动开发是什么 - ForeverPx](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9EOJRqBMnOlgrTVBnqK0BP9j1o2EcHdzptepWO62xbMM882kjBSPe8f77VYtz3iRuWxk0IVVNoyNkP9XUeK8-yv8mZHZpXYF__InARKEFEm2FNAooshwHfy8G4jGRqR3iGtO8ZSw3d4WBpsiuIn69aqMr2MTLIfuXyXCpETALffSrCDCayYmfpA..&type=2&query=SDD+开发)

---

#### Level 3: SDD 与 TDD 的区别 ⭐⭐

**📖 核心概念**
SDD（规范驱动开发）与 TDD（测试驱动开发）的核心区别：TDD 通过测试用例驱动代码，关注"代码是否正确"；SDD 通过规范文档驱动代码，关注"代码是否符合设计"。TDD 的测试是代码，SDD 的规范是自然语言 + 结构化约束。

**❓ 常见面试题**
1. SDD 与 TDD 的核心区别是什么？
2. SDD 能否替代 TDD？

**✅ 参考答案要点**
- TDD：测试先行，验证代码行为
- SDD：规范先行，定义系统约束
- 关系：SDD 可包含 TDD，规范中定义验收测试
- 最佳实践：SDD + TDD 结合使用

**🔗 关联文章**
- [Vibe Coding 时代 SDD 开发的黄金 16 条原则 - AGI 知路](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9tj9LWJTfXH_YdKvwISn_0OEImQD998Dlqn3Jx5Jee_KBAW8xCRjLX8VYnKa_oX3OYxshFZDbQOVwgzg-U19W-FoAhFL0NZbRyNsQykyH5BEoUop9kIKDNDOLgMPhK-vlkU6E9ZfdFr_EMEyKJgP4IK_pqTLEX0CBSfzfHCbr48CFW6cwuUnkdA..&type=2&query=SDD+开发)

---

### Level 2: SDD 核心工作流

#### Level 3: SDD 三阶段工作流 ⭐⭐

**📖 核心概念**
SDD 工作流分为三阶段：(1) 编写规范：定义功能需求、约束条件、验收标准、接口定义；(2) AI 生成代码：基于规范生成实现、自动生成测试用例、输出实现说明；(3) 验证与迭代：运行验收测试、对比规范与实际、修正规范或代码。

**❓ 常见面试题**
1. 描述 SDD 的完整工作流
2. SDD 工作流中 AI 的角色是什么？

**✅ 参考答案要点**
```
1. 编写规范 (Spec)
   ├── 功能需求（做什么）
   ├── 约束条件（边界条件）
   ├── 验收标准（如何验证）
   └── 接口定义（输入输出）

2. AI 生成代码
   ├── 基于规范生成实现
   ├── 自动生成测试用例
   └── 输出实现说明

3. 验证与迭代
   ├── 运行验收测试
   ├── 对比规范与实际
   └── 修正规范或代码
```

**🔗 关联文章**
- [规范驱动开发 (SDD) 在生产环境下的落地实践 - 毕方教练团](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9HzNntUEmMCq2AZEQmaLhMQAvZqpTa9wgQnFsGoH5fan2jYC-IuXMDiaoOV-fG6c0vpIbDlQvu9YyVb-zI1vHZ7XAT7eYMEK7iVcnOWrI4Tkj7w8SjHNM3y--XuyHLbKm0JV1F0jmV7flsREdE-KMCxcjbZefqa3zrvtyMsfclucCn9lOoZLP2Q..&type=2&query=SDD+开发)

---

#### Level 3: 高质量规范的编写原则 ⭐⭐⭐

**📖 核心概念**
高质量规范的核心原则（黄金 16 条精选）：(1) 规范先行，代码后置；(2) 规范必须是可执行的；(3) 验收标准必须量化；(4) 规范即文档，文档即规范；(5) 让 AI"消失"，让规范可见。规范应该明确、可验证、无歧义。

**❓ 常见面试题**
1. 如何编写高质量的 SDD 规范？
2. 规范的"可执行性"如何体现？

**✅ 参考答案要点**
- 明确性：避免模糊描述，使用量化指标
- 可执行性：规范可直接转换为测试用例
- 完整性：覆盖功能、约束、接口、验收标准
- 可维护性：规范版本化，与代码同步更新

**💻 代码示例**
```yaml
# 规范示例：用户登录功能
specification:
  name: 用户登录
  version: 1.0
  
  functional_requirements:
    - 支持邮箱/手机号登录
    - 支持密码/验证码登录
    - 登录失败 5 次锁定 30 分钟
  
  constraints:
    - 响应时间 < 500ms (P95)
    - 并发支持 > 1000 QPS
    - 密码加密：bcrypt
  
  acceptance_criteria:
    - 正确凭证 100% 登录成功
    - 错误凭证返回明确错误码
    - 锁定期间拒绝登录请求
  
  interfaces:
    - POST /api/login
      request: {identifier, credential}
      response: {token, expires_at}
```

---

### Level 2: SDD 工具生态

#### Level 3: SDD 工具对比 ⭐⭐

**📖 核心概念**
主流 SDD 工具包括：Spec Kit（GitHub 推出的规范驱动开发工具包）、Superpowers（规范生成与验证框架）、Speckit（结构化规范编写工具）。目前尚无成熟的一站式解决方案，建议融合 Speckit 和 Superpowers 能力。

**❓ 常见面试题**
1. 主流 SDD 工具有哪些？
2. 如何选择 SDD 工具？

**✅ 参考答案要点**
- Spec Kit：GitHub 官方，生态集成好
- Superpowers：规范验证能力强
- Speckit：结构化规范编写
- 选型建议：根据团队技术栈选择，可组合使用

**🔗 关联文章**
- [SDD 开发框架汇总 - AI 大模型情报局](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9L3eX0P-P2kZx2K3yn9El-FMr8BUyD2wLG1NE0_vKlM_m-wMRKXDh2CKv9VfSHcuAe7qcW-pf-fDVy0kioNQKEy1A7jszH4qkzRdizVk7kVHid1JvsCfa_uNcmzND1lHtsWO_Ljzb6zuaMFXilTtrpXpYcop89IsDZaAKi8yeaWfYl_Q5RRZQjg..&type=2&query=SDD+开发)

---

## Level 1: SDD 实战应用

### Level 2: SDD 生产环境落地

#### Level 3: SDD 在企业中的落地实践 ⭐⭐⭐

**📖 核心概念**
SDD 在生产环境的落地关键：(1) 规范模板化：建立团队规范模板库；(2) 流程集成：将规范审查纳入 Code Review；(3) 工具链：规范→代码→测试自动化；(4) 文化转变：从"代码优先"到"规范优先"。成功案例显示，SDD 可将 AI 项目成功率从 33% 提升至 75%。

**❓ 常见面试题**
1. SDD 如何在团队中落地？
2. SDD 落地的主要阻力是什么？

**✅ 参考答案要点**
- 落地步骤：模板化→流程化→自动化→文化化
- 主要阻力：开发者习惯转变、规范编写成本
- 解决方案：提供模板、工具支持、渐进式采用
- 收益：代码质量提升、维护成本降低、新人上手快

**🔗 关联文章**
- [麻辣小龙虾公司 SDD 开发范式实战 - 健哥有道](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9DK9dmMkM41XQ2_CghYTGlPTjdL2y9PQCSWPdjmWFXnHbxjI94_v7uD4a0sGqtOiYKjXVXRr-820fUyZAGDZt4f048tkeoA9dX1MSU9J9mXtXqbEw90zRyQw3pN4S5j6_KW1d9kOrrOPc12SEyD33HQgtqxDE9fToq-5G1ferj1-rCDCayYmfpA..&type=2&query=SDD+开发)

---

#### Level 3: SDD 规范示例：API 开发 ⭐⭐⭐

**📖 核心概念**
API 开发的 SDD 规范应包含：接口定义（URL、方法、参数）、业务逻辑（处理流程、边界条件）、错误处理（错误码、重试策略）、性能要求（延迟、吞吐）、安全要求（认证、限流）。规范应足够详细，使 AI 能生成完整实现。

**❓ 常见面试题**
1. 如何为 API 开发编写 SDD 规范？
2. 规范详细程度如何把握？

**✅ 参考答案要点**
- 接口定义：RESTful 规范，OpenAPI 格式
- 业务逻辑：流程图 + 文字描述
- 错误处理：完整错误码表
- 详细程度：AI 能独立实现为准

**💻 代码示例**
```yaml
# API 规范示例
api:
  name: 创建订单
  method: POST
  path: /api/orders
  
  request:
    body:
      user_id: integer, required
      items: array, required
        - product_id: integer
          quantity: integer
      payment_method: enum[alipay, wechat, card]
    
    validation:
      - items 不能为空
      - 单个订单最多 10 件商品
      - 用户必须存在
  
  response:
    success:
      status: 201
      body:
        order_id: string
        total_amount: decimal
        status: enum[pending, paid, cancelled]
    error:
      - 400: 参数验证失败
      - 404: 用户不存在
      - 409: 库存不足
  
  business_logic:
    - 检查用户存在
    - 检查库存充足
    - 计算总价（含优惠）
    - 扣减库存
    - 创建订单记录
    - 发送确认通知
  
  performance:
    - P95 延迟 < 200ms
    - 支持 500 QPS
  
  security:
    - JWT 认证
    - 限流：100 req/min/user
```

---

### Level 2: SDD 与 AI 协作

#### Level 3: 让 AI"消失"的规范设计 ⭐⭐⭐

**📖 核心概念**
SDD 的核心理念是"让 AI 消失，让规范可见"。规范应足够清晰，使 AI 生成过程透明化。关键方法：(1) 规范即文档：规范可直接作为技术文档；(2) 规范可追溯：代码变更可追溯到规范变更；(3) 规范可验证：验收测试自动生成。

**❓ 常见面试题**
1. 如何理解"让 AI 消失"？
2. 规范如何实现可追溯性？

**✅ 参考答案要点**
- AI 消失：关注点从 AI 转移到规范质量
- 规范可见：规范是唯一的"事实来源"
- 可追溯性：规范版本→代码版本→测试版本
- 实现方式：规范 ID 嵌入代码注释

**🔗 关联文章**
- [AGI SDD 规范驱动开发：本质到底是什么？- JeffckyShare](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9xR1Ubita78zeUer-cpizM0O4BcTBjWzRGB5I5jcIg3nqqhOaKQa4LJGMGebcV4mNNjMNPia9gPr5Ir_mvH_mBqaRk8aHTKwydeZzIuNMRf2B_exskxtMcTe_GJsKb1DbIjinh-BbatIE9oh9z6JVX0RYnVw2NEr_N4yA3w57_Vm00NVofL2iDw..&type=2&query=SDD+开发)

---

## Level 1: SDD 面试考点汇总

### Level 2: 基础概念题

#### Level 3: SDD 定义与价值 ⭐
- 定义：规范驱动开发，规范是唯一事实来源
- 价值：解决 AI 项目高失败率问题
- 核心：先写规范，再生成代码

### Level 2: 工作流题

#### Level 3: SDD 三阶段 ⭐⭐
- 编写规范：需求、约束、验收、接口
- AI 生成：代码、测试、说明
- 验证迭代：测试、对比、修正

### Level 2: 实践应用题

#### Level 3: SDD 落地实践 ⭐⭐⭐
- 模板化：建立规范模板库
- 流程化：规范审查纳入 Code Review
- 自动化：规范→代码→测试
- 文化化：从代码优先到规范优先

### Level 2: 规范编写题

#### Level 3: 高质量规范原则 ⭐⭐
- 明确性：量化指标，避免模糊
- 可执行性：可直接转换为测试
- 完整性：覆盖功能、约束、接口
- 可维护性：版本化，与代码同步

---

**生成时间**: 2026-03-22  
**文章来源**: 10 篇微信公众号精选  
**优化级别**: 三级知识结构 (主题→子主题→知识点)
