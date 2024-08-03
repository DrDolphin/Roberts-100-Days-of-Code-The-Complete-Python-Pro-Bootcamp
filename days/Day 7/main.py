import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6

display = []
for _ in chosen_word:
    display.append("_")

previous_guesses = []

os.system("cls")
print(logo + "\n")

game_over = False
while not game_over:
    print(stages[lives])
    print(f"{' '.join(display)}\n")
    
    guess = input("Enter a letter to guess: ").lower()
    
    os.system("cls")
    print(logo + "\n")
    
    if guess not in previous_guesses:
        previous_guesses.append(guess)
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
                    
            print(f"You guessed '{guess}' and that is in the word!")
        else:
            lives -= 1
            
            if lives > 0:
                print(f"You guessed '{guess}' but that is not in the word!")
        
        if "_" not in display or lives == 0:
            game_over = True
            print(stages[lives])
            print(f"{' '.join(display)}\n")
            if "_" not in display:
                print(f"You correctly got the word {chosen_word}, you win!")
            else:
                print(f"Oh no! You ran out of lives! The word was {chosen_word}, you lose!")
    else:
        print(f"You've already guessed '{guess}'!")
