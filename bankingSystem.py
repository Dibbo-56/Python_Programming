from random import randint

class Account:
    
    def createAccount(self):
        pass
    
    def authenticate(self):
        pass
    
    def withdraw(self):
        pass
    
    def deposite(self):
        pass
    
    def displaybalance(self):
        pass
    

class SavingAccount(Account):
    
    def __init__(self):
        self.savingAccounts = dict()
        
    def createAccount(self, name, initialDeposite):
        self.accountNumber = randint(10000,99999)
        self.savingAccounts[int(self.accountNumber)] = [name,int(initialDeposite)]
        print(self.savingAccounts[self.accountNumber])
        print("Your account nuber is %d" %(self.accountNumber))
    
    def authenticate(self, name, accountNumber):
        accountNumber = int(accountNumber)
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
            return True
        else:
            print("Authentication Failed")
            return False
    
    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdraw Successful")
            self.displaybalance(self.accountNumber)
        
    def deposite(self,depositeAmount):
        self.savingAccounts[self.accountNumber][1] += depositeAmount
        print("Deposite Successful")
        self.displaybalance(self.accountNumber)
        
    
    def displaybalance(self,accountNumber):
        print("Available amount of money %d" %self.savingAccounts[self.accountNumber][1])

savingAccount = SavingAccount()

while True:
    print("Press 1 for openning account")
    print("Press 2 for accessing account")
    print("Press 3 for exit")
    
    userChoice = int(input())
    
    if userChoice == 1:
        name = input("Enter your name ")
        initialDeposite = input("Enter your initial deposite ")
        savingAccount.createAccount(name,initialDeposite)
    elif userChoice == 2:
        name = input("Enter your name ")
        accountNumber = input("Enter your account number ")
        status = savingAccount.authenticate( name, accountNumber)
        if status == True:
            while True:
                print("Press 1 for withdraw")
                print("Press 2 for deposite")
                print("Press 3 for balance check")
                print("Press 4 for exit")
                
                userChoice = int(input()) 
                
                if userChoice == 1:
                    withdrawAmount = int(input("Enter your withdraw amount "))
                    savingAccount.withdraw(withdrawAmount)
                elif userChoice == 2:
                    depositeAmount = int(input("Enter your deposite amount "))
                    savingAccount.deposite(depositeAmount)
                elif userChoice == 3:
                    savingAccount.displaybalance(accountNumber)
                elif userChoice == 4:
                    break
    else:
        break
        
        
