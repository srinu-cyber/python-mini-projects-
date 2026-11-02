import random
import string


def cows_bulls(length):
    
    return "".join(random.sample(string.digits, length))


print("Welcome to BULLS and COWS game! Guess the number !!!")
secret = cows_bulls(4)
turns = 0

while True:
    guess = input("\n>>> ")

    if len(guess) != 4 or not guess.isdigit():
        print("Enter a valid 4-digit number.")
        continue

    turns += 1

    cows = 0
    bulls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    print(f"{bulls} bulls, {cows} cows")

    if bulls == 4:
        print(f"Bulls = 4! You won! ")
        print(f"Turns you took to complete the game: {turns}")
        break
