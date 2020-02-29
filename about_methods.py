# types of methods-
# instance (accessor{to access values}, mutator{to modify values}), class, static.


class Student:

    school = 'Oxford'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # class method
    @classmethod
    def get_school(cls):
        return cls.school

    # static method
    @staticmethod
    def info():
        print("This is a student class")


s1 = Student(10, 23, 56)
s2 = Student(23, 10, 40)
print(Student.get_school())
Student.info()
