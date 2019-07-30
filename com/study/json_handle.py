import json

# Python 字典类型转换为json对象

data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print("Python原始对象:", repr(data1))
print('json对象', json_str)

# 将json对象转换为json字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])


