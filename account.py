class Account:
    def __init__(self, name):
        account_name = 'name'
        account_balance = 0

        def deposit(self, amount):
            if amount > 0:
                self.account_balance += amount
                return True
            else:
                return False

        def withdraw(self, amount):
            if self.account_balance <= amount:
                return False
            elif amount < 0:
                return False
            else:
                self.account_balance -= amount
                return True

        def get_balance(self):
            return self.account_balance

        def get_name(self):
            return self.accout_name


