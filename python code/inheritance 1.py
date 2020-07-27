class Parent():
    def __init__(self):
        print("Parent Class ")
        
    def altered(self):
        print("Parent alter")

class Child(Parent):
    def altered(self):
        print("Child alter")
        #super().altered()
        print("Child after suoer")

obj = Child()
obj.altered()
