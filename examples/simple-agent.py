"""
简单 Agent 示例 - 基于 LangChain
功能：支持工具调用的智能助手
"""

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

# 配置 API Key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# 定义工具
def search_web(query: str) -> str:
    """搜索网络获取信息"""
    # 实际使用时接入 SerpAPI 或其他搜索 API
    return f"搜索结果：关于'{query}'的相关信息..."

def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        result = eval(expression)
        return f"计算结果：{result}"
    except Exception as e:
        return f"计算错误：{str(e)}"

def get_weather(city: str) -> str:
    """获取天气信息"""
    # 实际使用时接入天气 API
    return f"{city}今天天气晴朗，气温 25°C，适合外出"

tools = [
    Tool(
        name="Web Search",
        func=search_web,
        description="当你需要搜索网络信息时使用，输入应该是搜索关键词"
    ),
    Tool(
        name="Calculator",
        func=calculate,
        description="当你需要计算数学表达式时使用，输入应该是数学表达式"
    ),
    Tool(
        name="Weather",
        func=get_weather,
        description="当你需要查询天气时使用，输入应该是城市名"
    ),
]

# 创建 LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# 创建 Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，可以帮助用户回答问题。你可以使用以下工具：Web Search、Calculator、Weather"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 创建 Agent
agent = create_openai_functions_agent(llm, tools, prompt)

# 创建记忆
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 创建执行器
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=5
)

# 使用示例
if __name__ == "__main__":
    print("🤖 Agent 助手已就绪！输入'quit'退出\n")
    
    while True:
        user_input = input("你：")
        if user_input.lower() == "quit":
            break
        
        response = agent_executor.invoke({"input": user_input})
        print(f"助手：{response['output']}\n")

"""
使用示例：

你：北京今天天气如何？
助手：北京今天天气晴朗，气温 25°C，适合外出

你：123 * 456 等于多少？
助手：计算结果：56088

你：帮我搜索一下 AI Agent 的最新进展
助手：搜索结果：关于'AI Agent 的最新进展'的相关信息...
"""
