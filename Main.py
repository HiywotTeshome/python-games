from Hangman import main as hangman_game
from Dice import main as dice_game
from Slot_machine import main as slot_game

print("*************************")
print("Welcome to Python games")
print("*************************")

while True:

    print()
    print("1. Hangman game")
    print("2. Dice game")
    print("3. Slot machine game")
    print("4. exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hangman_game()
    elif choice == 2:
        dice_game()
    elif choice == 3:
        slot_game()
    elif choice == 4:
        print("Thank you for playing!!")
        break
    else:
        print("Invalid choice. Please choose 1-4.")