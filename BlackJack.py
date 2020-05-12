#Modules
from Cards import Cards
from Player import Player
from Dealer import Dealer

#components
import time

print("//////////////////////////////////////////////")
print("//            21 Blackjack                  //")
print("//////////////////////////////////////////////")
print("\nWelcome, Player 1!")
print("Read the instructions below to play:\n")
print("OBJECTIVE: Beat the Dealer (computer) in a 21 Blcackjack game")
print("* Player initially receives 2 cards facing up")
print("* Dealer draws 2 cards one facing up and the other facing down")
print("* Then Player draws first until he stops or bursts")
print("* If the player stops before busting then it´s Dealer's turn")
print("* Dealer draws until it's equal or above 17")
print("* If the Dealer pass 21 then the Player wins")
print("* If no one passes 21, then the one with the closest sum to 21 wins")
print("* The House pays double each win")
print("\n/////////SPECIAL CARDS VALUES////////")
print("* ACE  = Player/Dealer chooses either 1 or 11")
print("* JACK-QUEEN-KING = 10")
print("/////////////////////////////////////\n")

start = ""
stop = False
end = False
p1sum1 = 0
p1sum2 = 0
dlsum1 = 0
dlsum2 = 0
hit = True
h = ""
p1busted = False
dlbusted = False
pa = ""
p1bj = False
dlbj = False
p1lost = False
p1max = 0
dlmax = 0

def restart_game():
    global stop
    global end
    global p1sum1
    global p1sum2
    global dlsum1
    global dlsum2
    global hit
    global h
    global p1busted
    global dlbusted
    global pa
    global p1bj
    global dlbj
    global p1lost
    global p1max
    global dlmax

    stop = False
    end = False
    p1sum1 = 0
    p1sum2 = 0
    dlsum1 = 0
    dlsum2 = 0
    hit = True
    h = ""
    p1busted = False
    dlbusted = False
    pa = ""
    p1bj = False
    dlbj = False
    p1lost = False
    p1max = 0
    dlmax = 0
    p1.hand = []
    dl.hand = []

#Check if the player wants to play
while (start.upper() != "Y" and start.upper()  != "N"):
    start = input("\nWanna play?(Y/N):  ")

