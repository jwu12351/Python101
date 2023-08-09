# set
# 无序的、不重复的 元素序列
# 可以进行并集、交集、差集、补集的运算
set1 = set()
print(type(set1))
print(set1)

# add: 参数是单个元素
# update: 参数可以是列表，元组，字典等
set1 = {1, 3, 2, 3, 5, 0, 7, 8}
set1.add(1)
set1.add(1)
set1.add(2)
print(set1)

set1.update([2, 3, 4])
print(set1)

# remove: 如果元素不存在，会发生错误
# discard: 如果元素不存在，不会发生错误
if -1 in set1:
    set1.remove(-1)
print(set1)

set1.discard(99)  # 即使不存在也不报错

# pop: 随机删除
value = set1.pop()
print(value, set1)

set1.clear()
print(set1)

del set1
# print(set1)

set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set2 = {'a', 'b', 'c', 'x', 'y', 'z'}
print(set2)

# 并集
set3 = set1.union(set2)
print(type(set3), set3)
print(type(sorted(set3)), sorted(set3))
print(sorted(set1 | set2))

# 交集
set3 = set1.intersection(set2)
print(sorted(set3))
print(sorted(set1 & set2))
print(set1.isdisjoint(set2))


# 差集
set3 = set1.difference(set2)
print(set3)
print(set1 - set2)  # set1独有的(移除与set2共有的)

set3 = set2.difference(set1)
print(set3)
print(set2 - set1)  # set2独有的(移除与set1共有的)

print(set1.symmetric_difference(set2))  # 返回两个集合中不重复的元素集合

set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set2 = {'a', 'b', 'c', 'x', 'y', 'z'}
set1.difference_update(set2)  # set1独有的(移除与set2共有的)，set1本身被修改
print(set1)


set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set2 = {'a', 'b', 'c', 'x', 'y', 'z'}
set2.difference_update(set1)  # set2独有的(移除与set1共有的)，set2本身被修改
print(set2)


# 子集、超集
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1.issubset(set2))
print(set2.issuperset(set1))
print('\n' * 10)



# dict
# 存储键值对，用于根据key查找对应的value;
# key 应该 是唯一的，例如数字、字母、字符串，但不可以是 可变数据类型，比如list、set、dict
# key1: [value1, value2...]
# key2: [value1, value2...]
# ....
dict_empty = {}
print(type(dict_empty), dict_empty)

dict1 = {'cat': 1, 'dog': 2, 'bird': 3}

# add
dict1['fish'] = 0
print(dict1)

# update
dict1['bird'] = 0
print(dict1)

# 对已存在的不修改，只添加原来不存在的
dict1.setdefault('bird', -1)  # 'bird'已存在，不变
print(dict1)
dict1.setdefault('fish', -1)  # 'fish'不存在，新增
print(dict1)

# 查看元素
print(dict1['cat'], dict1['dog'])
print(dict1.get('cat'), dict1.get('dog'))

key = 'wewe'
# print(dict1[key])    # 不存在，报错
print(dict1.get(key))  # 不存在，返回 None

if key in dict1:
    print(dict1[key])

print(dict1.keys())
print(dict1.values())
print(dict1.items())


# 遍历所有元素
for key in dict1.keys():
    print(key, dict1.get(key))
print()

for item in dict1.items():
    print(item)
print()

for item in dict1.items():
    print(item[0], item[1])
print()

for key, value in dict1.items():
    print(key, value)
print()


# 删除
value = dict1.pop('cat')
print(value)

item = dict1.popitem()
print(item)

# del dict1


# 排序
dict1 = {'cat': 10, 'dog': 1, 'bird': 3}

dict_sorted = sorted(dict1.items(), key=lambda x: x[0])  # 0表示第一个key，按key排序
print(dict_sorted)

dict_sorted = sorted(dict1.items(), key=lambda x: x[1])  # 1表示第二个value，按value排序
print(dict_sorted)

dict_sorted = sorted(dict1.items(), key=lambda x: x[1], reverse=True)  # 1表示第二个value，按value排序，且逆序
print(dict_sorted)
