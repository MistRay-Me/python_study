import time

'''
时间和日期
'''

ticks = time.time()
# 获取一个时间戳
print(ticks)
# 获取本地时间
localtime = time.localtime()
print('本地时间为:', localtime)
# 格式化时间
localtime_format = time.asctime(localtime)
print(localtime_format)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
