""" Create a Account class with methods"""
import math

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

     # This method gets the current balance of the account.
    def get_balance(self):
        """Gets the current balance of the account."""
        return self.balance

    # This method gets the current interest gained for the account.
    def get_interest(self):
        """Gets the current interest gained for the account."""
        return self.interest

    # def __eq__(self, other):
    #     """Overrides the default implementation of the equality operator."""
    #     if isinstance(other, Account):
    #         return math.isclose(self.balance, other.balance) and math.isclose(self.interest, other.interest)
    #     return False