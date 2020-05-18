class Point:
    a = 5
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def func(self):
        print(self)
        print(self.a)


p1 = Point(5,5)
p2 = Point(6,6)

p1.func()
print(p1)
p2.func()
print(p2)

