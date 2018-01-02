import weatherHttp_2
import sql_test_1
import sql_test_2
import datetime


# 案例坐标：上海
twitters = weatherHttp_2.getCityWeather_RealTime(101020100)

city = twitters[0]  # 城市
temp = twitters[1]  # 温度
fx = twitters[2]    # 风向
fl = twitters[3]    # 风力
sd = twitters[4]    # 相对湿度
tm = twitters[5]    # 更新时间
wind = fx + fl      # 风
city = '上海'        # 城市
now = datetime.datetime.now()
times = str(now.strftime('%Y-%m-%d ')) + tm    #时间

# print(city, times, temp, wind, sd)

# 查询数据
weathers = sql_test_1.queryAllData()

# 是否插入
for model in weathers:
    if model[1] != times :
        print(model[1])
        sql_test_2.insertData(city,times,temp,wind,sd)

