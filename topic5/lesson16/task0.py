class Cassa(object):

    def __init__(self, init_amount):
        self.amount = init_amount

    def top_up(self, X):
        self.amount += X

    def count_1000(self):
        return self.amount // 1000
    
    def take_away(self, X):
        if X > self.amount:
            raise ValueError("Not enough money")
        self.amount -= X