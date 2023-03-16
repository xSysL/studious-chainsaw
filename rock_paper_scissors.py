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

import random
user_choice = input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
computer_choice = random.randint(0,2)

choice = [rock, paper, scissors]

if int(user_choice) > 3 or int(user_choice) < 0:
    print("You chose invalid number. You lost.")
elif int(user_choice) == 2 and int(computer_choice) == 0:
    print(f"You chose {choice[int(user_choice)]} \nComputer chose {choice[computer_choice]} \nComputer Wins!")
elif int(user_choice) > int(computer_choice) :
    print(f"You chose {choice[int(user_choice)]} \nComputer chose {choice[computer_choice]} \nYou win!")
elif int(user_choice) == int(computer_choice):
    print(f"You chose {choice[int(user_choice)]} \nComputer chose {choice[computer_choice]} \nIt\'s a Draw!")

else :
    print(f"You chose {choice[int(user_choice)]} \nComputer chose {choice[computer_choice]} \nComputer Wins!")

input("Press \'Enter\' to quit: ")