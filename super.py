class Vehicle():
    def __init__(self,name):
        self.name = name
        print(self.name," has an engine and have wheels")

class Four_wheel_vehicle(Vehicle):
    def __init__(self,name):
        self.name = name
        print(self.name," have 4 wheels")
        super().__init__(self.name)

class Car(Four_wheel_vehicle):
    def __init__(self,name):
        self.name = name
        print(self.name, " have 4 wheels but small in size")
        super().__init__(self.name)

class Bus(Four_wheel_vehicle):
    def __init__(self,name):
        self.name = name
        print(self.name, "have 4 wheels but large in size")
        super().__init__(self.name)

class Hiace(Car,Bus):
    def __init__(self,name):
        self.name = name
        print(self.name,"is Car but small Bus")
        super().__init__(self.name)

obj = Hiace("Toyota")
