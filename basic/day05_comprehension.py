# 列表推导式
# [表达式 for 变量 in 序列]
# [表达式 for 变量 in 序列 if 条件]
# [表达式1 if 条件 else 表达式2 for 变量 in 序列]
names = ['Bob', 'Tom', 'Alice', 'Jerry']


# 所有
new_names = [name.upper() for name in names]
print(type(new_names))
print(new_names)

new_names = []
for name in names:
    new_names.append(name.upper())
print(new_names)


# if
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

new_names = []
for name in names:
    if len(name) > 3:
        new_names.append(name.upper())
print(new_names)


# if else
new_names = [name.upper() if len(name) > 3 else name for name in names]
print(new_names)

new_names = []
for name in names:
    if len(name) > 3:
        new_names.append(name.upper())
    else:
        new_names.append(name)
print(new_names)


# -----------------------------------------
# 元组推导式(生成器表达式)
# (表达式 for 变量 in 序列)
# (表达式 for 变量 in 序列 if 条件)
# (表达式1 if 条件 else 表达式2 for 变量 in 序列)
# 结果不是元组，而是生成器generator
# 使用 tuple() 函数，可以将生成器对象 转换成 元组
tuple_generator = (name.upper() for name in names)
print(type(tuple_generator))
print(tuple_generator)

# for x in tuple_generator:
#     print(x, end=' ')
# print()

tuple_test = tuple(tuple_generator)
print(type(tuple_test))
print(tuple_test)

# for x in tuple_generator:
#     print(x, end=' ')
# print()


# -----------------------------------------
# 集合推导式
# {表达式 for 变量 in 序列}
# {表达式 for 变量 in 序列 if 条件}
# {表达式1 if 条件 else 表达式2 for 变量 in 序列}
new_names = {name.upper() for name in names}
print(type(new_names))
print(new_names)


# -----------------------------------------
# 字典推导式
# {key的表达式: value的表达式 for value in 序列}
# {key的表达式: value的表达式 for value in 序列 if 条件}
# {key的表达式1: value的表达式1 if 条件 else key的表达式2: value的表达式2 for value in 序列}
dict_test = {'a': 1}
new_names = {name: len(name) for name in names}
print(type(new_names))
print(new_names)

new_names = {(name + '-suffix'): (len(name) + 10) for name in names}
print(type(new_names))
print(new_names)

new_names = {(name + '-suffix'): ((len(name) + 10) if len(name) < 4 else name) for name in names}
print(type(new_names))
print(new_names)
