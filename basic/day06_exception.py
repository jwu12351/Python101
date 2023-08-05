# exception：异常，运行期检测到的错误
# raise：手动抛出异常
# assert：断言，判断一个表达式为false的时候触发异常

# try:
#     xxxx             # 正常的业务逻辑
# except XXXError:
#     xxx              # 若出现异常 所执行的的操作
# else:
#     xxx              # 若未出现异常 所执行的操作
# finally:
#     xxx              # 最后一定执行的操作

a = 2
b = 0
print(a / b)


if b != 0:
    print(a / b)
else:
    print('b不能为0')


num_str = input('请输入一个数字：')
if num_str.isdigit():
    num = int(num_str)
    print(num + 10)
else:
    print('需要是一个数字')


try:
    print(a / b)
except ZeroDivisionError:
    print('b不能为0')
print()


try:
    print(a / b)
except ZeroDivisionError as f:
    print('b不能为0')
    print(f)
print()


try:
    num_str = input('请输入一个数字：')
    num = int(num_str)
    print(num + 10)
except ValueError as f:
    print('需要是一个数字')
    print(f)


num_str = input('请输入一个数字：')
try:
    num = int(num_str)
except ValueError as f:
    print('需要是一个数字')
    print(f)
else:
    print(num + 10)


num_str = input('请输入一个数字：')
try:
    num = int(num_str)
except ValueError as f:
    print('需要是一个数字')
    print(f)
else:
    print(num + 10)
finally:
    print('bye')


# raise
a = 2
b = 0
if b == 0:
    raise ZeroDivisionError
print('next')


try:
    raise ZeroDivisionError
except Exception:
    print('found error')


# assert
b = 1
assert b == 0
print('xxxxx')


b = 1
assert b == 0, 'b应该为0'
print('xxxxx')
