class Class1():
    def __init__(self):
        print("object created from class 1");

    def override(self):
        print("override from class 1")
        

class Class2():
    def __init__(self):
        print("object created from class 2");

    def override(self):
        print("override from class 2")

class Class3(Class1,Class2):
    def __init__(self):
        print("object created from class 3")

    def override(self):
        super().override()
        

class Class4(Class2,Class1):
    def __init__(self):
        print("object created from class 4")

    def override(self):
        super().override()

obj = Class3()
obj.override()

obj = Class4()
obj.override()
