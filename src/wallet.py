########################################################################
# CUSTOM EXCEPTION
########################################################################
class InsufficientAmount(Exception):
    pass

########################################################################
# CLASS TO IMPLEMENT
########################################################################

class Wallet(object):

    def __init__(self, initial_amount:int =0):
        self.balance = initial_amount

    def spend_cash(self, amount:int):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount:int):
        self.balance += amount