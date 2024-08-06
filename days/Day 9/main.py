from art import logo
import os
import platform


def find_highest_bid(bids_list):
    highest_bidder = {
        "bidder": "no one",
        "bid": 0,
    }
    for bid in bids_list:
        if bid["bid"] > highest_bidder["bid"]:
            highest_bidder = bid
            
    print(f"The highest bidder was {highest_bidder['bidder']} with a bid of ${highest_bidder['bid']:.2f}.")


bids: list[dict[str, str | float]] = []
add_another_bidder = True
while add_another_bidder:
    print(logo)
    print("Welcome to the silent auction!")
    new_bid: dict[str, str | float] = {}
    new_bid["bidder"] = input("Please enter your name: ")
    new_bid["bid"] = float(input("Please enter your bid: "))
    bids.append(new_bid)
    more_bidders = input("Are there anymore bidders? (Yes or No): ").lower()
    
    if more_bidders == "no":
        add_another_bidder = False
        
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

print(logo)
find_highest_bid(bids)
