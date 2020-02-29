class Student:

    def __init__(self, name):
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print(self.name)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i3'
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)


# to create object of inner class
obj = Student('abc').lap
obj.show()
# another way
Student.Laptop().show()
# another way
Student('xyz').show()
