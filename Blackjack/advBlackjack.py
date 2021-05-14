import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def addPlayerCard(playerCards, cards):
    playerCards.append(random.choice(cards))

def addDealerCard(dealerCards, cards):
    dealerCards.append(random.choice(cards))

def addSum(hand):
    totalsum = 0
    hand2 = []
    for card in hand:
        if(card == 'A'):
            hand2.append(card)
            hand2.remove(card)
        else:
            hand2.append(card)

    for cards in hand2:
        if(cards == 'A'):
            hand2.append('A')
            hand2.remove('A')
        if(cards == 'J' or cards == 'K' or cards == 'Q'):
            totalsum += 10
        elif(cards == 'A'):
            if(totalsum + 11 <= 21):
                totalsum += 11
            else:
                totalsum += 1
        else:
            totalsum += cards
    return totalsum 

def showDealerHand(dealerCards):
    print("Dealer's hand: [X,", str(dealerCards[1]) + "]")

def showPlayerHand(playerCards):
    print("Player's hand: [" + str(playerCards[0]) + ", " + str(playerCards[1]) + "]")

def checkBlackjack(cards):
    flag1 = 0
    flag2 = 0
    if(cards[0] == 'A' or cards[1] == 'A'):
        flag1 += 1
        if(cards[0] == 'J' or cards[1] == 'J' or cards[0] == 'K' or cards[1] == 'K' or cards[0] == 'Q' or cards[1] == 'Q'):
            flag2 += 1
    if(flag1 + flag2 == 2):
        return True
    else:
        return False

def handCount(hand):
    handCount = len(hand)
    return handCount

def hitOrStand(playerCards, dealerCards, cards, fiveHandRule):
    i = 0
    while(i != 2):
        hitstand = str(input("\nDo you want to hit or stand?\n")).lower()
        if(hitstand[0] == "h"):
            addPlayerCard(playerCards, cards)
            flag1 = addSum(playerCards)
            flag2 = handCount(playerCards)
            clear()
            print("Dealer's hand: [X,", str(dealerCards[1]) + "]")
            print("Player's hand: " + str(playerCards))

            if(flag1 > 21):
                print("\nYOU BUSTED!")
                time.sleep(2)
                return True
            elif(flag2 >= 5 and flag1 <= 21):
                fiveHandRule.append("PASS")
                return True
        if(hitstand[0] == "s"):
            return True

def dealerCheck(dealerSum, dealerCards, cards, playerCards):
    if(dealerSum <= 16):
        print("Dealer's hand: " + str(dealerCards))
        print("Player's hand: " + str(playerCards) + "\n")
        print("_________________________________________________\n")
        print("The Dealer's Cards' Total Sum do not exceed 16.")
        print("The Dealer Hits!")
        addDealerCard(dealerCards, cards)
        dealerSum = addSum(dealerCards)
        time.sleep(2)
        return dealerSum

def blackjackCard(playerCards, dealerCards):
    print("You Got a Blackjack!\n")
    time.sleep(1)

    print("Revealing Dealer's Hand...")
    time.sleep(1)
    print("Dealer's hand: " + str(dealerCards))
    print("Player's hand: " + str(playerCards) + "\n")

    if(checkBlackjack(dealerCards)):
        print("The Dealer Also Has a Blackjack!")
        return 8
    else:
        print("The Dealer Does Not Have a Blackjack.")
        return 9

def winLose(pSum, dSum, pHandCount):
    if(pSum > dSum and pSum <= 21):
        return 1
    elif(dSum > pSum and dSum <= 21):
        return 2
    elif(pHandCount >= 5 and pSum <= 21):
        return 3
    elif(dSum == pSum and pSum <= 21 and dSum <= 21):
        return 4
    elif(pSum > 21 and dSum <= 21):
        return 5
    elif(dSum > 21 and pSum <= 21):
        return 6
    elif(pSum > 21 and dSum > 21):
        return 7

