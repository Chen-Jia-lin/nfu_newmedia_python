import requests,json,urllib.request #python中的import语句是用来导入模块的,在这里导入了requests和json模块
def find_the_weather(city_name): #定义def函数查询天气 变量为city_name
   #各个城市天气状况的Api
        url_api = ( 'https://api.seniverse.com/v3/weather/now.json?key=lkdq5kssgdg01qrn&location=guangzhou&language=zh-Hans&unit=c'%city_name)
        response = urllib.request.urlopen(url_api)#使用urllib.request 来抓取api资源.
        weather_html = response.read()
        json_data = json.loads(weather_html)
        
        return [json_data()]
    
  

