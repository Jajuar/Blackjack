class Dealer():

    def __init__(self):
        self.hand = []

    def drop_hand(self):
        self.hand = []

    def print_hand():
        print("Dealer's hand: ")
        for suit,num in self.hand:
            print(f"[ {num} of {suit} ]")
