import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'https://www.runoob.com'
}
print("ttjson",data)

file_path = json.dump(data, open('data.json', 'w'), ensure_ascii=False, indent=4)

json_str = json.dumps(data)
dict1=json.loads(json_str)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)
print("dict1:", dict1)
