
import random

number = random.randint(1, 10)

print("----- NUMBER GUESSING GAME -----")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed correctly!")

elif guess > number:
    print("Too high! The correct number was", number)

else:
    print("Too low! The correct number was", number)
