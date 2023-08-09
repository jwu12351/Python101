# 定义一个函数
# 函数代码块以 def 关键词开头，后接函数名称、圆括号()
# 传入参数放在圆括号中间，圆括号中间可以用于定义参数
# return [表达式] 结束函数，选择性地返回一个值给调用方
# 不带表达式的return相当于返回 None

# def 函数名(参数列表):
#     函数体

def hello_1():
    print('hello world1')


def hello_2():
    return 'hello world2'


def calculate_num_1(a, b):
    print(a)
    print(b)
    print(a + b)


def calculate_num_2(a, b):
    print(a)
    print(b)
    return a + b


def calculate_num_3(a, b=10):
    print(a)
    print(b)
    return a + b


def calculate_num_4(a, *b):
    total = a
    for x in b:
        total += x
    return total


def calculate_num_5(a, **b):
    print(type(b))
    for key, value in b.items():
        print(key, value)


# num、string、tuple：不可变
# set、dict、list：可变
def change_value_1(a2):
    a2 = '22'
    return '22'


def change_value_2(list_test2):
    list_test2.clear()


print(__name__)
if __name__ == '__main__':
    s = '11'
    a = change_value_1(s)
    print(s)


s = '11'
a = change_value_1(s)
print(a)


list_test1 = {1, 2}
change_value_2(list_test1)
print(list_test1)


print(type(hello_1))
hello_test = hello_1
hello_test2 = hello_test
hello_test2()


# 匿名函数 lambda表达式
function_test = lambda x1, x2: x1 + x2
print(function_test(1, 2))

def function_test(x1, x2):
    return x1 + x2

hello_1()
print(hello_1())
print()


hello_2()  # 没有输出
print(hello_2())
print()


str_test = hello_2()
print(str_test + ' cat')


print(calculate_num_1(1, 2))
print()

print(calculate_num_2(1, 2))
print()

print(calculate_num_2(b=3, a=5))
print()

print(calculate_num_3(1))
print()

print(calculate_num_3(1, 9))
print()

print(calculate_num_4(1, 1, 2, 3))

calculate_num_5(1, b=2, c=3)
