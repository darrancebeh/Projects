import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lobby():
    clear()
    totalgames = len(history)
    totalwins = 0
    totallosses = 0
    totalties = 0

    for game in history:
        if(game == 0):
            totalties += 1
        elif(game == 1):
            totalwins += 1
        elif(game == 2):
            totallosses += 1

    winrate = (2 * totalwins + totalties) / (2 * totalgames) * 100
    winrate = round(winrate, 2)

    print("Your Stats")
    print("_________________________________________________\n")
    print("TOTAL GAMES: " + str(totalgames))
    print("WINS: " + str(totalwins))
    print("LOSSES: " + str(totallosses))
    print("TIES: " + str(totalties) + "\n")
    print("YOUR WINRATE: " + str(winrate) + "%")
    print("_________________________________________________\n")

def game():
    clear()
    computer = random.randint(0,2)
    player = input("Rock, Paper or Scissors?\n").lower()

    if(player[0] == 'r'):
         playerInt = 0
    elif(player[0] == 'p'):
        playerInt = 1
    elif(player[0] == 's'):
        playerInt = 2

    intToOption = [
        "Rock",
        "Paper",
        "Scissors"
    ]

    result = (playerInt - computer) % 3
        
    resultMessages = [
        "It's a tie! Both of you chose " + str(intToOption[playerInt] + "."),
        "Player Win! Player chose " + str(intToOption[playerInt] + " while Computer chose " + str(intToOption[computer]) + ". " + intToOption[playerInt] + " beats " + intToOption[computer] + "."),
        "Computer Win! Player chose " + str(intToOption[playerInt] + " while Computer chose " + str(intToOption[computer]) + ". " + intToOption[computer] + " beats " + intToOption[playerInt] + ".")
    ]

    print(resultMessages[result] +"\n")
    input("Input any key to return to lobby.\n")
    history.append(result)
    return result

history = []

def main():
    game()
    lobby()
    while(input("Would you like to play again? (Y/N)\n")).lower()[0] == 'y':
        game()
        lobby()

    clear()
    print("Thanks for playing darrance's Rock Paper Scissors game!")
    input("Input any key to exit the program.\n")

main()
