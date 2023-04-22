import unittest
from account import *

class Test(unittest.account):
    def init(self, name):
        self.p1 = name('Nick', 100)
        self.p2 = name('Jack', 1000)
        self.assertEqual(self.p1.get_name(), 'Nick')
        self.assertEqual(self.p1.get_account_balance(), 100)
        self.assertEqual(self.p2.get_name(), 'Jack')
        self.assertEqual(self.p2.get_account)

    def deposit(self, amount):
        self.assertEqual(self.amount(100))
        self.assertEqual(self.amount(-2))

    def withdrawl(self, amount):
        self.assertEqual(self.amount(10))
        self.assertEqual(self.amount(-10))

    def get_balance(self):
        self.assertEqual(self.get.account_balance())

    def get_account(self):
        self.assertEqual(self.get_account())

if __name__ == '__main__':
    unittest.account()