if (start.upper() == "Y"):

    #Initialize Player and Dealer to place a bet
    name = input("\nWhat is your name?  ")
    while True:
        try:
            money = int(input("\nHow much money (chips) do you want to put in? (Integer numbers):  "))
        except:
            print("\nWhoops! This is not an integer number. Try again.")
            continue
        else:
            print(f"\nYou introduced {money} chips")
            break

    p1 = Player(money, name)
    dl = Dealer()

    #Start the game and loop until player runs out of money or leaves the table
    while end == False:
        #Clean variables
        restart_game()
        #inform current money
        print(p1)

        #Create the Cards obejct to "shuffle"
        mycards = Cards()

        #The player places the bet
        while True:
            try:
                bet = int(input("\nHow much money do you want to bet? (Integer numbers):  "))
            except:
                print("\nWhoops! This is not an integer number. Try again.")
                continue
            else:
                if (p1.bet(bet)):
                    break
                else:
                    print("\nYou don't have enough chips")
                    #print(f"Your current balance is {p1.money} chips")

        #Print player's balance
        print(f"\nYour current balance is {p1.money} chips in your pocket & {bet} chips on the table ")

        time.sleep(2)

        #Beggin draw
        print("\n//////////Let's Beggin!/////////////")
        print("\nYour cards: ")

        #The player receives 2 Cards
        for _ in range(2):
            p1.hand.append(mycards.draw())
            #Print Player's cards
            print(mycards)
        time.sleep(2)

        print("\nDealer's cards: ")
        #Dealer draws
        for _ in range(2):
            dl.hand.append(mycards.draw())
            #Print Dealer's card
            if (len(dl.hand) == 2):
                print(mycards)
            else:
                #Hidden card
                print("[///////]")

        time.sleep(2)
        #Let know how much does de user have in his hand
        (p1sum1,p1sum2) = mycards.sum(p1.hand, p1.name)
        print(f"\n////////////{p1.name}'s Turn////////////")
        #Now the player can draw more cards or stop
        while (hit):
            if(p1sum1 == 21 or p1sum2 == 21):
                hit = False
                p1bj = True
                print("21!!!")
            else:
                while (h.upper() != "Y" and h.upper() != "N"):
                    h = input("\nDo you want another card?(Y/N): ")
                if (h.upper() == "Y"):
                    p1.hand.append(mycards.draw())
                    p1.print_hand()
                    (p1sum1,p1sum2) = mycards.sum(p1.hand, p1.name)
                    time.sleep(2)
                    if (p1sum1 > 21 and p1sum2 > 21):
                        hit = False
                        p1busted = True
                        print("BUSTED!!!")
                    elif(p1sum1 == 21 or p1sum2 == 21):
                        hit = False
                        p1bj = True
                        print("21!!!")
                    else:
                        h = ""
                else:
                    hit = False

        #Check if player busted or not
        if (p1busted):
            if (p1.money == 0):
                print("\nOh! those were your last chips :(")
                end = True
            else:
                while(pa.upper() != "Y" and pa.upper() != "N"):
                    pa = input("\nDo you wanna keep playing?(Y/N):  ")
                if (pa.upper() == "Y"):
                    end = False
                else:
                    end = True
        #It's Dealer's turn
        else:
            time.sleep(2)
            print("\n////////////Dealer's turn////////////")
            #Discover his faced down card first
            dl.print_hand()
            #Check if initial sum >= 17
            (dlsum1,dlsum2) = mycards.sum(dl.hand, "Dealer")
            while stop == False:
                if(dlsum1 == 21 or dlsum2 == 21):
                    stop = True
                    dlbj = True
                    print("21!!!")
                else:
                    if (dlsum1 >= 17 and dlsum2 >= 17):
                        print("\nDealer can't draw more cards")
                        stop = True
                    else:
                        #Draw more cards
                        dl.hand.append(mycards.draw())
                        dl.print_hand()
                        #Check that the Dealer does not bust
                        (dlsum1,dlsum2) = mycards.sum(dl.hand, "Dealer")
                        time.sleep(2)
                        if (dlsum1 > 21 and dlsum2 > 21):
                            stop = True
                            dlbusted = True
                            print("BUSTED!!!")
                        elif(dlsum1 == 21 or dlsum2 == 21):
                            stop = True
                            dlbj = True
                            print("21!!!")
                        else:
                            continue

            time.sleep(2)
            #CHECK RESULTS!!!!!!!!
            print("\n//////////////////RESULTS//////////////////")
            #Check if dealer waas busted
            if (dlbusted == True):
                print("\nWinner winner chicken dinner!")
                p1.win(bet)
            else:
                #Both have 21
                if(p1bj == True and dlbj == True):
                    print("\nIt's a Tie!")
                    p1.tie(bet)
                #Player1 wins with a 21
                elif(p1bj == True and dlbj == False):
                    print("\nWinner winner chicken dinner!")
                    p1.win(bet)
                #Dealer wins with a 21
                elif(p1bj == False and dlbj == True):
                    print("\nThe House always wins!")
                    print("\nBetter luck next time Malarkey")
                    p1lost = True
                #Nobody has a 21
                else:
                    #Determine max sum without busting
                    #Player1
                    if(p1sum1 >= p1sum2):
                        p1max = p1sum1
                    else:
                        if(p1sum2 > 21):
                            p1max = p1sum1
                        else:
                            p1max = p1sum2
                    #Dealer
                    if(dlsum1 >= dlsum2):
                        dlmax = dlsum1
                    else:
                        if(dlsum2 > 21):
                            dlmax = dlsum1
                        else:
                            dlmax = dlsum2

                    #Decide winner
                    if (p1max > dlmax ):
                        print(f"\nPlayer 1 {p1max} > Dealer {dlmax}")
                        print("\nWinner winner chicken dinner!")
                        p1.win(bet)
                    elif(p1max < dlmax):
                        print(f"\nPlayer 1 {p1max} < Dealer {dlmax}")
                        print("\nThe House always wins!")
                        print("\nBetter luck next time Malarkey")
                        p1lost = True
                    else:
                        print("\nIt's a Tie!")
                        p1.tie(bet)


        #Play again?
        if (end == False):
            if (p1.money == 0 and p1lost == True):
                print("\nOh! those were your last chips :(")
                end = True
            else:
                while(pa.upper() != "Y" and pa.upper() != "N"):
                    pa = input("\nDo you wanna keep playing?(Y/N):  ")
                    time.sleep(2)
                if (pa.upper() == "Y"):
                    end = False
                else:
                    end = True

        #Farewell
        if (end == True):
            time.sleep(2)
            print("\nThank you for playing :)!")

else:
    print("\nSee you next time! ;) Bye!")
