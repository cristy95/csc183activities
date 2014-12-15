"DOCSTRING"

class Bank(object):
    """Creates the object Bank"""
    def __init__(self):
        """Initialize an empty list of accounts"""
        self.accounts = {}

    def add_account(self, account):
        """Adds an account to the list"""
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        """gets information of a certain account"""
        return self.accounts.get(account_number)