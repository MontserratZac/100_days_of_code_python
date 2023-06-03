from art import logo 
import random
import os

print(logo)

#Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  """Function to set difficulty."""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    global turns
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  
def game():   
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)

  # print(f"I'm thinking in answer {answer}")
  
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
  
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
  
left_game = False
while not left_game:
  game()
  play_again = input("Play again? Type 'y' for play again or 'n' for left the game ")
  if play_again == 'n':
    left_game = True
  else:
    os.system ("cls")
