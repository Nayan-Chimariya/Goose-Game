from random import randint
import time

first_to_go = ""
second_to_go = ""
user_position = 1
computer_position = 1
user_index = [1]
computer_index = [1]


# game conditions:
goose = [7,11,15]
bridge = [6]
maze = [13,20]
skull = [23]

# game board list:
# goose = 7, 11, 15
# bridge = 6
# maze = 13, 20

def map():
  for i in range(1, 25):
    if i == user_index[0] == computer_index[0]: 
      print(f"[$%]", end=" ")
    elif i == 12 and computer_index[0] == 12:
      print(f"[%]\n")
    elif i == 12 and user_index[0] == 12:
      print(f"[$]\n")
    elif i == computer_index[0]:
      print(f"[%]", end=" ")
    elif i == user_index[0]: 
      print(f"[$]", end=" ")
    elif i in goose:
      print(f"+[{i}]", end=" ")
    elif i in maze:
      print(f"-[{i}]", end=" ")
    elif i in bridge:
      print(f"*[{i}]", end=" ")
    elif i == 23:
      print(f"![{i}]", end=" ")
    elif i == 24:
      print(f"<{i}>")
    elif i == 12:
      print(f"[{i}]\n")
    else:
      print(f"[{i}]", end=" ")

print("\n------------------------------------------------------")
print("Welcome to the game of goose, Please select an option: ")
print("------------------------------------------------------\n")

start = input("Press 'p' to play\nPress 'q' to quit: ").lower()

