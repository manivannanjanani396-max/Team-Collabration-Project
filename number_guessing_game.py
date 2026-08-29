"""
Beginner Python Practice: Number Guessing Game
Concepts covered:
- Variables
- Functions
- if / elif / else
- while loop
- Basic input/output
- try/except for handling bad input
- Random number generation
"""
import random

def get_guess():
    guess = input("Enter your guess: ")
    return guess

def check_guess(guess, target):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def main():
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'quit' to give up.\n")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        raw_guess = get_guess()

        if raw_guess.lower() == "quit":
            print(f"Goodbye! The number was {target}.")
            break

        try:
            guess = int(raw_guess)
        except ValueError:
            print("That's not a valid number. Try again.\n")
            continue

        attempts += 1
        result = check_guess(guess, target)
        print(result)

        if result == "Correct!":
            print(f"You got it in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()
