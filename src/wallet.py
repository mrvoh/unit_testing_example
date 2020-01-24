########################################################################
# CUSTOM EXCEPTION
########################################################################


########################################################################
# CLASS TO IMPLEMENT
########################################################################


class Wallet(object):

    def __init__(self, initial_amount):
        pass

    def spend_cash(self, amount):
        raise NotImplementedError

    def add_cash(self, amount):
        raise NotImplementedError