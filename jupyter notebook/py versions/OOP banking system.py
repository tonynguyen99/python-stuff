class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        print("Account balanced has been updated: $", self.balance)
        
        
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance < withdraw_amount:
            print("You have insufficient funds | Balance Available: $%s" % self.balance)
        else:
            self.balance -= self.withdraw_amount
            print("Your account balance is now: $%s" % self.balance)
            
            
    def view_balance(self):
        self.show_details()
        print("Account balance: %s" % self.balance)