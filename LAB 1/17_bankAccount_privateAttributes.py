class BankAccount:
   def __init__(self , balance, accountNumber):
      self.__balance = balance
      self.__accountNumber = accountNumber

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def getBalance(self):
        return self.__balance
   
    def getAccountNumber(self):
        return self.__accountNumber
   
    def __str__(self):
        return "Account Number: " + str(self.__accountNumber) + " Balance: " + str(self.__balance)
   
# Create an object of the class
account = BankAccount(1000, 123456)
print(account.getBalance())
print(account.getAccountNumber())

account.deposit(500)
print(account.getBalance())

account.withdraw(200)
print(account.getBalance())

account.withdraw(2000)
print(account.getBalance())
 
   

