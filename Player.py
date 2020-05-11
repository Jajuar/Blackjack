class Player():

    #Initialize
    def __init__(self, money):
        self.money = money
        self.hand = []

    def bet(num):
        if (num > self.money):
            return False
        else:
            self.money -= num
            return True

    #if the player wins then it receives twice his bet
    def win(num):
        self.money += num*2
