from math import fabs
from random import randint
first_to_go = ""
cycle = 0

print("\n------------------------------------------------------")
print("Welcome to the game of goose, Please select an option: ")
print("------------------------------------------------------\n")

start = input("Press 'p' to play\nPress 'q' to quit: ").lower()

def who_goes_first():
  global first_to_go
  global second_to_go
  doesUser_enter = input("\nHuman player press Enter: ")
  if doesUser_enter == "":
    user_dice_one = randint(1,6)
    user_dice_two = randint(1,6)
    user_roll = user_dice_one + user_dice_two
    print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")

  doesComputer_enter = input("Computer press Enter: ")
  if doesComputer_enter == "":
    computer_dice_one = randint(1,6)
    computer_dice_two = randint(1,6)
    computer_roll = computer_dice_one + computer_dice_two
    print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")

  if user_roll > computer_roll:
    first_to_go = "Human"
    second_to_go = "Computer"
    print("🏁 Human goes first\n")
    
  elif computer_roll > user_roll:
    first_to_go = "Computer"
    second_to_go = "Human"
    print("🏁 Computer goes first\n")

  else:
    print("🎌 Tied...\nRe-running the rolls...")
    who_goes_first()


def game_start():
  print(f"Its {first_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if first_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")

    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      

  print(f"Its {second_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if second_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
      
    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      

if start == "p":
  who_goes_first()
  print("-------------------")
  print("🎮 Game begins 🎮")
  print("-------------------\n")

  game_start_state = True

  while game_start_state != False:
    game_start()
    
else:
  print("\nGood Game\n")
  
    