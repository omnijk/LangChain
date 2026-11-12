from langchain.tools import tool
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


