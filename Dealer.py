class Dealer():

    def __init__(self):
        self.hand = []

    def drop_hand(self):
        self.hand = []

    def print_hand():
        for suit,num in self.hand:
            print(f"[ {num} of {suit} ]")
