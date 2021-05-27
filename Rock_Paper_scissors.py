import random

Computer_choice=random.choice(['scissors', 'rock', 'paper'])
user_choice =  input('Do you want - Rock,paper, or scissors?\n')

if Computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and Computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and Computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and Computer_choice == 'paper':
    print('WIN')
else :
    print("you lose !!! Computer_choice is " + str(Computer_choice))

