- chunk有以下几个常见的属性
- chunk.content:当前的文本内容
- chunk.id:消息id
- chunk.response_metadata ： 模型返回的一些元数据
- chunk.usage_metadata    # token 用量信息


## 流式输出
```py
for chunk in llm.stream(msg):
    print(chunk.content,end="",flush=True)
```
- print默认end会换行，所以将end换为啥也没有
- flush=True 立即把内容刷到终端，不等缓冲区攒够再显示。

## langchain对模型可用工具的封装
从langchain.tool包里引入tool，这个工具变成了大模型自动可以用的工具了，此时的注释也变成了给大模型看的工具描述.
不过也不是魔法，只是大模型能认识这个工具了，具体要让大模型能调用这个工具，还要绑定一下工具

## create_agent常用的参数
- model:模型，唯一必填参数
- tools:可用工具列表
- system_prompt:系统提示词，定义agent的角色和行为
- 传给agent的消息格式如下
```py
{
    "messages":[
        {
            "role":"user",
            "content":"杭州天气怎么样"
        }
    ]
}
```