def who_goes_first():
  global first_to_go
  global second_to_go

  doesUser_enter = input("\n👨 Human player press Enter: ")
  if doesUser_enter == "":
    user_dice_one = randint(1,6)
    user_dice_two = randint(1,6)
    user_roll = user_dice_one + user_dice_two
    print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")

  doesComputer_enter = input("🤖 Computer press Enter: ")
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

  print(f"🟢 Its {first_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if first_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      user_position += user_roll

      if user_position > 24:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(0.5)
        print("🚫 Exceeded board limit... you did not move")
        user_position -= user_roll
        time.sleep(0.5)
        print(f"Your current position is {user_position}\n")
        user_index[0]
        
      elif user_position == 24:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(1.5)
        print(f"\nMoving you to position {user_position} ...")
        time.sleep(1)
        print(f"Human is now in position {user_position}\n")
        user_index.append(user_position)
        user_index.pop(0)

        print("🏆 Congrats human you have won")
        print("I guess there is hope for humatiy after all\n")
        exit(0)
      
      else:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(1.5)

        print(f"\nMoving you to position {user_position} ...")
        time.sleep(1)
        print(f"Human is now in position {user_position}\n")
        user_index.append(user_position)
        user_index.pop(0)

        if user_position in bridge:
          print("🌫️ You have crossed a bridge")
          print("Your position has been doubled")
          user_position *= 2
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
          
        elif user_position in goose:
          if user_position > 24:
            print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
            time.sleep(0.5)
            print("🚫 Exceeded board limit... you did not move")
            user_position -= user_roll
            time.sleep(0.5)
            print(f"Your current position is {user_position}\n")
            user_index[0]
          else:
            print("🌫️ You have crossed a bridge")
            print("Your position has been doubled")
            user_position *= 2
            print(f"\nMoving you to position {user_position} ...")
            time.sleep(1)
            print(f"Human is now in position {user_position}\n")
            user_index.append(user_position)
            user_index.pop(0)

        elif user_position in maze:
          print("🌫️ You entered a maze, You got lost")
          print("mooving you back to previous position....")
          user_position -= user_roll
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
        
        elif user_position in skull:
          print("🌫️ You placed your foot on a skull")
          print("you died...restarting from origin...")
          user_position = 1
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
      map()
      time.sleep(1)
      print("\n")

    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      computer_position += computer_roll
      if computer_position > 24:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(0.5)
        print("🚫 Exceeded board limit... you did not move")
        computer_position -= computer_roll
        time.sleep(0.5)
        print(f"Your current position is {computer_position}\n")
        computer_index[0]

      elif computer_position == 24:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(1.5)
        print(f"\nMoving you to position {computer_position} ...")
        time.sleep(1)
        print(f"Computer is now in position {computer_position}\n")
        computer_index.append(computer_position)
        computer_index.pop(0)

        print("🏆 Congrats computer you have won")
        print("Now human termination is certain\n")
        exit(0)
        
      else:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(1.5)

        print(f"\nMoving you to position {computer_position} ...")
        time.sleep(1)
        print(f"Computer is now in position {computer_position}\n")
        computer_index.append(computer_position)
        computer_index.pop(0)

        if computer_position in bridge:
          print("🌫️ You have crossed a bridge")
          print("Your position has been doubled")
          computer_position *= 2
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"Computer is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
          
        elif computer_position in goose:
          if computer_position > 24:
            print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
            time.sleep(0.5)
            print("🚫 Exceeded board limit... you did not move")
            computer_position -= computer_roll
            time.sleep(0.5)
            print(f"Your current position is {computer_position}\n")
            computer_index[0]
          else:
            print("🌫️ You have landed on goose")
            print("mooving your piece by the same distance....")
            computer_position += computer_roll
            print(f"\nMoving you to position {computer_position} ...")
            time.sleep(1)
            print(f"Computer is now in position {computer_position}\n")
            computer_index.append(computer_position)
            computer_index.pop(0)

        elif computer_position in maze:
          print("🌫️ You entered a maze, You got lost")
          print("mooving you back to previous position....")
          computer_position -= computer_roll
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"Computer is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
        
        elif computer_position in skull:
          print("🌫️ You placed your foot on a skull")
          print("you died...restarting from origin...")
          computer_position = 1
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"Human is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
      map()
      print("\n")
  
  print(f"🟢 Its {second_to_go}'s turn\n")
  game_start = input("Press Enter: ")
  if game_start == "":
    if second_to_go == "Human":
      user_dice_one = randint(1,6)
      user_dice_two = randint(1,6)
      user_roll = user_dice_one + user_dice_two
      user_position += user_roll
      if user_position > 24:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(0.5)
        print("🚫 Exceeded board limit... you did not move")
        user_position -=  user_roll
        time.sleep(0.5)
        print(f"Your current position is {user_position}\n")
        user_index[0]

      elif user_position == 24:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(1.5)
        print(f"\nMoving you to position {user_position} ...")
        time.sleep(1)
        print(f"Human is now in position {user_position}\n")
        user_index.append(user_position)
        user_index.pop(0)

        print("🏆 Congrats human you have won")
        print("I guess there is hope for humatiy after all\n")
        exit(0)

      else:
        print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
        time.sleep(1.5)

        print(f"\nMoving you to position {user_position} ...")
        time.sleep(1)
        print(f"Human is now in position {user_position}\n")
        user_index.append(user_position)
        user_index.pop(0)

        if user_position in bridge:
          print("🌫️ You have crossed a bridge")
          print("Your position has been doubled")
          user_position *= 2
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
          
        elif user_position in goose:
          if user_position > 24:
            print(f"\n🎲 🎲 You have rolled {user_dice_one} and {user_dice_two} making it {user_roll}\n")
            time.sleep(0.5)
            print("🚫 Exceeded board limit... you did not move")
            user_position -=  user_roll
            time.sleep(0.5)
            print(f"Your current position is {user_position}\n")
            user_index[0]
          else:
            print("🌫️ You have landed on goose")
            print("mooving your piece by the same distance....")
            user_position += user_roll
            print(f"\nMoving you to position {user_position} ...")
            time.sleep(1)
            print(f"Human is now in position {user_position}\n")
            user_index.append(user_position)
            user_index.pop(0)

        elif user_position in maze:
          print("🌫️ You entered a maze, You got lost")
          print("mooving you back to previous position....")
          user_position -= user_roll
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
        
        elif user_position in skull:
          print("🌫️ You placed your foot on a skull")
          print("you died...restarting from origin...")
          user_position = 1
          print(f"\nMoving you to position {user_position} ...")
          time.sleep(1)
          print(f"Human is now in position {user_position}\n")
          user_index.append(user_position)
          user_index.pop(0)
      map() 
      time.sleep(1)
      print("\n")
      
    else:
      computer_dice_one = randint(1,6)
      computer_dice_two = randint(1,6)
      computer_roll = computer_dice_one + computer_dice_two
      computer_position += computer_roll
      if computer_position > 24:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(0.5)
        print("🚫 Exceeded board limit... you did not move")
        computer_position -= computer_roll
        time.sleep(0.5)
        print(f"Your current position is {computer_position}\n")
        user_index[0]
      
      elif computer_position == 24:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(1.5)
        print(f"\nMoving you to position {computer_position} ...")
        time.sleep(1)
        print(f"Computer is now in position {computer_position}\n")
        computer_index.append(computer_position)
        computer_index.pop(0)

        print("🏆 Congrats computer you have won")
        print("Now human termination is certain\n")
        exit(0)

      else:
        print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
        time.sleep(1.5)

        print(f"\nMoving you to position {computer_position} ...")
        time.sleep(1)
        print(f"Computer is now in position {computer_position}\n")
        computer_index.append(computer_position)
        computer_index.pop(0)

        if computer_position in bridge:
          print("🌫️ You have crossed a bridge")
          print("Your position has been doubled")
          computer_position *= 2
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"computer is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
          
        elif computer_position in goose:
          if computer_position > 24:
            print(f"\n🎲 🎲 You have rolled {computer_dice_one} and {computer_dice_two} making it {computer_roll}\n")
            time.sleep(0.5)
            print("🚫 Exceeded board limit... you did not move")
            computer_position -= computer_roll
            time.sleep(0.5)
            print(f"Your current position is {computer_position}\n")
            user_index[0]
          else:
            print("🌫️ You have landed on goose")
            print("mooving your piece by the same distance....")
            computer_position += computer_roll
            print(f"\nMoving you to position {computer_position} ...")
            time.sleep(1)
            print(f"Computer is now in position {computer_position}\n")
            computer_index.append(computer_position)
            computer_index.pop(0)

        elif computer_position in maze:
          print("🌫️ You entered a maze, You got lost")
          print("mooving you back to previous position....")
          computer_position -= computer_roll
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"Computer is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
        
        elif computer_position in skull:
          print("🌫️ You placed your foot on a skull")
          print("you died...restarting from origin...")
          computer_position = 1
          print(f"\nMoving you to position {computer_position} ...")
          time.sleep(1)
          print(f"Computer is now in position {computer_position}\n")
          computer_index.append(computer_position)
          computer_index.pop(0)
      map()
      time.sleep(1)
      print("\n")
  
  if user_index == computer_index and user_index != 0:
    print("💀 Computer was overlapped by Human\n")
    print("Computer is now at the start point")
    computer_index.append(1)
    computer_index.pop(0)
    map()
    time.sleep(1)
    print("\n")
  elif computer_index == user_index and computer_index != 0:
    print("💀 Human was overlapped by Computer\n")
    print("Human is now at the start point")
    user_index.append(1)
    user_index.pop(0)
    map()
    time.sleep(1)
    print("\n")

      
if start == "p":
  who_goes_first()
  time.sleep(0.5)
  print("-------------------")
  print("🎮 Game begins 🎮")
  print("-------------------\n")
  time.sleep(1)

  print("-------------------------")
  print("📃 Game Info / Conditions")
  print("-------------------------\n")
  time.sleep(0.5)
  print("$ = Human's Position\n"
        "% = computer's position\n"
        "+ = goose: move your piece again by the same distance\n"
        "* = bridge: double the value\n"
        "- = maze: go back to your previous space\n"
        "! = skull: return to the beginning\n"
  )
  time.sleep(5)

  print("----------")
  print("Game board")
  print("----------\n")
  map()
  print("\n")
  time.sleep(5)
  
  while True:
    game_start()
    time.sleep(1.5)
    
else:
  print("\nGood Game\n")
     