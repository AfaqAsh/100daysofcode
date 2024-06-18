import random

# *Exercise 1 - Coin Toss
# coin_toss = random.randint(0,1)
# if (coin_toss == 0):
#     print(f'Heads')
# else:
#     print(f'Tails')

# *Exercise 2 - Finance Roulette
# list_of_names = input("Enter the names separated by commas: ").split(',')
# payer = list_of_names[random.randint(0, len(list_of_names)-1)]
# print(f'The one who should pay the bill is {payer}')

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

player_choice = int(input("Select your option. Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
if player_choice >=3 or player_choice <0:
    print("You input an invalid number and lost")
else:
    print(f'Your choice \n {choices[player_choice]}')
    computer_choice = random.randint(0,2)
    print(f'Computer choice \n {choices[computer_choice]}')

    if player_choice == computer_choice:
        print("Draw")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print("You win")
    else:
        print("You lose")


# * Revised the concept of modules. Creating different files containing different codes and using in a single file using import
