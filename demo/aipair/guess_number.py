import random

secret_number = random.randint(1, 15)
attempts = 0

print("Guess the number between 1 and 15. You have 3 attempts.")

while attempts < 3:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < 1 or guess > 15:
        print("Your guess must be between 1 and 15.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")
else:
    print(f"Sorry, the number was {secret_number}.")