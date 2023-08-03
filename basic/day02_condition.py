# 判断：if
# 循环: while for
# 停止: continue, break

# if
is_political_science = True

# 只用if
if is_political_science:
    print('yes')

# if + else
if not is_political_science:
    print('yes')
else:
    print('no')

# if + 多个else(elif)
a = 111
if a == 1:
    print('a')
elif a == 2:
    print('b')
elif a == 3:
    print('c')
else:
    print('other')


# while
index = 0
total = 0
while index < 100:
    index += 1
    if index == 100:
        continue
    total += index
print(total)


# for: 可循环 字符串、列表等等....
# range(a, b, c)：生成元素序列, from a, end b, 每次间隔c
for i in range(1, 10, 2):
    print(i, end=' ')
print()

s = 'a*b*c*d*i'
for i in s:
    print(i, end=' ')
print()

s = [1, 2, 3, 'a']
for i in s:
    print(i, end=' ')
print()

for i in range(0, 10):
    if i % 2 == 1:
        continue
    print(i, end=' ')
print()
