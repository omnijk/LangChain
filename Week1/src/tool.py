from langchain.tools import tool
from langchain.agents import create_agent;
from langchain.chat_models import init_chat_model;
from dotenv import load_dotenv;
@tool
def get_weather(city:str)->str:
    '''
    用于大模型查询天气的工具
    '''
    weather_data={
        "北京":"22摄氏度",
        "上海":"sunny"
    };
    return weather_data.get(city,f"找不到{city}的模拟天气")

load_dotenv()

# 工具定义好之后，来定义一个最简单的agent
# 舒适化模型
model = init_chat_model(
    "deepseek:deepseek-flash"
)
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt=(
        "你是一名AI助手"
        "回答天气问题时，必须先调用工具"
    )
)

result = agent.invoke(
    {
    "messages":[
        {
            "role":"user",
            "content":"北京天气怎么样"
        }
    ]
}
)

# 取出消息列表中的最后一条消息，并打印他的内容
print(result["messages"][-1].content)

# 看一下消息列表中的消息分别是什么样子或者结构
for msg in result["messages"]:
    print(f"消息类型:{msg.type}")

    # 查看模型的工具请求,工具请求时AI发出的，所以是AI消息
    if msg.type == "ai" and msg.tool_calls:
        for call in msg.tool_calls:
            print(f"工具名称：{call["name"]}");
            print(f"工具参数：{call["args"]}");

    # 查看工具的返回结果
    if msg.type=="tool":
        print(f"工具名；{msg.name}");
        print(f"工具结果：{msg.content}");

    # 查看模型回答
    if(msg.type=="ai" and not msg.tool_calls):
        print("AI回复",msg.content)

    # 之间的分割
    print('11111111111111111111111111111111111')