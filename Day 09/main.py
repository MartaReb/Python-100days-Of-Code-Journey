import os
from art import logo

print(logo)
print("Welcome to the Blind Auction" )

def find_highest_bidder(users_bidding):
    highest_bid = 0
    winner = ""
    for user in users_bidding:
        if highest_bid < users_bidding[user]:
            highest_bid = users_bidding[user]
            winner = user

    print(f" The winner is {winner} with a bid of ${highest_bid}$")
    print("Thank you for your participation.")

users_dict = {}
while True:
    name = input("What is your name? ")
    price = int(input ("What is your bid? $"))
    users_dict[name] = price
    new_bid = input("Are there any other bidders?y/n ").lower()
    os.system('cls')
    if new_bid == "n":
        find_highest_bidder(users_dict)
        break