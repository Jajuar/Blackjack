class Player():

    #Initialize
    def __init__(self, money, name):
        self.money = money
        self.hand = []
        self.name = name

    def bet(self, num):
        if (num > self.money):
            return False
        else:
            self.money -= num
            return True

    #if the player wins then it receives twice his bet
    def win(self, num):
        self.money += num*2

    #Print player balance and name
    def __str__(self):
        return f"{self.name} has {self.money} chips"

    def drop_hand(self):
        self.hand = []

    def print_hand():
        for suit,num in self.hand:
            print(f"[ {num} of {suit} ]")
