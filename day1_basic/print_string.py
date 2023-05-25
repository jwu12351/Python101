# print
print('Hello World!')
print(1, 2, sep='_')

print('a' + 'b')
s = 'cat '
print(s * 3)

a = 1
b = 2
c = a + b
d = e = c + 1
print(a, b, c, d, e)

a = True
b = False
c, d = 1, 2
print(a, b, c == d, c != d)

# input()
# int()、float()、round()
# str()
# a = input("please input a: ")
# b = input("please input b: ")
# print(a + b)
# print(int(a) + int(b))
print(int('12'), float('12.3456'), round(12.3456, 2))
print('aaa' + str(1) + 'bbb')

# min() max()
print(min(1, 2), max(1, 10))


# string
s = "It's a cat"
print(type(s))
print(s[0], s[1], s[-1], s[-2])
print(s[0:3])
print(s[:-2])
print(s[:])

s = ' a cat '
print(s.strip())
print((s.split(' ')))
print(s.replace(' ', ''))
print(s.upper(), s.lower())
print(s.startswith('a'), s.strip().startswith('a'))
print(s.count('a'))
print(s.index('a'), s.strip().index('a'))

# Escape character: \n，\t
print("123\t456\n789\n10\t11")
