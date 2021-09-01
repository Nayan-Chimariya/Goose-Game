from random import randint

print("\n------------------------------------------------------")
print("Welcome to the game of goose, Please select an option: ")
print("------------------------------------------------------\n")

start = input("Press 'p' to play\nPress 'q' to quit: ").lower()

if start == "p":
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


