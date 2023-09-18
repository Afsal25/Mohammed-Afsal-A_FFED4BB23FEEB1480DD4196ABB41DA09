class BankAccount:

  def __init__(self, account_number, holder_name, initial_balance):
    self.__accounu_number = account_number
    self.__holder_name = holder_name
    self.__initial_balance = initial_balance

  def deposite(self, amount):
    self.__initial_balance += amount
    if amount > 0:
      return f"{amount} deposite after deposite {self.__initial_balance}"
    else:
      return f"invalite enter positive number"

  def withdraw(self, amount):
    self.__initial_balance -= amount
    if amount > 0 <= self.__initial_balance:
      return f"{amount} to withdraw after withdraw you get {self.__initial_balance}"
    else:
      return f"your balance is low"

  def check_balance(self):
    return f"your balance is {self.__initial_balance}"


dd = BankAccount(12345634534, "MOHAMMED AFSAL A", 1000)
print(dd.check_balance())
print(dd.deposite(500))
print(dd.withdraw(200))
print(dd.check_balance())
