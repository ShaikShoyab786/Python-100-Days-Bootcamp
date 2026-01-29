import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_elements = [rock, paper, scissors]
user_input = int(input("Choose your choice 0 is Rock, 1 is paper, 2 is scissor: ?"))

if user_input >=0 and user_input <=2:
    print(game_elements[user_input])

comp_choice = random.randint(0,2)
print("computer_choice: ")
print(game_elements[comp_choice])
if user_input < 0 or user_input >2:
    print("Please choose a valid value")
elif user_input ==0 and comp_choice ==2:
    print("You win")
elif user_input ==2 and comp_choice ==0:
    print("You loose")
elif comp_choice > user_input:
    print("You lose!")
elif user_input > comp_choice:
    print("You win!")
elif comp_choice == user_input:
    print("It's a draw!")