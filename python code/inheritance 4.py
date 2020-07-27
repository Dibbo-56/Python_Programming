class Parent:
    def __init__(self,var1,var2,s):
        self.var1 = var1
        self.var2 = var2
        print(s)


class Child(Parent):
    def __init__(self,var3,s):
        super().__init__(4,5,s)  # Equivalent --> super(Child, self).__init__(4,5,s)
        self.var3 = var3


obj_p = Parent(1,2,"Parent")
obj_c = Child(3,"Child")

print(obj_p.var1, obj_p.var2)
print(obj_c.var1, obj_c.var2, obj_c.var3)
