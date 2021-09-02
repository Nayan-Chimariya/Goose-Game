from math import fabs
from random import randint
import time

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

  time.sleep(0.5)

  if user_roll > computer_roll:
    first_to_go = "Human"
    second_to_go = "Computer"
    print("🏁 Human goes first\n")
    time.sleep(0.5)
    
  elif computer_roll > user_roll:
    first_to_go = "Computer"
    second_to_go = "Human"
    print("🏁 Computer goes first\n")
    time.sleep(0.5)

  else:
    print("🎌 Tied...\nRe-running the rolls...")
    time.sleep(0.5)
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
      time.sleep(1.5)

      print(f"\nMoving you to position {user_roll} ...")
      time.sleep(1)
      print(f"Human is now in position {user_roll}\n")

    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {computer_roll} ...")
      time.sleep(1)
      print(f"Computer is now in position {computer_roll}\n")
      

  print(f"Its {second_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if second_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {user_roll} ...")
      time.sleep(1)
      print(f"Human is now in position {user_roll}\n")
      
    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {computer_roll} ...")
      time.sleep(1)
      print(f"Computer is now in position {computer_roll}\n")
      

if start == "p":
  who_goes_first()
  time.sleep(0.5)
  print("-------------------")
  print("🎮 Game begins 🎮")
  print("-------------------\n")
  time.sleep(1)


  game_start_state = True

  while game_start_state != False:
    game_start()
    time.sleep(1.5)
    
else:
  print("\nGood Game\n")
  
    