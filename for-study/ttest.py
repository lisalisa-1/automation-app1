import json
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")


# 定义一个元组
my_tuple = (1, 2, 3, 4, 5)

# 使用星号获取前三个元素和最后一个元素
first_three, *rest = my_tuple
first_element, *middle_elements, last_element = my_tuple

print(first_three)        # 输出: (1, 2, 3)
print(rest)               # 输出: [4, 5]
print(first_element)      # 输出: 1
print(middle_elements)    # 输出: [2, 3, 4]
print(last_element)       # 输出: 5

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(
    tinydict['Name']
)

json1=json.dumps(tinydict)
