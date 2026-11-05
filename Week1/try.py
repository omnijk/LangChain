from langchain_deepseek import ChatDeepSeek;
from langchain_core.prompts import ChatPromptTemplate;
from dotenv import load_dotenv;
load_dotenv();

# 初始化模型
llm = ChatDeepSeek(
    model = "deepseek-flash"
)

# prompt模板
prompt = ChatPromptTemplate.from_template(
    "请解释：{topic}"
)

# 创建chain,链条
chain = prompt|llm;

# 调用大模型
result = chain.invoke({
    "topic":"langchain"
})

# 输出结果
print(result.content);