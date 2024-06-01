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
   

