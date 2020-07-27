class AttClass():
    class_att = "Class attributes"
    def __init__(self,instance_att):
        self.instance = instance_att

obj1 = AttClass(1)
obj2 = AttClass(2)

print(obj1.instance)
print(obj2.instance)
print(obj1.class_att)
print(obj2.class_att)
AttClass.class_att = 123 ## Change from "Class attributes" to 123
print(obj1.class_att) ## 123
print(obj2.class_att) ## 123
obj1.class_att = 321 # set class_att to 321 for obj1 
print(obj1.class_att) # 321
print(obj2.class_att) # 123 because it remains 123 same for obj2
