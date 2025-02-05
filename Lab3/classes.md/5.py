class Account:
    def __init__(self, balance):
        self.b = balance
    def deposit(self):
        self.deposit = int(input("Input deposit: "))
        self.b = self.deposit + self.b
        print("")
        print("You have succesfully topped:", self.deposit, "\n")
        print("Your activity is: ", self.b)

    def withdraw(self):
        self.withdraw = int(input("How much money do you want to withdraw: "))
        if self.withdraw <= self.b:
            self.b = self.b - self.withdraw
            print("You have succeslfully withdrawn money:", self.withdraw, "\n")
            print("Your activity is:", self.b, "\n")
        else:
            print("No, I will not give you more money than you have\n")
            return self.b

owner = input("Name: ")   #attributes
balance = int(input("Your balance: "))   #attributes
Acc = Account(balance)
print("What do you want to do: \n")
print("*  If to up the bank account enrter '+'")
print("*  If to withdraw money Enrter '-'\n")
print("*  To exit enter 'Exit' \n")
i = input()
if i == "+":
    Acc.deposit()
if i == "-":
    Acc.withdraw()
print("Name:", owner)
print("Ok, good bye")