# 步骤1：定义装饰器（接收函数作为参数）
def log_decorator(func):
    # 步骤2：定义内部函数（包装原函数，添加额外功能）
    def wrapper(*args, **kwargs):
        # 额外功能1：执行前打印日志
        print(f"[日志] 函数 {func.__name__} 开始执行")
        print(f"位置参数：{args}")
        print(f"关键字参数：{kwargs}")
        # 执行原函数，保留返回值
        result = func(*args, **kwargs)
        # 额外功能2：执行后打印日志
        print(f"[日志] 函数 {func.__name__} 执行完成")
        # 返回原函数的结果
        return result
    # 步骤3：返回包装后的函数
    return wrapper

# 步骤4：使用装饰器（@语法糖）
@log_decorator
def add(a, b,c=4):
    """计算两数之和"""
    return a + b

# 调用装饰后的函数
print(add(2, 3,c=3 ))
"""
输出结果：
[日志] 函数 add 开始执行
[日志] 函数 add 执行完成
5
"""



def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func.__name__}")
        print(f"位置参数：{args}")
        print(f"关键字参数：{kwargs}")
        result = func(*args, **kwargs)  # 传递所有参数给原函数
        print(f"函数返回：{result}")
        return result

    return wrapper


# 被装饰函数可以是任意参数形式
@log_decorator
def add(x, y, z=0):
    return x + y + z


@log_decorator
def print_info(name, age, **kwargs):
    return f"{name}({age}): {kwargs}"


add(1, 2)
print_info("Alice", 25, city="Beijing")  # 适配混合参数


def print_args(*args):
    print("args中的每个元素：")
    for index, value in enumerate(args):
        print(f"第{index + 1}个元素: {value}")


def print_kwargs(**kwargs):
    print("kwargs中的键值对：")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


def func(a, b=10, *args, **kwargs):
    print(f"固定参数a: {a}")
    print(f"默认参数b: {b}")
    print(f"可变位置参数args: {args}")
    print(f"可变关键字参数kwargs: {kwargs}")


func(1, 2, 3 ,8, c=5, d=6, e=7,t=20)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet(1,"qqq")