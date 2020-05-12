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

start = "M"
stop = False
end = False
p1sum1 = 0
p1sum2 = 0
dlsum1 = 0
dlsum2 = 0
hit = True
h = "M"
p1busted = False
dlbusted = False
pa = "M"
p1bj = False
dlbj = False
p1lost = False
p1max = 0
dlmax = 0

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
                print("[///////]")

        #Now the player can draw more cards or stop
        while (hit):
            #Let know how much does de user have in his hand
            print_sum()
            while (h.upper() != "Y" or h.upper() != "N"):
                h = input("Do you want another card?(Y/N): ")
            if (h.upper() == "Y"):
                p1.hand.append(mycards.draw())
                p1.print_hand()
                (p1sum1,p1sum2) = mycards.print_sum()
                if (p1sum1 > 21 and p1sum2 > 21):
                    hit = False
                    p1busted = True
                    print("BUSTED!!!")
                elif(p1sum1 == 21 or p1sum2 == 21):
                    hit = False
                    p1bj = True
                    print("21!!!")
                else:
                    continue
            else:
                hit = False

        #Check if player busted or not
        if (p1busted):
            if (p1.money == 0):
                print("Oh! that was your last chip(s) :(")
                end == True
            else:
                while(pa.upper() != "Y" or pa.upper() != "N"):
                    pa = input("Do you wanna keep playing?(Y/N):  ")
                if (pa == "Y"):
                    end = False
                else:
                    end = True
        #It's Dealer's turn
        else:
            #Discover his faced down card first
            dl.print_hand()
            #Check if initial sum >= 17
            (dlsum1,dlsum2) = mycards.print_sum()
            while stop == False:
                if (dlsum1 >= 17 and dlsum2 >= 17):
                    print("Dealer can't draw more cards")
                    stop == True
                else:
                    #Draw more cards
                    dl.hand.append(mycards.draw())
                    dl.print_hand()
                    #Check that the Dealer does not bust
                    (dlsum1,dlsum2) = mycards.print_sum()
                    if (dlsum1 > 21 and dlsum2 > 21):
                        stop = True
                        dlbusted = True
                        print("BUSTED!!!")
                    elif(p1sum1 == 21 or p1sum2 == 21):
                        stop = True
                        dlbj = True
                        print("21!!!")
                    else:
                        continue

            #CHECK RESULTS!!!!!!!!
            print("////////////RESULTS//////////////////")
            #Both have 21
            if(p1bj == True and dlbj == True):
                print("It's a Tie!")
                p1.tie(bet)
            #Player1 wins with a 21
            elif(p1bj == True and dlbj == False):
                print("Winner winner chicken dinner!")
                pl.win(bet)
            #Dealer wins with a 21
            elif(p1bj == False and dlbj == True):
                print("The House always wins!")
                print("Better luck next time Malarkey")
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
                if (p1max > dlmax):
                    print("Winner winner chicken dinner!")
                    pl.win(bet)
                elif(p1max < dlmax):
                    print("The House always wins!")
                    print("Better luck next time Malarkey")
                    p1lost = True
                else:
                    print("It's a Tie!")
                    p1.tie(bet)


        #Play again?
        if (p1.money == 0 and p1lost == True):
            print("Oh! that was your last chip(s) :(")
            end == True
        else:
            while(pa.upper() != "Y" or pa.upper() != "N"):
                pa = input("Do you wanna keep playing?(Y/N):  ")
            if (pa == "Y"):
                end = False
            else:
                end = True

        if (end == True):
            print("Thank you for playing :)!")

else:
    print("See you next time! ;) Bye!")
