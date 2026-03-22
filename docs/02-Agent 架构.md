# 02-Agent 架构

> AI Agent 设计模式、工具调用、记忆与规划、多 Agent 协作

---

## 2.1 什么是 AI Agent

**定义**：AI Agent 是能够感知环境、进行推理、执行行动以实现目标的智能系统。

### 核心公式

```
Agent = LLM + 规划 + 记忆 + 工具使用
```

### Agent 与传统 API 的区别

| 传统 API | AI Agent |
|---------|----------|
| 固定输入输出 | 灵活理解自然语言 |
| 预定义逻辑 | 自主推理决策 |
| 单一功能 | 多步骤任务编排 |
| 被动调用 | 主动规划执行 |

---

## 2.2 Agent 核心组件

### 1. 规划 (Planning)

**任务分解**：
```
目标："分析某公司财务状况"
  ↓
1. 搜索公司最新财报
2. 提取关键财务指标
3. 计算增长率、利润率
4. 与同行业对比
5. 生成分析报告
```

**常见方法**：

#### Chain of Thought (CoT)
```
问题 → 思考步骤 1 → 思考步骤 2 → ... → 答案
```

**示例**：
```
Q: 小明有 5 个苹果，给了小红 2 个，又买了 3 个，现在有几个？
A: 让我们一步步思考：
   1. 初始：5 个苹果
   2. 给小红后：5 - 2 = 3 个
   3. 买了 3 个后：3 + 3 = 6 个
   答案：6 个
```

#### Tree of Thoughts (ToT)
```
        初始问题
       /    |    \
   思路 1  思路 2  思路 3
    /  \    /  \    /  \
   ...  ... ...  ... ...  ...
```

#### ReAct (Reason + Act)
```
Thought: 我需要先搜索...
Action: search[关键词]
Observation: 搜索结果...
Thought: 现在我需要...
Action: ...
```

### 2. 记忆 (Memory)

#### 分类

```
记忆
├── 短期记忆 (上下文窗口)
├── 长期记忆
│   ├── 程序性记忆 (技能)
│   └── 陈述性记忆 (事实)
│       ├──  episodic (经历)
│       └──  semantic (知识)
```

#### 实现方式

**1. 向量数据库**
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(embedding_function=embeddings, persist_directory="./chroma")

# 添加记忆
vectorstore.add_texts(["今天和用户讨论了 Agent 架构"])

# 检索记忆
results = vectorstore.similarity_search("Agent 相关讨论")
```

**2. 摘要压缩**
```python
def compress_memory(messages):
    summary = llm.generate(f"总结以下对话：{messages}")
    return summary
```

**3. 知识图谱**
```
用户 → 喜欢 → Python
用户 → 工作于 → AI 公司
项目 → 使用 → LangChain
```

### 3. 工具使用 (Tool Use)

#### Function Calling

**OpenAI 格式**：
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "搜索网络获取信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "搜索关键词"}
                },
                "required": ["query"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "今天天气如何？"}],
    tools=tools
)
```

#### 常见工具类型

| 工具类型 | 示例 |
|---------|------|
| 搜索 | Google Search、Bing API |
| 计算 | Wolfram Alpha、Python REPL |
| 代码执行 | Sandboxed Code Interpreter |
| API 调用 | REST API、GraphQL |
| 文件操作 | Read/Write、PDF 解析 |
| 数据库 | SQL Query、Vector DB |

---

## 2.3 主流 Agent 框架对比

### LangChain

**特点**：
- 生态最丰富
- 组件化设计
- 支持多种 LLM

**核心概念**：
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory

# Chain
chain = prompt | model | output_parser

# Agent
agent = create_openai_functions_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, memory=memory)
```

### AutoGen

**特点**：
- 多 Agent 协作
- 对话驱动
- 微软出品

**示例**：
```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

user_proxy.initiate_chat(assistant, message="写一个 Python 脚本计算斐波那契数列")
```

### CrewAI

**特点**：
- 角色分工
- 任务编排
- 基于 LangChain

**示例**：
```python
from crewai import Agent, Task, Crew

researcher = Agent(role='研究员', goal='深入研究主题', backstory='...')
writer = Agent(role='作家', goal='撰写高质量文章', backstory='...')

