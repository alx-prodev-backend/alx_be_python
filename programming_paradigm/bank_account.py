# bank_account.py

class BankAccount:
    """ A simple bank account class with deposit , withdraw and display. """
    def __init__(self, initial_balance=0):
        """ initialize the  account with an optional"""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount into the account  """
        self.account_balance += amount

    def withdraw(self,amount ):
        """
        withdraw a positive amount if sufficient funds exist.
        Returns
            True if withdraw succeeds,
            Fals if insufficient funds
        """
        if amount <=  self.account_balance:
            self.account_balance -=amount
            return  True
        else:
            return False

    def display_balance(self):
        """ print the current balance in the required format . """
        print(f"Current Balance : ${self.account_balance}")