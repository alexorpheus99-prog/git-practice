# 一个小练习：Python 基础
# 双击打不开，要在 VS Code 里跑，或者命令行里 python hello.py


def greet(name):
    return "你好，" + name + "！欢迎来到 Python。"


def add(a, b):
    """把两个数加起来。"""
    return a + b


if __name__ == "__main__":
    print(greet("乌金-分支版"))
    print("1 + 2 =", add(1, 2))
