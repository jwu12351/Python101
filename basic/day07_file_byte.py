import os
import ctypes

# 文件的读写
# open()
# read()、readline()、readiness()
# write()、writelines()
# flush()、close()
# tell()、seek()

# open(file_path, mode='r', encoding='UTF-8')
# mode
#   t(text文本)、b(binary二进制)
#   x(写模式，新建一个文件，如果该文件已存在则会报错)、+(打开一个文件进行更新(可读可写))
#   r(只读；如果该文件不存在，报错；如果写入，报错)
#       rb(二进制格式)、r+(可读可写)、rb+(二进制格式可读可写)
#   w(只写，完全覆盖(先清空再写)；如果该文件不存在，先创建新文件；如果读取，报错)
#       wb(二进制格式)、w+(可读可写)、wb+(二进制格式可读可写)
#   a(追加；如果该文件不存在，先创建新文件)
#       ab(二进制格式)、a+(可读可写)、ab+(二进制格式可读可写)
#   r+ 如果该文件不存在，报错；写入时，从头开始写，同时覆盖原有内容，当新内容少于原有内容，未覆盖部分保留(前部分新，后部分旧)
#   w+ 如果该文件不存在，先创建新文件；如果文件存在，每次打开文件时，会清空原有内容，再写入
#   a+ 如果该文件不存在，先创建新文件；如果文件存在，在原内容后追加写
# with语句 可以保证文件在读取完成后自动关闭


file_path = 'file.txt'
content_list = ['abc', 'def', 'ghi']

f = open(file_path, 'r')
for line in f.readlines():
    print(line)
f.close()


# 1、只读
# 先判断文件是否存在
if os.path.isfile(file_path):      # pathlib.Path(file_name).is_file()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            print(line)
# 判断目录是否存在: os.path.exists(dir_path)、pathlib.Path(file_name).exist()

result = ''
if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result += line
print(result)


# 2、读、覆盖写
with open(file_path, 'a+') as f:
    f.write('123\n')
    for x in content_list:
        f.write(x + '\n')

result = ''
with open(file_path, 'w+') as f:
    for line in f.readlines():  # 已打开就清空，可以读取，但是内容还是空的
        result += line
    print(result)

    f.write('123')

    print(f.tell())
    f.seek(0)
    print(f.tell())
    result = ''
    for line in f.readlines():
        result += line
    print(result)


# 3、读、追加写
with open(file_path, 'a+') as f:
    f.write('abc')

result = ''
with open(file_path, 'a+') as f:
    f.seek(0)
    for line in f.readlines():
        result += line
    print('before')
    print(result)

    f.write('abc\n')

    f.seek(0)
    result = ''
    for line in f.readlines():
        result += line
    print('after')
    print(result)

# 二进制
#   0: 0
#   1: 1
#  10: 2
#  11: 3
# 100: 4

# 0000 0000：0
# 0000 0001：1
# 0000 0010：2
# 0000 0011：3
# 0000 0100：4 = 0*2^0 + 0*2^1 + 1*2^2
# 0001 0000：16 = 0*2^0 + 0*2^1 + 1*2^4
# 1111 1111: 255 = 1*2^0 + 1*2^1 + 1*2^2 + 1*2^3 + 1*2^4 + 1*2^5 + 1*2^6 + 1*2^7


# Bit(位): 0、1
# Byte(字节): 8 Bits
# 硬件如何存储信息
#   物理电磁学(正负电荷、高低电平、频率振幅)——计算机硬件(CPU、内存、磁盘)——0/1——数字(16/10进制)<——>编码(映射)<——>人类使用的字符
#   1963, ASCII(American Standard Code for Information Interchange), 数字、字母、符号等128个常用字符
#   1964, IBM System/360，1 Byte = 8 Bit
#   1个字节可以存储的范围：2^8 = 256，-127~128 or 0-255
#   2个字节可以存储的范围：2^16 = 65536
#   3个字节可以存储的范围：2^24 = 1677 7216
# 最全的字符集：Unicode字符集，最多可以编码大约 110 万个字符
# UTF-8: Unicode字符集的一种常用编码方式


