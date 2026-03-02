# 简单的生成器函数
def simple_generator():
    print("第一步：执行到 yield 前")
    yield "返回给调用者的值"  # 暂停，返回值
    print("第二步：从 yield 恢复执行")  # 调用者再次触发时执行

# 调用生成器
gen = simple_generator()
# 第一次调用：执行到 yield，返回值
print(next(gen))  # 输出：第一步：执行到 yield 前 → 返回给调用者的值
# 第二次调用：从 yield 继续执行
print(next(gen))