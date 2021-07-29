import random

computer_score = 0
user_score = 0

options = ["rock", "paper", "scissors"]

print("Welcome to rock, paper, scissors! Winner is the first to 3 points!")
while True :

    user = input("Type rock, paper or scissors: ").lower()
    
    random_number = random.randint (0, 2)

    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + ".")

    if user == "rock" and computer_pick == "scissors":
        print("You win!")
        user_score += 1

    elif user == "paper" and computer_pick == "rock":
        print("You win!")
        user_score += 1

    elif user == "scissors" and computer_pick == "paper":
        print("You win!")
        user_score += 1

    elif user == computer_pick:
        print("Draw!")

    else:
        print("Computer wins!")
        computer_score += 1

    if computer_score >= 3 or user_score >= 3:
        break

print("Game over!")

if computer_score > user_score:
    print("The computer wins the game!")
else:
    print("Congrats you win!")

print("You scored " + str(user_score) + " points and the computer scored " + str(computer_score) + " points!")



 
    
    


