class Calculate():
    def __init__(self,number):
        self.number = number
    
    def addition(self):
        print(self.number+self.number)
    
    def subtraction(self):
        print(self.number-self.number)
        
    def multiplication(self):
        print(self.number*self.number)
        
    def division(self):
        print(self.number/self.number)
        
class Calculator():
    def __init__(self,number):
        self.number = number 
        self.obj = Calculate(self.number)
    
    def addition(self):
        self.obj.addition()
        
    def subtraction(self):
        self.obj.subtraction()
            
    def multiplication(self):
        self.obj.multiplication()
    
    def division(self):
        self.obj.division()

obj = Calculator(10)
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
