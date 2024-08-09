from art import logo
import random
import os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def display_logo():
    print(logo)


def initialize():
    display_logo()

    starter_hands = {
        "player_hand": [],
        "dealer_hand": [],
    }

    for _ in range(2):
        give_new_card(starter_hands["player_hand"])
        give_new_card(starter_hands["dealer_hand"])

    return starter_hands


def check_for_21(player_hand):
    if sum(player_hand) == 21:
        return True
    return False


def display_outcome(final_hands):
    players_final_score = sum(final_hands["player_hand"])
    dealers_final_score = sum(final_hands["dealer_hand"])

    print(
        f"\tYour final hand: {final_hands['player_hand']}, final score: {players_final_score}"
    )
    print(
        f"\tDealer's final hand: {final_hands['dealer_hand']}, final score: {dealers_final_score}"
    )

    if players_final_score > 21 or (
        dealers_final_score > players_final_score and dealers_final_score <= 21
    ):
        print("You lose! 😤")
    elif players_final_score == dealers_final_score:
        print("It's a tie! 😅")
    else:
        print("You win! 🥳")


def display_current_hands(current_hands):
    print(
        f"\tYour current hand: {current_hands['player_hand']}, current score: {sum(current_hands['player_hand'])}"
    )
    print(f"\tDealer's first card: {current_hands['dealer_hand'][0]}")


def give_new_card(hand):
    new_card = random.choice(deck)
    hand.append(new_card)
    hand_sum = sum(hand)

    if hand_sum > 21:
        if 11 in hand:
            hand[hand.index(11)] = 1


def play_blackjack():
    hands = initialize()

    if check_for_21(hands["player_hand"]):
        display_outcome(hands)
        return

    player_hold = False
    while not player_hold:
        display_current_hands(hands)
        hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if hit_me == "y":
            give_new_card(hands["player_hand"])
            if sum(hands["player_hand"]) > 21:
                display_outcome(hands)
                return
        else:
            player_hold = True

    while sum(hands["dealer_hand"]) < 17:
        give_new_card(hands["dealer_hand"])

    display_outcome(hands)
    return


display_logo()
play_again = True
while play_again:
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == "y":
        os.system("cls")
        play_blackjack()
    else:
        play_again = False
