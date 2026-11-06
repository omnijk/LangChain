from langchain_deepseek import ChatDeepSeek;
from langchain_core.prompts import ChatPromptTemplate;
from langchain.chat_models import init_chat_model;
from langchain_core.messages import HumanMessage,SystemMessage;
from dotenv import load_dotenv;
load_dotenv();

# # 初始化模型：这是根据不同厂商适配的不同模型
# llm = ChatDeepSeek(
#     model = "deepseek-flash",
#     temperature=0.7,
#     # 模型的随机性，取值范围0-1，数值越大，模型的回答越天马行空，越小回答越固定
#     timeout=None,
#     # http请求超时时间，不设置代表多久也不算超时
#     max_retries=2
#     # 最多重试两次
# )

# 初始化模型：统一各大模型的写法
llm = init_chat_model(
    model="deepseek-flash",
    model_provider="deepseek",
    temperature=0,
    max_tokens=1024,
    timeout=30,
    max_retries=2
)

# # prompt模板
# prompt = ChatPromptTemplate.from_template(
#     "请解释：{topic}"
# )

# # 创建chain,链条
# chain = prompt|llm;

# # 调用大模型
# result = chain.invoke({
#     "topic":"langchain"
# })

# 传入不同角色的消息
msg=[
    SystemMessage(content="你是一名小老师，简洁且通俗易懂的讲解知识"),
    HumanMessage(content="啥是langchain")
]

# result = llm.invoke(msg)

# # 输出结果
# print(result.content);

# 使用流式输出
for chunk in llm.stream(msg):
    print(chunk.content,end="",flush=True)

