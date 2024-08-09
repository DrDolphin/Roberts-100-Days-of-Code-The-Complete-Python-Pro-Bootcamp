import random
from art import logo

RANDOM_MIN = 1
RANDOM_MAX = 100

EASY_MODE_GUESSES = 10
HARD_MODE_GUESSES = 5


def display_start() -> None:
    """Simply displays the logo and the welcome message"""
    print(logo)
    print("Welcome to the number guessing game!")


def set_difficulty() -> int:
    """Prompts the user for difficulty select and returns the number of guesses for that difficulty"""
    difficulty_choice: str = input(
        "Type 'easy' for 10 guesses and 'hard' for 5 guesses: "
    ).lower()
    guesses_left: int
    if difficulty_choice == "easy":
        guesses_left = EASY_MODE_GUESSES
    else:
        guesses_left = HARD_MODE_GUESSES

    return guesses_left


def guessing_game() -> None:
    display_start()

    random_number: int = random.randint(RANDOM_MIN, RANDOM_MAX)
    print(f"I have chosen a random number between {RANDOM_MIN} and {RANDOM_MAX}!")

    guesses_left: int = set_difficulty()

    guessed_correctly = False
    guess: int
    while not guessed_correctly and guesses_left > 0:
        print(f"You have {guesses_left} guesses left!")
        guess = int(input("What is your guess?: "))

        guesses_left -= 1

        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("You guessed correcty!")
            guessed_correctly = True

        print("-----")

    if guessed_correctly:
        print(
            f"Congratulations! You win! The number was {random_number} and you guessed it with {guesses_left} guesse(s) left!"
        )
    else:
        print(f"You ran out of guesses! The number was {random_number}!")


play_again = True
while play_again:
    guessing_game()
    play_again_choice: str = input("Type 'y' to play again and 'n' to quit: ")
    if not play_again_choice == "y":
        play_again = False
