# 迭代器 iterator
# 一个一个、一次一次 获得当前对象：next()
# 关键：如何获得下一个对象
# 自定义一个迭代器
#   1、新建一个类
#   2、__iter__(self)：表明可迭代
#   3、__next__(self)：编写规则如何获取下一个元素


# yield，只能用在函数内部
# 把含有 yield 的函数称之为 生成器函数(generator function)
# 把 生成器函数 返回的结果称为 生成器(generator) (生成器对象也是迭代器，所以它的运行方式和迭代器一致)
# 执行过程
#   1、通过 next() 函数来调用
#   2、每次 next() 都会在 生成器函数内部遇到 yield 后返回结果
#   3、如果函数运行结束(return)则抛出 StopIteration 异常

# 生成器的4个状态
#   1、生成器函数 ——> 生成器对象：初始状态
#   2、next()：运行中状态
#   3、遇到 yield 语句，next()返回时
#        yield 语句右边的对象作为 next() 的返回值
#        生成器在 yield 语句所在的位置暂停，当再次使用 next() 时继续从该位置继续运行
#   4、如果执行到函数结束，则抛出 StopIteration 异常
#        不管是使用了 return 语句显式地返回值，或者默认返回 None 值，返回值都只能作为异常的值一并抛出
#        此时的生成器对象处于结束的状态
#        对于已经结束的生成器对象再次调用 next()，直接抛出 StopIteration 异常，并且不含返回值

class ReverseIterator:
    def __init__(self, data):
        self.index = len(data)
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            raise StopIteration


class LeftRightIterator:
    def __init__(self, data):
        self.count = 0
        self.left_index = 0
        self.right_index = len(data) - 1
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.data):
            raise StopIteration

        if self.count % 2 == 0:
            value = self.data[self.left_index]
            self.left_index += 1
        else:
            value = self.data[self.right_index]
            self.right_index -= 1
        self.count += 1
        return value


class MyData:
    def __init__(self, list1, list2):
        self._list1 = list1
        self._list2 = list2

    def get_size(self):
        return len(self._list1)

    def get_value(self, index):
        if index >= self.get_size():
            return
        n = len(self._list1) - index - 1
        return str(self._list1[index]) + '-' + str(self._list2[n])

    def __iter__(self):
        return MyDataIterator(self)


class MyDataIterator:
    def __init__(self, data):
        self._data = data
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index < self._data.get_size():
            return self._data.get_value(self._index)
        raise StopIteration


def my_generator():
    list1 = [1, 2, 3]
    for x in list1:
        yield x


def my_generator2(signal):
    print('aaa')
    if signal:
        print('bbb')
        yield 'ccc'
        print('ddd')
    print('eee')


class MyData2:
    def __init__(self, list1, list2):
        self._list1 = list1
        self._list2 = list2

    def __iter__(self):
        index = 0
        size = len(self._list1)
        while index < size:
            last_index = size - index - 1
            yield str(self._list1[index]) + '-' + str(self._list2[last_index])
            index += 1


if __name__ == '__main__':
    list_test = [1, 2, 3]

    # list
    for num in list_test:
        print(num, end=' ')
    print()

    print(type(iter(list_test)))

    for num in iter(list_test):
        print(num, end=' ')
    print()

    list_iterator = iter(list_test)
    for num in list_iterator:
        print(num, end=' ')
    print()

    value = next(list_iterator)
    print(value)

    value = next(list_iterator)
    print(value)

    value = next(list_iterator)
    print(value)

    list_test.reverse()
    for num in list_test:
        print(num, end=' ')
    print()

    # 逆序迭代器
    iterator = ReverseIterator(list_test)
    for num in iterator:
        print(num, end=' ')
    print()
    print(next(iterator))

    # 先左后右顺序的迭代器
    list_test = [1, 2, 3, 4, 5, 6, 7]
    iterator = LeftRightIterator(list_test)

    for num in iterator:
        print(num, end=' ')
    print()
    # print(next(iterator))

    # 自定义数据类型
    data = MyData([1, 2, 3], ['a', 'b', 'c'])
    for i in range(0, data.get_size()):
        print(data.get_value(i), end=' ')
    print()

    print(data)
    print(iter(data))
    print(MyDataIterator(data))

    for x in data:
        print(x, end=' ')
    print()

    for x in iter(data):
        print(x, end=' ')
    print()

    iterator = iter(data)
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))

    for i in range(0, data.get_size()):
        print(next(iterator), end=' ')
    print()

    while True:
        try:
            print(next(iterator), end=' ')
        except StopIteration:
            print('stop error')
            break

    data = MyData2([1, 2, 3], ['a', 'b', 'c'])
    print(data)
    print(type(data))
    print(iter(data))

    for x in data:
        print(x, end=' ')
    print()

    for x in iter(data):
        print(x, end=' ')
    print()

    iterator = iter(data)
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))

    while True:
        try:
            print(next(iterator), end=' ')
        except StopIteration:
            print('stop error')
            break
