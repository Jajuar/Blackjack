from random import randint

class Cards():

    #Initialize calss
    def __init__(self):
        self.deck = [("Clubs","Ace"),("Clubs",2),("Clubs",3),("Clubs",4),("Clubs",5),("Clubs",6),("Clubs",7),("Clubs",8),("Clubs",9),("Clubs",10),("Clubs","Jack"),("Clubs","Queen"),("Clubs","King"),
                     ("Hearts","Ace"),("Hearts",2),("Hearts",3),("Hearts",4),("Hearts",5),("Hearts",6),("Hearts",7),("Hearts",8),("Hearts",9),("Hearts",10),("Hearts","Jack"),("Hearts","Queen"),("Hearts","King"),
                     ("Diamonds","Ace"),("Diamonds",2),("Diamonds",3),("Diamonds",4),("Diamonds",5),("Diamonds",6),("Diamonds",7),("Diamonds",8),("Diamonds",9),("Diamonds",10),("Diamonds","Jack"),("Diamonds","Queen"),("Diamonds","King"),
                     ("Spades","Ace"),("Spades",2),("Spades",3),("Spades",4),("Spades",5),("Spades",6),("Spades",7),("Spades",8),("Spades",9),("Spades",10),("Spades","Jack"),("Spades","Queen"),("Spades","King")]
        self.curr_card = ""

    #Print current card
    def __str__(self):
        return (f"[ {self.curr_card[1]} of {self.curr_card[0]} ]")

    #Draw a card from the deck and take it out from it
    def draw(self):
        pick = randint(0,51)
        dr = False
        while (dr == False):
            if (self.deck[pick] != 0):
                dr == True
                self.curr_card = self.deck[pick]
                self.deck[pick] = 0
                return self.curr_card
            else:
                pick = randint(0,51)

    def sum(self, hand, person):
        sum1 = 0
        sum2 = 0
        for suit,num in hand:
            if type(num) == str:
                if (num == "Jack" or num == "Queen" or num == "King"):
                    sum1 += 10
                    sum2 += 10
                elif (num == "Ace"):
                    sum1 += 1
                    sum2 += 11
            else:
                sum1 += num
                sum2 += num

        if (sum1 == sum2):
            print(f"\n{person} sum is {sum1} ")
            return (sum1,sum2)
        else:
            print(f"\n{person} sum is {sum1} or {sum2}")
            return (sum1,sum2)
