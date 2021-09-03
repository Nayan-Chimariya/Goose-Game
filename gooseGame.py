from math import fabs
from random import randint
import time

first_to_go = ""
second_to_go = ""
user_position = 1
computer_position = 1

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
  global user_position 
  global computer_position 
  print(f"Its {first_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if first_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      user_position += user_roll
      print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {user_position} ...")
      time.sleep(1)
      print(f"Human is now in position {user_position}\n")

    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      computer_position += computer_roll
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {computer_position} ...")
      time.sleep(1)
      print(f"Computer is now in position {computer_position}\n")
      

  print(f"Its {second_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if second_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      user_position += user_roll
      print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {user_position} ...")
      time.sleep(1)
      print(f"Human is now in position {user_position}\n")
      
    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      computer_position += computer_roll
      print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
      time.sleep(1.5)

      print(f"\nMoving you to position {computer_position} ...")
      time.sleep(1)
      print(f"Computer is now in position {computer_position}\n")
      

if start == "p":
  who_goes_first()
  time.sleep(0.5)
  print("-------------------")
  print("🎮 Game begins 🎮")
  print("-------------------\n")
  time.sleep(1)

  board = "[$%] [2] [3] [4] [5] *[6] +[7] [8] [9] [10] +[11] [12]\n-[13] [14] +[15] [16] [17] [18] [19] -[20] [21] [22] ![23] <24>\n"

  print("----------")
  print("Game Rules")
  print("----------\n")
  time.sleep(0.5)
  print("$ = Human's Position\n"
        "% = computer's position\n"
        "+ = goose: move your piece again by the same distance\n"
        "* = bridge: double the value\n"
        "- = maze: go back to your previous space\n"
        "! = skull: return to the beginning\n"
  )
  time.sleep(5)

  print(".....Game board......\n")
  print (board)
  time.sleep(5)
  
  game_start_state = True

  while game_start_state != False:
    game_start()
    time.sleep(1.5)
    
else:
  print("\nGood Game\n")
  
    