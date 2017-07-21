Find_the_weather
		
# 简介 
Find_the_weather是可以实现用户通过输入所要选取的日期以及相关的城市名的一个简单操作，来查询所选取时间段的该城市的天气预报，以此来简单获取到天气实况！

## 输入：
用户输入日期，城市 交互界面使用到[HTML5之datalist标签](http://www.w3school.com.cn/html5/html5_datalist.asp)
具体详情见  [templates/entry.html](templates/entry.html)
## 输出：
预期用户得到输出结果为：所对应的天气温度和天气现象（例如小雨，晴，暴雨等等）， 
见  [templates/results.html](templates/results.html)
## 从输入到输出，本组作品使用了：
### 模块
•[requests](http://www.python-requests.org/en/master/)
### 数据
•[city_name.txt](city_name.txt)
其中包含503个城市name及其code
### API
[心知天气](https://api.seniverse.com/v3/weather/now.json?key=lkdq5kssgdg01qrn&location=guangzhou&language=zh-Hans&unit=c)
变量为city_name

# Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 [find_the_weather_4web.py](find_the_weather_4web.py) 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：[find_the_weather_4web.py](find_the_weather_4web.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版  [templates/entry.html](templates/entry.html)会出现《欢迎使用天气查询工具》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'city’和‘date’，详见HTML  [templates/entry.html](templates/entry.html)，使用了HTML5的datalist 定义在 list="name"" 及 datalist标签，
前端浏览器web 请求：用户选取指标後按了提交钮「寻找」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_date'，以POST为方法，动作为／[main.py](main.py)请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_date', methods=['POST'])的函数 pick_a_date()

find_the_weather_4web.py 中 def pick_a_date() 函数，把用户提交的数据，以flask 模块request.form['city']和['date']	取到Web 请求中，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出）。

前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应,显示信息。



## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
