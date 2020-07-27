class Parent:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def method(self):
        return self.var1,self.var2


class Child:
    def __init__(self,var1,parent):
        self.var1 = var1
        self.parent = parent

    def method(self):
        print(self.var1)
        print(self.parent.method())


p_obj = Parent(1,2)
c_obj = Child(5,p_obj)
c_obj.method()

''' Aggregation implies a relationship
    where the child can exist independently of the parent.
'''
