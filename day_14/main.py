from game_data import data
from art import logo, vs
import random
import os

def check_answer(account_a, account_b, guess):
  """Take the user guess and follower counts and returns if they got it right."""
  if account_a['follower_count'] > account_b['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'

print(logo)
score = 0
wrong_answer = False
account_b = random.choice(data)

#Make the game repeatable
while not wrong_answer:
  # Generate a random account from the game data.
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  # Formate the account data into a printable format
  print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
  print(vs)
  print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

  # Ask user for a guess
  guess = input("Who has more followers? Type'A' or 'B': ").lower()

  # Check if user is correct
  is_correct = check_answer(account_a, account_b, guess)

  # Clear the screen between rounds
  os.system("cls")
  print(logo)
  
  # Give user feedback on their guess
  if is_correct:
    # Score keeping
    score +=1
    print(f"You're right! Current score: {score}")
    
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

    wrong_answer = True