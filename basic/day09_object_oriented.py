# 面向对象 Object Oriented: 对应现实世界的对象
# 类 Class
#   某一类对象的总称, 可以有不同的层次，例如动物、鸟类、汽车等
# 对象 Object
#   具体的一个对象，例如一只喜鹊、一辆SUV等
#   对象是类的实例
import math


class MyClass:
    name = '1'
    age = 10

    __private = ''

    # 构造函数，用于创建对象时赋值内部属性
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def get_private(self):
        return self.__private

    def set_private(self, private_value):
        self.__private = private_value

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


class Graph:
    name = ''
    area = 100

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return self.area


# extend
class Rectangle(Graph):
    def __init__(self, name, width, height):
        Graph.__init__(self, name)  # super().__init__(self, name)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Squire(Rectangle):
    def __init__(self, name, length):
        Rectangle.__init__(self, name, length, length)


class Circle(Graph):
    def __init__(self, name, radius):
        Graph.__init__(self, name)  # self.name = name
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


if __name__ == '__main__':
    # print(type(MyClass))
    # print(MyClass)
    # print()

    # x = MyClass()
    #
    # MyClass.name = 'xxx'
    # MyClass.age = -1
    #
    # print(x.name, x.age)
    # print(MyClass.name, MyClass.age)

    # x.set_private('abc')
    # print(x.name, x.age, x.get_private())

    rectangle = Rectangle('rectangle', 3, 4)
    print(rectangle.name, rectangle.get_area())

    squire = Squire('squire', 2)
    print(squire.name, squire.get_area())

    circle = Circle('circle', 3)
    print(circle.name, circle.get_area())

    # 调用父类的方法
    print(super(Circle, circle).get_area())