def gameEnd(result):
    if(result == 1):
        print("\nCongratulations, You Won! Your Cards' Total Sum Is Higher Than The Dealer's.")
        return 1
    elif(result == 2):
        print("\nYou Lost! The Dealer's Cards' Total Sum Is Higher Than Your's.")
        return 2
    elif(result == 3):
        print("\nCongratulations, You Won! You Have a 5 Card Hand Without Busting, Winning by 5-Card Charlie.")
        return 1
    elif(result == 4):
        print("\nIt's a Push! Your Cards' Total Sum Is The Same As The Dealer's!")
        return 3
    elif(result == 5):
        print("\nYou Lost! You Busted but The Dealer Did Not. The Total Sum of Your Cards Exceeded 21.")
        return 2
    elif(result == 6):
        print("\nCongratulations, You Won! The Dealer Busted but You Did Not. The Total Sum of The Dealer's Cards Exceeded 21.")
        return 1
    elif(result == 7):
        print("\nIt's a Push! Both Parties Busted. Both Parties' Total Sum of Their Respective Cards Exceeded 21.")
        return 3
    elif(result == 8):
        print("\nIt's a Push! Both Parties Have a Blackjack!")
        return 3
    elif(result == 9):
        print("\nCongratulations, You Won! You Have a Blackjack but The Dealer Does Not!")
        return 1

def gameEnd2(result):
    if(result == 1 or result == 3 or result == 6 or result == 9):
        return 1
    if(result == 2 or result == 5):
        return 2
    if(result == 4 or result == 7 or result == 8):
        return 3
    
def Blackjack():
    clear()
    cards = ['A','J','K','Q', 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dealerCards = []
    playerCards = []

    addPlayerCard(playerCards, cards)
    addPlayerCard(playerCards, cards)
    addDealerCard(dealerCards, cards)
    addDealerCard(dealerCards, cards)
    showDealerHand(dealerCards)
    showPlayerHand(playerCards)
    checkBlackjack(playerCards)
    checkBlackjack(dealerCards)

    blackjack = False
    if(checkBlackjack(playerCards)):
        blackjack = True

    fiveHandRule = []
    if(blackjack == False):
        while(hitOrStand(playerCards, dealerCards, cards, fiveHandRule) != True):
            hitOrStand(playerCards, dealerCards, cards, fiveHandRule)

        if(len(fiveHandRule) <= 0):
            clear()
            print("Revealing Dealer's Hand...")
            time.sleep(1)
            dSum = addSum(dealerCards)
            if(dSum <= 16):
                while(dSum <= 16):
                    dealerCheck(dSum, dealerCards, cards, playerCards)
                    dSum = addSum(dealerCards)
            
            if(dSum > 16):
                print("Dealer's hand: " + str(dealerCards))
                print("Player's hand: " + str(playerCards))
            if(dSum > 21):
                print("\nTHE DEALER BUSTED!")
                time.sleep(2)

            pSum = addSum(playerCards)
            dSum = addSum(dealerCards)
            pHandCount = handCount(playerCards)

            winLose(pSum, dSum, pHandCount)

            result = winLose(pSum, dSum, pHandCount)

            gameEnd(result)
        else:
            print("Five-Hand Charlie!")
            time.sleep(2)
            result = 3
            gameEnd(result)
    else:
        result = blackjackCard(playerCards, dealerCards)
        gameEnd(result)

    input("Input any key to continue.\n")
    return result

def endgame(result, gamelog):
    clear()
    print("The Match Has Been Concluded.")
    flag = gameEnd2(result)
    if(flag == 1):
        print("Result: WIN")
        gamelog.append('W')
    elif(flag == 2):
        print("Result: LOSS")
        gamelog.append('L')
    elif(flag == 3):
        print("Result: TIE")
        gamelog.append('T')
    input("Input any key to continue.\n")
    clear()

def lobby(gamelog):
    totalgames = len(gamelog)
    totalwins = 0
    totallosses = 0
    totalties = 0
    for game in gamelog:
        if(game == 'W'):
            totalwins += 1
        elif(game == 'L'):
            totallosses += 1
        elif(game == 'T'):
            totalties += 1
    winrate = (2 * totalwins + totalties) / (2 * totalgames) * 100
    winrate = round(winrate, 2)
    
    print("YOUR STATISTICS")
    print("_________________________________________________\n")
    print("TOTAL GAMES: " + str(totalgames))
    print("WINS: " + str(totalwins))
    print("LOSSES: " + str(totallosses))
    print("TIES/PUSHES: " + str(totalties) + "\n")
    print("YOUR WINRATE: " + str(winrate) + "%")
    print("_________________________________________________\n")

gamelog = []
print("Welcome to Darrance's Blackjack. Have fun!")
time.sleep(2)

def main():
    result = Blackjack()
    endgame(result, gamelog)
    lobby(gamelog)
    option = input("Would you like to play again? (Y/N)\n").lower()
    if(option[0] == 'y'):
        main()
    elif(option[0] == 'n'):
        clear()
        print("Thank you for playing Darrance's Blackjack!")
        input("Input any key to exit program.\n")
        clear()

main()
