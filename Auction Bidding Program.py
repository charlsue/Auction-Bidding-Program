bids = {}
introduction = print("Welcome to the Secret Auction Program")
No_more_bidders = False
import os
def clear_screen():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while not No_more_bidders:
    name = input("What is your name?:").capitalize()
    bid = int(input("What's your bid?:"))
    more_bidders = input("Are there any other bidders? Y/N").lower()
    bids[name] = bid
    if more_bidders == "y":
        clear_screen
        continue
    else:
        break

highest_bid = 0
winner = ""

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    
    
print(f"The winner is {winner} with the bid of {highest_bid}")