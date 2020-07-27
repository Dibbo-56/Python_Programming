class Notebook:
    def __init__(self, date, string, tags):
        self.date = date
        self.string = string
        self.tags = tags
    
    def modify(self):
        m_string = input()
        self.string += " "+m_string


obj_l = []

obj1 = Notebook("26/12/2010", "Hi there", ["Normal", "Greetings"])
obj2 = Notebook("26/12/2012", "Hello there", ["Normal", "Greetings"])

obj_l.append(obj1)
obj_l.append(obj2)

obj1.modify()

for i in obj_l:
    print(i.string)
