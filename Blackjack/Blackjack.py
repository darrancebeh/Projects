import random
import os

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
        hitstand = str(input("Do you want to hit or stand?\n")).lower()
        if(hitstand[0] == "h"):
            addPlayerCard(playerCards, cards)
            flag1 = addSum(playerCards)
            flag2 = handCount(playerCards)
            clear()
            print("Dealer's hand: [X,", str(dealerCards[1]) + "]")
            print("Player's hand: " + str(playerCards))

            if(flag1 > 21):
                return True
            elif(flag2 >= 5 and flag1 <= 21):
                fiveHandRule.append("PASS")
                return True
        if(hitstand[0] == "s"):
            return True

def dealerCheck(dealerSum, dealerCards, cards, playerCards):
    if(dealerSum <= 16):
        clear()
        print("Dealer's hand: " + str(dealerCards))
        print("Player's hand: " + str(playerCards) + "\n")
        addDealerCard(dealerCards, cards)
        dealerSum = addSum(dealerCards)
        return dealerSum

def blackjackCard(playerCards, dealerCards):
    clear()
    print("Dealer's hand: " + str(dealerCards))
    print("Player's hand: " + str(playerCards) + "\n")
    print("You Got a Blackjack!")

    if(checkBlackjack(dealerCards)):
        print("The Dealer Also Has a Blackjack!\n")
        return 8
    else:
        print("The Dealer Does Not Have a Blackjack.\n")
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
        print("Congratulations, You Won! Your Cards' Total Sum Is Higher Than The Dealer's.")
    elif(result == 2):
        print("You Lost! The Dealer's Cards' Total Sum Is Higher Than Your's.")
    elif(result == 3):
        print("Congratulations, You Won! You Have a 5 Card Hand Without Busting, Winning by 5-Card Charlie.")
    elif(result == 4):
        print("It's a Push! Your Cards' Total Sum Is The Same As The Dealer's!")
    elif(result == 5):
        print("You Lost! You Busted but The Dealer Did Not. The Total Sum of Your Cards Exceeded 21.")
    elif(result == 6):
        print("Congratulations, You Won! The Dealer Busted but You Did Not. The Total Sum of The Dealer's Cards Exceeded 21.")
    elif(result == 7):
        print("It's a Push! Both Parties Busted. Both Parties' Total Sum of Their Respective Cards Exceeded 21.")
    elif(result == 8):
        print("It's a Push! Both Parties Have a Blackjack!")
    elif(result == 9):
        print("Congratulations, You Won! You Have a Blackjack but The Dealer Does Not!")
    
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
        blackjackCard(playerCards, dealerCards)

    fiveHandRule = []
    if(blackjack == False):
        while(hitOrStand(playerCards, dealerCards, cards, fiveHandRule) != True):
            hitOrStand(playerCards, dealerCards, cards, fiveHandRule)

        if(len(fiveHandRule) <= 0):
            clear()
            dSum = addSum(dealerCards)
            if(dSum <= 16):
                while(dSum <= 16):
                    dealerCheck(dSum, dealerCards, cards, playerCards)
                    dSum = addSum(dealerCards)
            
            if(dSum > 16):
                print("Dealer's hand: " + str(dealerCards))
                print("Player's hand: " + str(playerCards))

            pSum = addSum(playerCards)
            dSum = addSum(dealerCards)
            pHandCount = handCount(playerCards)

            winLose(pSum, dSum, pHandCount)

            result = winLose(pSum, dSum, pHandCount)

            gameEnd(result)
        else:
            result = 3
            gameEnd(result)
    else:
        result = blackjackCard(playerCards, dealerCards)
        gameEnd(result)
    print("\nThank you for playing!")
    input("Input any key to exit the program.\n")

Blackjack()
