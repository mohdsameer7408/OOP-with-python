# __init__ method gets executed by default
class Computer:
    d = 6

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"{self.cpu}, {self.ram}, 1TB")


comp1 = Computer('i5', '8gb')
comp1.config()
# Computer.config(comp1)
c2 = Computer('i7', '16gb')
Computer.d = 7
print(comp1.d, c2.d)
