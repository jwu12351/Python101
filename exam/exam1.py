# 1、编写一个函数，用于判断一个字符串是不是回文字符串，返回True或False
# 回文数：从头到尾、从尾到头，都是一样的
# 例：abba、abccba、aaa
def judge(content):
    # return content == content[::-1]

    # return content == ''.join(reversed(content))

    reversed_content = ''
    index = len(content) - 1
    while index >= 0:
        reversed_content += content[index]
        index -= 1
    return content == reversed_content


print(judge('abba'))
print()

test_cases = ["abba", "abccba", "——aaa——", "JBbj", "JBA A BJ", "1221", "12aa 21", "2345"]
for s in test_cases:
    print(judge(s))
print()


# 2、编写一个函数，参数为1个字符串，对于其中重复出现的字符，只保留第一次出现的；返回去除之后的字符串
# 例：abcdabce ——> abcde
def remove_repeat(content):
    result = ''
    for x in content:
        if x not in result:
            result += x
    return result


print(remove_repeat('abcdabce'))
print()


# 3、编写一个函数，参数为1个字符串，对于其中重复出现的字符，全部删除；返回去除之后的字符串
# 例：abcdabce ——> de
def remove_repeat2(content):
    result = ''
    for x in content:
        if content.count(x) == 1:
            result += x
    return result


def remove_repeat3(content):
    result = ''

    count_dict = {}
    for x in content:
        if x not in count_dict:
            count_dict[x] = 1
        else:
            count_dict[x] += 1

    for x in content:
        if count_dict[x] == 1:
            result += x

    return result


print(remove_repeat2('abcdabce'))
print(remove_repeat3('abcdabce'))
print()


# 4、编写一个函数，参数为一个都是数字的列表，根据数字的绝对值进行排序；返回排序后的列表
# 例：[1, -6, 2, -5, 9, 4, 20, -3] ——> [1, 2, -3, 4, -5, -6, 9, 20]
def rank_list(num_list):
    # return sorted(num_list, key=lambda x: abs(x))
    # return sorted(num_list, key=lambda x: x if x > 0 else 0 - x)

    count_dict = {}
    for num in num_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    num_dict = {}
    for num in num_list:
        if num >= 0:
            num_dict[num] = num
        else:
            num_dict[num] = 0 - num
    dict_sorted = sorted(num_dict.items(), key=lambda x: x[1])
    # return [item[0] for item in dict_sorted]

    result = []
    for item in dict_sorted:
        value = item[0]
        for i in range(0, count_dict[value]):
            result.append(value)
    return result


print(rank_list([1, -6, 2, -2, -5, -2, 9, 4, 20, -3]))
print()


# 5、编写一个函数，参数为2个字典，合并2个字典为1个字典，返回合并后的字典
# 例：
# 1 {'a': 1, 'b': 2, 'c': 3}
# 2 {'b': 1, 'c': 2, 'd': 3}
# ——> {'a': 1, 'b': 3, 'c': 5, 'd': 3}
def merge_dict(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1

    # for key in dict1:
    #     if key in dict2:
    #         dict2[key] += dict1[key]
    #     else:
    #         dict2[key] = dict1[key]
    # return dict2


dict1 = {'a': 1, 'b': 2, 'c': 3}
print(merge_dict(dict1, {'b': 1, 'c': 2, 'd': 3}))
print()

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 1, 'c': 2, 'd': 3}
# dict3 = {}
#
# for key in set(dict1) | set(dict2):
#     # 用get 从 dict1&dict2 中获取对应键的值 如果键不存在 返回默认值0
#    dict1_value = dict1.get(key,0)
#    dict2_value = dict2.get(key,0)
#    dict3[key] = dict1_value + dict2_value
#
# print(dict3)


# # 6、编写一个函数，参数为一个数字，作为行数，打印出'*'构成的等腰三角形
# # 例，4行
#    *       1 = 2 * 1 - 1， 3 = 4 - 1
#   ***      3 = 2 * 2 - 1， 2 = 4 - 2
#  *****     5 = 2 * 3 - 1， 1 = 4 - 3
# *******    7 = 2 * 4 - 1， 0 = 4 - 4
def print_star_tree(line_num):
    for i in range(1, line_num + 1):
        star_num = 2 * i - 1
        space_num = line_num - i

        for j in range(0, space_num):
            print(' ', end='')
        for j in range(0, star_num):
            print('*', end='')
        print()


print_star_tree(4)
print()


# 7、打印99乘法表
# 1x1=1
# 1x2=2 2x2=4
# 1x3=3 2x3=6 3x3=9
# 1x4=4 2x4=8 3x4=12 4x4=16
# 1x5=5 2x5=10 3x5=15 4x5=20 5x5=25
# 1x6=6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36
# 1x7=7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49
# 1x8=8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64
# 1x9=9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81
def print_nine_nine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + "x" + str(i) + "=" + str(i * j) + ' ', end='')
        print()


print_nine_nine()
