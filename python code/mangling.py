''' When we use double underscore before ay class property, 
    the property prefixed with _<classname>. This process is
    called name mangling.
'''

class Test:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def show(self):
	print(self.__a, self.__b)


obj = Test(6, 5)
#print(obj.__a, obj.__b) --> This will occur AttributeError
obj.show()
print(obj._Test__a, obj._Test__b)