task1 = Task(description='研究 AI Agent 趋势', agent=researcher)
task2 = Task(description='撰写研究报告', agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = crew.kickoff()
```

### Dify

**特点**：
- 可视化编排
- 开箱即用
- 支持部署

---

## 2.4 Agent 设计模式

### 1. 单 Agent 模式

```
用户 → Agent → 工具 → 结果
```

**适用场景**：简单任务、快速原型

### 2. 多 Agent 协作

```
用户 → Orchestrator → Agent1 → 结果 1
                     → Agent2 → 结果 2
                     → 汇总 → 最终结果
```

**适用场景**：复杂任务、专业分工

### 3. 反射模式

```
生成 → 反思 → 修正 → 再反思 → 最终输出
```

**示例**：
```python
draft = llm.generate(prompt)
critique = llm.generate(f"评估以下内容：{draft}")
revised = llm.generate(f"根据反馈修改：{draft}\n反馈：{critique}")
```

### 4. 人机协作模式

```
用户 → Agent 提议 → 用户确认 → 执行 → 结果
```

**适用场景**：高风险操作、需要人工审核

---

## 2.5 Agent 评估

### 评估维度

| 维度 | 指标 | 测量方法 |
|------|------|----------|
| 准确性 | 任务完成率 | 人工评估/自动化测试 |
| 效率 | 执行时间、Token 消耗 | 日志统计 |
| 可靠性 | 错误率、恢复能力 | 压力测试 |
| 安全性 | 有害输出比例 | Red Teaming |

### 评估框架

**ARES**：
- Accuracy（准确性）
- Reliability（可靠性）
- Efficiency（效率）
- Safety（安全性）

**AgentBench**：
- 8 个环境、200+ 任务
- 涵盖代码、数学、推理等

---

## 2.6 常见面试问题

### Q1: 如何设计一个能自动订机票的 Agent？

**参考答案**：

```
1. 需求分析
   - 输入：出发地、目的地、时间、预算
   - 输出：航班推荐、预订链接

2. 工具设计
   - 航班搜索 API（Skyscanner、携程）
   - 价格比较工具
   - 用户偏好存储

3. Agent 流程
   Thought: 需要搜索航班
   Action: search_flights[北京，上海，2026-04-01]
   Observation: 返回 10 个航班
   Thought: 需要筛选符合预算的
   Action: filter[price < 1000]
   ...

4. 记忆设计
   - 用户偏好（靠窗、直飞）
   - 历史订单

5. 异常处理
   - API 失败重试
   - 无符合条件航班的处理
```

### Q2: Agent 陷入死循环怎么办？

**参考答案**：

1. **预防**：
   - 设置最大迭代次数
   - 检测重复动作
   - 超时机制

2. **检测**：
   ```python
   def detect_loop(history, window=5):
       recent = history[-window:]
       return len(set(recent)) < window // 2
   ```

3. **恢复**：
   - 回滚到上一个有效状态
   - 请求人工干预
   - 切换到简化模式

### Q3: 如何优化 Agent 的 Token 消耗？

**参考答案**：

1. **上下文压缩**：
   - 摘要历史对话
   - 只保留关键信息

2. **工具优化**：
   - 批量调用代替多次调用
   - 缓存重复查询结果

3. **模型选择**：
   - 简单任务用小模型
   - 复杂任务用大模型

4. **Prompt 优化**：
   - 精简指令
   - 避免冗余

---

## 2.7 实战项目建议

### 项目 1：个人研究助手

**功能**：
- 根据主题搜索论文
- 提取关键信息
- 生成文献综述

**技术栈**：
- LangChain + SerpAPI + Arxiv API
- Chroma 存储
- GPT-4 / Claude

### 项目 2：代码审查 Agent

**功能**：
- 读取 PR 变更
- 检查代码规范
- 发现潜在 bug
- 生成审查意见

**技术栈**：
- GitHub API
- Tree-sitter（代码解析）
- 自定义规则引擎

### 项目 3：数据分析助手

**功能**：
- 上传 CSV/Excel
- 自然语言查询
- 自动生成图表
- 导出报告

**技术栈**：
- Python REPL 工具
- Pandas + Matplotlib
- Code Interpreter

---

## 📚 延伸阅读

- [LangChain Agents 文档](https://python.langchain.com/docs/modules/agents/)
- [AutoGen 论文](https://arxiv.org/abs/2308.08155)
- [ReAct 论文](https://arxiv.org/abs/2210.03629)
- [WeThinkIn/AIGC-Interview-Book - AI Agent 基础](https://github.com/WeThinkIn/AIGC-Interview-Book/tree/main/AI%20Agent%E5%9F%BA%E7%A1%80)

---

**上一章**：[01-AIGC 基础.md](./01-AIGC 基础.md)  
**下一章**：[03-开发技能.md](./03-开发技能.md)
