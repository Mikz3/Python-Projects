import unittest
from Bank_Account import BankAccount

class TestBankAccount(unittest.TestCase):
    # Set Up Method
    def setUp(self):
        self.account = BankAccount(100)
    # Set Down Method
    def tearDown(self):
        self.account = None
    
    # Testing Bank Operations
    def test_Initial_Balance(self):
        self.assertEqual(self.account.balance, 100)
    # Testing Deposit
    def test_Deposit_Positive_Amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    # Value Error
    def test_Deposit_Zero_Amount(self):
        with self.assertRaises(ValueError):
          self.account.deposit(0)
    # Value Error With Negative Values
    def test_Deposit_Negative_Amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-30)
    # Testing Withdraw
    def test_Withdraw_Amount(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)
    # Testing Withdrawing Insufficiant Amount
    def test_Withdraw_Insufficient_Amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
    # Testing Withdrawing Zero Amount
    def test_Withdrawing_Zero_Amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
    # Testing Withdrawing Negative Amount
    def test_Withdrawing_Negative_Amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-35)

if __name__ == "__main__":
  unittest.main()