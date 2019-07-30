#!/usr/bin/python3

class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化
x = MyClass()

# 访问类的属性和方法
print(x.i)
print(x.f())


class Complex:
    # self表示类的实例而非类
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


# 类的方法
class People:
    name = ''
    age = 0
    # 定义私有属性,私有属性在外无法赋值访问
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说:我 %d 岁." % (self.name, self.age))


# 实例化类
p = People('mistray', 24, 30)
p.speak()


# 继承->单继承
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类方法
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写父类方法
    def speak(self):
        print("%s 说:我 %d 岁了,我再读 %d 年级 " % (self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()


# 继承->多继承准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s , 我是一个演说家, 我演讲的题目是 %s" % (self.name, self.topic))


# 继承->多继承

class simple(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = simple("tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
