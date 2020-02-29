class Car:

    def __init__(self, speed):
        self.__speed = speed

    def set_speed(self, val):
        self.__speed = val

    def get_speed(self):
        return self.__speed


c = Car(300)
c.set_speed(200)
print(c.get_speed())
# hey
