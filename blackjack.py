import random 
from blackjack_logo import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []
player_card.append(random.choice(cards))
player_card.append(random.choice(cards))
player_score = sum(player_card)
computer_card = []
computer_card.append(random.choice(cards))
choice_finished = False
more_than_17 = False

def generate(times):
    for i in range(times):
        player_card.append(random.choice(cards))

def generate2(times):
    for i in range(times):
        computer_card.append(random.choice(cards))

print(f"Your cards are {player_card}, Your score is {player_score} \nComputer card is {computer_card}")



while not choice_finished :

    should_continue = input("Do you want to pick more card? Type 'y' or 'n': ")
    if should_continue == "y":
        
        generate(1)
        player_score = sum(player_card)
        if player_score > 21 and 11 in player_card :
            player_card = [1 if item == 11 else item for item in player_card]
            player_score = sum(player_card)
            print(f"your cards are{player_card}, Your score is {player_score}")
        elif player_score > 21:
            #print(f"Your cards are {player_card},Your score is {player_score} You lost.")
            choice_finished = True
        elif player_score <= 21 :
            print(f"your cards are{player_card}, Your score is {player_score}")

    elif should_continue == "n" :
        choice_finished = True
        break   


while not more_than_17 :

    generate2(1)
    computer_score = sum(computer_card)
    
    if computer_score > 21 and 11 in computer_card :
            computer_card = [1 if item == 11 else item for item in computer_card]
            computer_score = sum(computer_card)
            generate2(1)
            #print('test')

    elif computer_score > 21 :

        more_than_17 = True
        #print("test2")
        break

    elif computer_score <21 :

        if computer_score < 17 :
            generate2(1)
            computer_score = sum(computer_card)
            break
        elif computer_score > 17 :
            more_than_17 = True
            #print("test4")
            break

if player_score > 21 :
    print(f"Your cards are {player_card}, your score is {player_score}. You Lost")

if computer_score >21 :
     print(f"Your cards are {player_card}, your score is {player_score}.\nComputer cards are {computer_card}, Computer score is {computer_score}\nYou Win !!!")

elif player_score <= 21 :

    if player_score > computer_score :
         print(f"Your cards are {player_card}, your score is {player_score}.\nComputer cards are {computer_card}, Computer score is {computer_score}\nYou Win !!!")

    elif player_score < computer_score :
        print(f"Your cards are {player_card}, your score is {player_score}.\nComputer cards are {computer_card}, Computer score is {computer_score}\nYou Lost :(")
 
    elif player_score == computer_score :
        print(f"Your cards are {player_card}, your score is {player_score}.\nComputer cards are {computer_card}, Computer score is {computer_score}\nIt's a Draw !")