# Building a number guessing game in Python

import random

def main():
    number_to_guess = random.randint(1, 1000)
    number_of_attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")

    while guess != number_to_guess:
        # Get input ONCE and validate it
        user_input = input("Enter your guess: ")
        
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(user_input)
        number_of_attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")


# Standard Python idiom to run the code directly

if __name__ == "__main__":
    main()