# 十六进制
# 0000: 0   0001: 1   0010: 2   0011: 3
# 0100: 4   0101: 5   0110: 6   0111: 7
# 1000: 8   1001: 9   1010: A   1011: B
# 1100: C   1101: D   1110: E   1111: F
# 0001 0000: 0x10 = 0*16^0 + 1*16^1 = 16
# 1111 1111: 0xFF = F*16^0 + F*16^1 = 15+15*16=255

# RGB: R(0-255) G(0-255) B(0-255)
# xxxx xxxx xxxx xxxx 0xFF0000 0xFF0000 0xFF0000


# 文字的编码
s = '你好世界'
bytes_str = s.encode("UTF-8")
print(bytes_str)

str_16 = str(bytes_str).replace('\\x', ' ').replace("b' ", '').replace("'", '')
print(str_16)

for x in str_16.split(' '):
    print(bin(int(x, 16)).replace('0b', ''), end=' ')
print()

print(bytes_str.decode("UTF-8"))


# 使用二进制形式打开文件
file_path = 'file.txt'
result = ''
with open(file_path, 'rb') as f:
    result = f.read()
print(result)
str_16 = str(result).replace('\\x', ' ').replace("b' ", '').replace("'", '')
print(str_16)
print(result.decode("UTF-8"))


# 复制Excel文件
file_path = 'a.xlsx'
result = ''
with open(file_path, 'rb') as f:
    result = f.read()
print(str(result))

with open('b.txt', 'wb') as f:
    f.write(result)


# 程序员节：10月24日，1024
# 10^1 = 1deca  = 1da
# 10^2 = 1hecto = 1h
# 10^3 = 1kilo  = 1k
# 10^3  = 1000^1 = 1Kilo = 1K
# 10^6  = 1000^2 = 1Mega = 1M
# 10^9  = 1000^3 = 1Giga = 1G
# 10^12 = 1000^4 = 1Tera = 1T
# 10^15 = 1000^5 = 1Peta = 1P

# Bit 位: 0、1
# Byte 字节: 8 Bits
# 0000 0000：0
# 0000 0001：1
# 0000 0010：2
# 0000 0011：3
# 0000 0100：4

# 0000 1000：8，2 ^ 3
# 0001 0000：16，2 ^ 4
# 0010 0000：32，2 ^ 5
# 0100 0000：64，2 ^ 6
# 1000 0000：128，2 ^ 7

# 0001 0000 0000：256，2 ^ 8
# 0010 0000 0000：512，2 ^ 9
# 0100 0000 0000：1024，2 ^ 10
# 1000 0000 0000：2028，2 ^ 11

# 2^10 = 1024^1 = 1Kibi = 1Ki
# 2^20 = 1024^2 = 1Mebi = 1Mi
# 2^30 = 1024^3 = 1Gibi = 1Gi
# 2^40 = 1024^4 = 1Tebi = 1Ti
# 2^50 = 1024^5 = 1Pebi = 1Pi

# Bit 位: 0、1
# Byte 字节: 8 Bits
# KB KiB：1024 Bytes
# MB MiB: 1024 KiB
# GB GiB: 1024 MiB

# U盘：标的是128GB
# 128 * 1024 * 1024 * 1024 Bytes = 137,438,953,472 Bytes
# 128 * 1000 * 1000 * 1000 Bytes = 128,000,000,000 Bytes
# 128,000,000,000 Bytes / 1024 / 1024 / 1024 = 119.21 GiB
# 119.21 / 128 = 93.13%

# 硬盘：标的是512GB
# 512 * 1024 * 1024 * 1024 Bytes = 549,755,813,888 Bytes
# 512 * 1000 * 1000 * 1000 Bytes = 512,000,000,000 Bytes
# 512,000,000,000 Bytes / 1024 / 1024 / 1024 = 476.84 GiB
# 476.84 / 512 = 93.13%

# 硬盘：标的是1TB
# 1000 * 1024 * 1024 * 1024 Bytes = 1,073,741,824,000 Bytes
# 1000 * 1000 * 1000 * 1000 Bytes = 1,000,000,000,000 Bytes
# 1,000,000,000,000 Bytes / 1024 / 1024 / 1024 = 931.32 GiB
# 931.32 / 1000 = 93.13%
