import os
from art import logo
from art import message

print(logo)
print("Welcome to the auction program.")

bids = {}
  
# Functions to compare the bids
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(message)
  print(f"The winner is {winner} with a bid of ${highest_bid}\n\n")
  
continue_bidding = True

while continue_bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  os.system("cls")
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bids)