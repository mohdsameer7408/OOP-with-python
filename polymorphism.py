# Polymorphism types-
# duck typing, operator overloading, method overloading, method overriding

# about duck typing


# class PyCharm:
#
#     def execute(self):
#         print('compiling')
#         print("running")
#
#
# class VisualStudioCode:
#
#     def execute(self):
#         print("Spell check")
#         print('compiling')
#         print("running")
#
#
# class Laptop:
#
#     def code(self, ide):
#         ide.execute()
#
#
# ide = PyCharm()
# l1 = Laptop()
# l1.code(ide)
#
# ide = VisualStudioCode()
# l2 = Laptop()
# l2.code(ide)

# about operator overloading


# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         return Student(m1, m2)
#
#     def __str__(self):
#         return '{} {}'.format(self.m1, self.m2)
#
#
# s1 = Student(10, 20)
# s2 = Student(15, 19)
#
# s3 = s1 + s2
# print(s3.m2)
# print(s3)

# method overloading


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=0, b=0, c=0):
        s = a+b+c
        return s


print(Student(2, 4).sum(2, 5))

# method overriding


class A:

    def show(self):
        print("in A show")


class B(A):

    def show(self):
        print('in B show')


B().show()
