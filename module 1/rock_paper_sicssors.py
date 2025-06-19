import random

options = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") :
      print("rock crushes scissors! You win!")
elif (user_choice == "paper" and computer_choice == "rock") :
      print("paper covers rock! You win!")
elif (user_choice == "scissors" and computer_choice == "paper") :
      print("scissors cuts paper! You win!")
else:
    print("You lose! Better luck next time.")