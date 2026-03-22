"""
RAG 示例 - 基于 LangChain 的文档问答系统
功能：上传文档，构建向量索引，支持自然语言问答
"""

import os
from typing import List, Dict
from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 配置 API Key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

class SimpleRAG:
    """简单的 RAG 系统"""
    
    def __init__(
        self,
        docs_dir: str = "./docs",
        persist_dir: str = "./chroma_db",
        model_name: str = "gpt-4",
        embedding_model: str = "text-embedding-3-small"
    ):
        """
        初始化 RAG 系统
        
        Args:
            docs_dir: 文档目录
            persist_dir: 向量数据库持久化目录
            model_name: LLM 模型名称
            embedding_model: Embedding 模型名称
        """
        self.docs_dir = docs_dir
        self.persist_dir = persist_dir
        
        # 初始化 Embedding
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        
        # 加载和处理文档
        self.documents = self._load_documents()
        self.chunks = self._split_documents(self.documents)
        
        # 创建或加载向量库
        self.vectorstore = self._create_vectorstore()
        
        # 初始化 LLM 和 QA Chain
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        self.qa_chain = self._create_qa_chain()
    
    def _load_documents(self) -> List:
        """加载文档"""
        print(f"📚 从 {self.docs_dir} 加载文档...")
        
        loaders = []
        
        # 加载 Markdown 文件
        if os.path.exists(self.docs_dir):
            md_loader = DirectoryLoader(
                self.docs_dir,
                glob="**/*.md",
                loader_cls=TextLoader,
                loader_kwargs={"encoding": "utf-8"}
            )
            loaders.append(md_loader)
            
            # 加载 PDF 文件
            pdf_loader = DirectoryLoader(
                self.docs_dir,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader
            )
            loaders.append(pdf_loader)
        
        # 加载所有文档
        documents = []
        for loader in loaders:
            documents.extend(loader.load())
        
        print(f"✅ 加载了 {len(documents)} 个文档")
        return documents
    
    def _split_documents(self, documents: List, chunk_size: int = 500, chunk_overlap: int = 50) -> List:
        """分割文档"""
        print(f"✂️  分割文档...")
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", ""]
        )
        
        chunks = splitter.split_documents(documents)
        print(f"✅ 分割为 {len(chunks)} 个片段")
        return chunks
    
    def _create_vectorstore(self) -> Chroma:
        """创建向量数据库"""
        print(f"🔧 创建向量索引...")
        
        # 检查是否有持久化的数据
        if os.path.exists(self.persist_dir):
            print(f"📂 加载已有的向量库...")
            vectorstore = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embeddings
            )
        else:
            print(f"✨ 创建新的向量库...")
            vectorstore = Chroma.from_documents(
                documents=self.chunks,
                embedding=self.embeddings,
                persist_directory=self.persist_dir
            )
            vectorstore.persist()
        
        print(f"✅ 向量库就绪")
        return vectorstore
    
    def _create_qa_chain(self) -> RetrievalQA:
        """创建 QA Chain"""
        # 自定义 Prompt
        prompt_template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。
        
上下文：
{context}

问题：{question}

有用的回答："""
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # 创建 QA Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 3}  # 检索 top 3 相关文档
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )
        
        return qa_chain
    
    def query(self, question: str) -> Dict:
        """
        查询问题
        
        Args:
            question: 问题文本
            
        Returns:
            包含答案和来源的字典
        """
        result = self.qa_chain({"query": question})
        
        return {
            "question": question,
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:200],  # 只显示前 200 字
                    "metadata": doc.metadata
                }
                for doc in result["source_documents"]
            ]
        }
    
    def add_documents(self, new_docs: List):
        """添加新文档"""
        print(f"📥 添加 {len(new_docs)} 个新文档...")
        
        # 分割新文档
        new_chunks = self._split_documents(new_docs)
        
        # 添加到向量库
        self.vectorstore.add_documents(new_chunks)
        
        print(f"✅ 添加完成")


# 使用示例
if __name__ == "__main__":
    # 初始化 RAG 系统
    rag = SimpleRAG(
        docs_dir="./docs",
        persist_dir="./chroma_db"
    )
    
    # 交互式问答
    print("\n🤖 RAG 问答系统已就绪！输入'quit'退出\n")
    
    while True:
        question = input("你：")
        if question.lower() == "quit":
            break
        
        # 查询
        result = rag.query(question)
        
        # 输出结果
        print(f"\n助手：{result['answer']}\n")
        
        # 显示来源
        if result["sources"]:
            print("📚 来源：")
            for i, source in enumerate(result["sources"], 1):
                print(f"{i}. {source['metadata'].get('source', 'Unknown')}")
                print(f"   {source['content']}...\n")

"""
使用示例：

1. 准备文档
   mkdir docs
   cp /path/to/your/*.md docs/

2. 运行系统
   python rag-demo.py

3. 提问
   你：什么是 Transformer？
   助手：Transformer 是一种基于自注意力机制的深度学习模型...
   
   📚 来源：
   1. docs/01-AIGC 基础.md
      Transformer 架构详解...
"""
