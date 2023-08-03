# var naming: 数字，字母，下划线
# 首字母不为数字 wrong: 1a = 2
# 不能用系统内置的单词 break if for while
a = 1
a1 = 1
a_1 = 1

print(1, 2, sep='_', end='\n\n')

a = input("please input a: ")
b = input("please input b: ")
print(int(a) + int(b))

# int() float() str()
print('aaa' + str(1) + 'bbb')

# 四舍五入
print(round(121.12121, 4))
print(int(round(121.12121, 4)))

print(min(1, 2), max(1, 22))

a = 1 + 121
b = 2
a = b = c = 1
print(a, b, c)

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# string
s = ' political * science '
print(type(s))
print(s[2])
print(s[:-2])
print(s.split('*'))
print(s.strip())
print(s.replace(' ', ''))
print(s.upper(), s.lower())

# boolean, 布尔， True or False
print(s.strip().startswith('j'))
print(s.count('i'))

if 'qq' in s:
    print(s.index('qq'))
else:
    print('not found')

# 查找所有出现的位置
index = 0
for x in s:
    if x == 'i':
        print('find', index)
    index = index + 1  # index += 1

# 转义符(Escape character): \n 换行，\t TAB
print("121\t1212\n")

s = 'political science'
print(s * 3)
