# RAG 系统实战 三级知识结构面试题

> 基于 10 篇微信文章整理的 RAG 知识体系  
> 更新时间：2026-03-23

---

## Level 1 主题一：RAG 核心架构

### Level 2 子主题 1.1：RAG 基础概念

#### Level 3 知识点 1.1.1：什么是 RAG

📖 **核心概念**：
RAG（Retrieval-Augmented Generation，检索增强生成）是一种将检索与生成结合的 AI 架构。核心流程：用户问题 → 检索相关文档 → 增强 Prompt → LLM 生成答案。RAG 解决了大模型幻觉问题，让 AI 回答基于事实依据，可追溯来源。

❓ **常见面试题**：
1. 什么是 RAG？它的核心流程是什么？
2. RAG 相比微调有什么优势？

✅ **参考答案要点**：
- 定义：检索增强生成，检索 + 生成结合
- 流程：问题 → 检索 → 增强 Prompt → 生成答案
- 优势：知识实时更新、幻觉少、成本低、可解释性高
- 适用：企业知识库、客服系统、文档问答

💻 **代码示例**：
```python
# 简单 RAG 流程
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

result = qa_chain({"query": "什么是 RAG？"})
print(result["result"])
print("来源:", result["source_documents"])
```

🔗 **关联文章**：
- [破解大模型幻觉!2026 最火 AI RAG 系统保姆级教程 - 天府 AI](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9weXCXtP-l4X2e4TtKXQMLZyh6GOGKADCku1_FVp-I_ddVRUgYtSXTR-ZCOwu6FojLQwIexmhLrEVjbpJ0eDQzjnaW41tMnSbek4-kga-k9jqPIDeuWoenYqfJcYGyyuCMdvSXHshvCBqDAZ5DqvfbuzqJo4GgK6rhjsCEE-IaNWAFV_3u-a3OQ..&type=2&query=RAG+系统实战)
- [RAG 实战 - 打造企业知识库问答系统 - 全栈生涯](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9q9K1FirE8Yc7E39Z-Rxe-ae9MgLsMdzc52Ec-YXKR7bexV92i1T_CITkDhOOLAib6jjib2sz4tAKJegRPCMZlJ_eYODoobAqvsBYjhXBwabHLLcqb1o24MIYK5YdYCabARWGYykW1w238I0CEWNFQwSgCajhyBOJ_OHuyxYX-BgCYioxHkzTmA..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐

---

#### Level 3 知识点 1.1.2：RAG 核心组件

📖 **核心概念**：
RAG 系统核心组件：1) 文档加载器（加载 PDF、Word、Markdown 等）；2) 文本分块器（RecursiveCharacterTextSplitter）；3) 向量化模型（OpenAI Embeddings、bge-m3）；4) 向量数据库（Chroma、FAISS、Milvus）；5) 检索器（相似性搜索、MMR）；6) LLM（GPT-4、Qwen 等）。

❓ **常见面试题**：
1. RAG 系统包含哪些核心组件？
2. 常用的向量数据库有哪些？

✅ **参考答案要点**：
- 组件 1：文档加载器（加载各种格式）
- 组件 2：文本分块器（分割文档）
- 组件 3：向量化模型（文本→向量）
- 组件 4：向量数据库（存储和检索）
- 组件 5：检索器（相似性搜索）
- 组件 6：LLM（生成答案）

