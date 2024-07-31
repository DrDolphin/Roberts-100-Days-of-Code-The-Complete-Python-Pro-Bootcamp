import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

possible_moves = [rock, paper, scissors]

win_message = "You win!"
loss_message = "You lose!"
draw_message = "It's a draw"

rock_outcomes = [draw_message, loss_message, win_message]
paper_outcomes = [win_message, draw_message, loss_message]
scissors_outcomes = [loss_message, win_message, draw_message]

outcomes = [rock_outcomes, paper_outcomes, scissors_outcomes]

input_user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

if input_user > 2 or input_user < 0:
    print("Invalid input!")
else:
    length_of_possible_moves = int(len(possible_moves)) - 1
    computer_move = random.randint(0, length_of_possible_moves)

    print(possible_moves[input_user] + "\n")
    print("Computer chose:\n")
    print(possible_moves[computer_move] + "\n")
    print(outcomes[input_user][computer_move])
