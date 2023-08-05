# -----------------------------------------
# collection: list、tuple、set、dict
# list = []
# tuple = ()
# set = {1, 2, 3} or set()
# dict = {} or {'a': 1, 'b': 2}
# -----------------------------------------
# 1、list：内部元素有序(添加顺序，从0开始)
list_empty = []
print(type(list_empty), list_empty)

list1 = [1, 2, 3, 'a', 1.2]
list1.append(1)
list.append(2)
list.append('a')
print(list)

# 查看list内部元素
print(list1[0], list1[2], list[-1], list[:])

# 修改内部元素
list1[0] = 0
print(list1)

# 删除内部元素
del list1[0:2]
print(list1)

# 清空所有元素
list1.clear()
print(list1)


# +：拼接
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)
print(list1 * 3)

index = 0
for x in list1:
    list1[index] = x * 3
    index += 1
print(list1)

list3 = [x * 3 for x in list1]
print(list3)

list1 = [1, 2, 2, 3, 1.2]

# count: 指定元素的数量
# index: 指定元素出现的位置，第一个位置为0
print(list1.count(2), list1.index(2), min(list1), max(list1), len(list1))


# 参数为序号位置
print(list1.remove(2), list1)
print(list1.pop(), list1)
print(list1.pop(0), list1)

list1.insert(0, -1)
print(list1)

print(list1.reverse())
print(list1)

print(list1.sort())
print(list1)



# tuple，和list的区别在于内部元素无法修改
tuple1 = ()
print(type(tuple1))
print(tuple1)

tuple1 = (1, 2, 3)
print(tuple1[0])
print(tuple1[:])

tuple2 = tuple1 + (3, 5, 6)
print(tuple2)

print(tuple1 * 2)

tuple1 = (1, 2)
tuple2 = list(tuple1)
print(type(tuple2))