🔗 **关联文章**：
- [企业级 RAG 本地知识库问答系统全链路实战 - 编程基础很重要](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9u9vEJz4K-8CD4_dkt3oa86i6uz8m6bOKviWgrlWixikLyHU0l74FMxYIpNf9xD5eJz6UwQcNxVHW1NSg2KzWxbz-AvyQOGy9xkkHFVVIBcSPYj4_Ls_FJlyPOfKBumXzm5_fUdd832xOos8XknBHpu82cWhbSInptb6Y3C7PNUGAFV_3u-a3OQ..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐

---

### Level 2 子主题 1.2：RAG 优化技巧

#### Level 3 知识点 1.2.1：混合检索策略

📖 **核心概念**：
混合检索（Hybrid Search）结合向量检索和关键词检索（BM25），提升检索准确率。实现方式：EnsembleRetriever，权重可调（如向量 0.7 + 关键词 0.3）。适用场景：专业术语多、需要精确匹配的文档。

❓ **常见面试题**：
1. 什么是混合检索？如何实现？
2. 混合检索的权重如何设置？

✅ **参考答案要点**：
- 定义：向量检索 + 关键词检索结合
- 实现：EnsembleRetriever，可调权重
- 权重：通常向量 0.7 + 关键词 0.3
- 适用：专业术语多、需要精确匹配

💻 **代码示例**：
```python
from langchain.retrievers import EnsembleRetriever

retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]  # 关键词 30% + 向量 70%
)
```

🔗 **关联文章**：
- [智能体准确率提升 200% 的 RAG 系统实战 - 慧测 (2026-03-17)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd99tk5DlC5UfpNZlUhTYE9976bWzG44qjgCqItuVja9FKlvbCviYK0sif-sBtOiuGtgPBOJWmS4j0jzxLDFf-vuWuCRhg-Db2BKJ0lUvllWvJdb0f5CjKjdbLwgIzP1KP1nR2E34ePMYOHdkqZtAFljgSbC6g_hlNP4MNfW-ik6HthWLv6O878UA..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐⭐

---

#### Level 3 知识点 1.2.2：多模态 RAG

📖 **核心概念**：
多模态 RAG 结合文本和图像检索，使用 LLaVA 等多模态模型。核心流程：提取文档中的图像 → 生成图像描述 → 向量化 → 联合检索。适用场景：技术文档（含架构图）、产品手册（含产品图）、医疗影像报告。

❓ **常见面试题**：
1. 什么是多模态 RAG？
2. 多模态 RAG 的适用场景有哪些？

✅ **参考答案要点**：
- 定义：结合文本和图像的 RAG 系统
- 模型：LLaVA 等多模态模型
- 流程：提取图像 → 生成描述 → 联合检索
- 场景：技术文档、产品手册、医疗影像

🔗 **关联文章**：
- [【深度解析】多模态 RAG 系统实战:LLaVA+LangChain - 出家二少 (2026-03-13)](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9KVqNUmyTwQCYACZoBGOihc5chcOn_gC7pBILP9yzl0fBno6WeTmuArDc1D6Xsk9tI9m5sm8Y47J9j6Vmfd_zEABjbKfTLTFfWV6M7ykgcj-4n3nTuB-JQaEMdHEvM07doWnvpf4QDC4m35XwBfTr4HAkDuS3q8c7ECvTM9x9S18HpHkoPMgL3A..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐⭐⭐

---

## Level 1 主题二：RAG 实战应用

### Level 2 子主题 2.1：企业级 RAG 系统

#### Level 3 知识点 2.1.1：HR 制度智能问答系统

📖 **核心概念**：
HR 制度智能问答是 RAG 的典型应用场景。实现流程：1) 加载《人事管理制度.docx》；2) 分块向量化；3) 员工自然语言提问；4) 检索相关制度条款；5) AI 生成答案并引用原文。效果：减少 HR 重复工作，提高员工自助服务效率。

❓ **常见面试题**：
1. 如何用 RAG 实现 HR 制度问答系统？
2. RAG 在企业知识库的应用价值是什么？

✅ **参考答案要点**：
- 流程：加载文档 → 分块 → 向量化 → 检索 → 生成
- 价值：减少重复工作，提高自助服务效率
- 关键：文档质量、检索准确率、答案可追溯
- 效果：人工客服工作量减少 60%+

🔗 **关联文章**：
- [AI-07 实战:Naive RAG 实现公司 HR 制度智能问答系统 - 码上大模型](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9yulGhJvtd4DklVqM2FyOuIKOQGzbfehVINsXL83zns9aNT3TfaxQoYhdb9IQxvTcZ-EjSpMFIVQI45luxp9-N05xIaxP2dU8OZseSKYokzbK8QTvRGvlc9PvPh4ndZTWSA8fXxWvQVXpHgl0cpxXsSVGTwvybWIWGhX50Axsxkw5eBgmN3LoYQ..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐⭐

---

#### Level 3 知识点 2.1.2：RAG 系统安全防御

📖 **核心概念**：
RAG 系统面临安全威胁：1) PoisonedRAG（投毒攻击）；2) 提示注入；3) 数据泄露。防御策略：1) 文档来源验证；2) 输入过滤；3) 输出审查；4) 访问控制。安全是 RAG 生产落地的关键考量。

❓ **常见面试题**：
1. RAG 系统面临哪些安全威胁？
2. 如何防御 RAG 系统的安全攻击？

✅ **参考答案要点**：
- 威胁 1：PoisonedRAG（投毒攻击）
- 威胁 2：提示注入
- 威胁 3：数据泄露
- 防御：文档验证、输入过滤、输出审查、访问控制

🔗 **关联文章**：
- [RAG 系统安全威胁全景：从学术前沿到实战防御 - Sidereus](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7g9FB5Jdk0bq5g3DFVrJw2zZZ2YjZrZUVqXa8Fplpd9yhHRFu01mQKGqviMrD_QFMcar83IrFDQyOa8vJbKm0UvetG5lmvvK83L46RGZlrrYgsolvMTwQp3WSDo8TbXMw5lN_CAaMymZHfHAu8TOW4DBIxUdHZaFWDNSnnc6tXr6Hbo_3Y3fyXw1hAF7GT0LT-xSZT7kcLT8zx2Xw_0KUDf3q8uRDTfkw..&type=2&query=RAG+系统实战)

📊 **难度标注**：⭐⭐⭐

---

## 📊 面试题汇总

### 基础题（⭐）
1. 什么是 RAG？它的核心流程是什么？
2. RAG 系统包含哪些核心组件？
3. RAG 相比微调有什么优势？

### 进阶题（⭐⭐）
4. 什么是混合检索？如何实现？
5. 如何用 RAG 实现 HR 制度问答系统？
6. 多模态 RAG 的适用场景有哪些？

### 高级题（⭐⭐⭐）
7. RAG 系统面临哪些安全威胁？如何防御？
8. 多模态 RAG 的技术实现原理是什么？

---

**生成时间**：2026-03-23  
**文章来源**：10 篇 RAG 微信文章
