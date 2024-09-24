class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self,amount):
    self.balance = self.balance - amount
    return self.balance
  def display_balance(self):
    print(f"${self.balance}")
  
checking_account = BankAccount("Mikloven", "Muhadri", 170307099, "Barclays", 8540, 20)
checking_account.deposit(96)
checking_account.display_balance()
checking_account.withdraw(25)
checking_account.display_balance()