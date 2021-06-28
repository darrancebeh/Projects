import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lobby():
    clear()
    totalgames = len(history)
    print("YOUR STATISTICS")
    print("_________________________________________________\n")
    print("TOTAL GAMES: " + str(totalgames))
    print("TOTAL ATTEMPTS: " + str(sum(history)))
    average = sum(history)/totalgames
    round(average, 2)
    print("AVERAGE ATTEMPTS PER GAME: " + str(average))
    print("_________________________________________________\n")

def game():
    clear()
    print("Generating random lucky number...")
    time.sleep(1)
    print("Lucky number generated. Good luck!\n")
    key = random.randint(0,100)
    attempts = 1
    print("ATTEMPT #" + str(attempts))
    guess = int(input("Guess the number, (0 - 100)\n"))
    if(guess != key):
        attempts += 1
        while(guess != key):
            if(guess < key):
                clear()
                print("ATTEMPT #" + str(attempts))
                print("\nYour guess is SMALLER than the lucky number.")
                guess = int(input("Guess the number, (0 - 100)\n"))
                attempts += 1
            elif(guess > key):
                clear()
                print("ATTEMPT #" + str(attempts))
                print("\nYour guess is LARGER than the lucky number.")
                guess = int(input("Guess the number, (0 - 100)\n"))
                attempts += 1

    print("Congratulations! The number was " + str(key) + ".")
    print("\nNumber of attempts: " + str(attempts) + ".")
    input("Input any key to return to lobby.\n")
    history.append(attempts)

history = []

def main():
    clear()
    game()
    lobby()

    while(input("Would you like to play again? (Y/N)\n")).lower()[0] == 'y':
        game()
        lobby()
    
    clear()
    print("Thanks for playing darrance's Random Number Guesser game!")
    input("Input any key to exit the program.\n")

main()
