import datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)

# 格式化时间字符串
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)

# 将字符串转换为datetime对象
time_str = "2022-03-11 12:30:45"
time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(time_obj)

# 获取指定日期的前一天
date_obj = datetime.date(2022, 3, 11)
yesterday = date_obj - datetime.timedelta(days=1)
print(yesterday)

# 获取指定日期的后一天
tomorrow = date_obj + datetime.timedelta(days=1)
print(tomorrow)

# 计算两个日期之间的天数差
date1 = datetime.date(2022, 3, 1)
date2 = datetime.date(2022, 3, 11)
delta_days = (date2 - date1).days
print(delta_days)

# 获取当前月份
current_month = now.month
print(current_month)

# 获取当前年份
current_year = now.year
print(current_year)

# 获取当前日期所在周的第一天和最后一天
weekday = now.weekday()  # 获取当前日期的星期几，0代表星期一，6代表星期日
start_of_week = now - datetime.timedelta(days=weekday)
end_of_week = start_of_week + datetime.timedelta(days=6)
print(start_of_week, end_of_week)