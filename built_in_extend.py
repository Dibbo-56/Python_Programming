class Contact(list):
    def __init__(self):
        print("List Created")
        

class Test:
    C = Contact()
    def __init__(self,num):
        self.C.append(int(num))


obj1 = Test(1)
obj2 = Test(2)
obj3 = Test(3)

for i in Test.C:
    print(i)
