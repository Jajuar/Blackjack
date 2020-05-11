import Cards
import player
import Dealer

print("//////////////////////////////////////////////")
print("//            21 Blackjack                  //")
print("//////////////////////////////////////////////")
print("\n Welcome, player one!")
print("Read the instructions below to play:\n")
print("OBJECTIVE: Beat the Dealer (computer) in a 21 BJ game")
print("* Player initially receives 2 cards face up")
print("* Dealer draws 2 cards one face up and the other face down")
print("* Then Player draws first until he stops or bursts")
print("* If the player stops before busting then it´s Dealer's turn")
print("* Dealer draws until it's equal or above 17")
print("* If the Dealer pass 21 then the Player wins")
print("* If no one passes 21, then the one with the closest sum to 21 wins")
print("SPECIAL CARDS VALUES: ")
print("ACE  = Player/Dealer chooses either 1 or 11")
print("JACK-QUEEN-KING = 10")

start = pass
end = False

#Check if the player wants to play
while (start.upper() != "Y" or start.upper()  != "N":
    start = input("Wanna play?(Y/N):  ")

if (start.upper() == "Y"):

    #Initialize Player and Dealer to place a bet
    name = input("What is your name?")
    while True:
        try:
            money = int(input("How much money(chips) do you want to put in? (Integer numbers)"))
        except:
            print("Whoops! This is not an integer number")
            continue
        else:
            print(f"You introduced {money} chips")
            break

    p1 = Player(money, name)
    dl = Dealer()

    #Start the game and loop until player runs out of money or leaves the table
    while end == False:

        #inform current money
        print(p1)

        #Create the Cards obejct to "shuffle"
        mycards = Cards()

        #The player places the bet
        while True:
            try:
                bet = int(input("How much money do you want to bet? (Integer numbers)"))
            except:
                print("Whoops! This is not an integer number")
                continue
            else:
                if (p1.bet(bet)):
                    break
                else:
                    print("You don't have enough chips")
                    #print(f"Your current balance is {p1.money} chips")

        #Print player's balance
        print(f"Your current balance is {p1.money} chips on your pocket & {bet} chips on the table ")

        #Beggin draw
        print("Your cards: ")

        #The player receives 2 Cards
        for _ in xrange(2):
            p1.hand.append(mycards.draw())
            #Print Player's cards
            print(mycards)

        #Dealer draws
        for _ in xrange(2):
            dl.hand.append(mycards.draw())
            #Print Dealer's card
            if (len(dl.hand) == 2:)
                print(mycards)
            else:
                #Hidden card
                print("[********]")

        #Now the player can draw more cards or stop
        hit = True
        while (hit):
            h = pass
            while (h.upper() != "Y" or h.upper() != "N"):
                h = input("Do you want another card?(Y/N): ")
            if (h.upper() == "Y"):
                pass









else:
    print("See you next time! ;) Bye!")
