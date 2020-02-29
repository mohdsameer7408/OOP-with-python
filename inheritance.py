# A sub-class calls the constructor of super class by default, if sub-class don't have that constructor method
# to include init of both the class inside sub-class we need to have super().__init__() in the constructor of sub-class
# like -
# class Prototype(Mammals):
#
#     def __init__(self):
#         super().__init__()
#     def deer(self):
#         print("Its a deer")

# inheritance works from left to right as per MRO (Method Resolution Order)


class Mammals:

    def bird(self):
        print("its a bird")

    def lion(self):
        print("Its a lion")


# single level inheritance
class Prototype(Mammals):

    def deer(self):
        print("Its a deer")


# Multi level inheritance
class Model(Prototype):
    pass


class Lizards:

    def frog(self):
        print("Its a frog")


# Multiple inheritance
class All(Model, Lizards):
    pass


a = Prototype()
a.bird()

b = Model()
b.lion()

c = All()
c.frog()
