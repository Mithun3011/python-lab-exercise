
# Dice Simulator

import random

while True:
    print("\n--- DICE SIMULATOR ---")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice == "2":
        print("Game closed!")
        break

    else:
        print("Invalid choice!")
