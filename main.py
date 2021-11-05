import random
computer_choices = ["Snake","Water","Gun"]
print("Welcome to the Snake, Water & Gun Game.")
user_choice = input("What do you want to select? (Snake, Water or Gun)\n").title()
computer = random.randint(0,2)
if computer == 0:
  computer_choice = computer_choices[0]
elif computer == 1:
  computer_choice = computer_choices[1]
else:
  computer_choice = computer_choices[2]

if computer_choice == computer_choices[0] and user_choice == computer_choices[0]:
  print(f"Computer Chose: {computer_choice}")
  print("Its a Draw")
elif computer_choice == computer_choices[0] and user_choice == computer_choices[1]:
  print(f"Computer Chose: {computer_choice}")
  print("Snake dips in Water")
  print("Hurray! You Win")
elif computer_choice == computer_choices[0] and user_choice == computer_choices[2]:
  print(f"Computer Chose: {computer_choice}")
  print("Snake is shooted by Gun")
  print("Hurray! You Win")
elif computer_choice == computer_choices[1] and user_choice == computer_choices[0]:
  print(f"Computer Chose: {computer_choice}")
  print("Snake dips in Water")
  print("Sorry! You Lose")
elif computer_choice == computer_choices[1] and user_choice == computer_choices[1]:
  print(f"Computer Chose: {computer_choice}")
  print("Its a Draw")
elif computer_choice == computer_choices[1] and user_choice == computer_choices[2]:
  print(f"Computer Chose: {computer_choice}")
  print("Gun dips in Water")
  print("Sorry! You Lose")
elif computer_choice == computer_choices[2] and user_choice == computer_choices[0]:
  print(f"Computer Chose: {computer_choice}")
  print("Snake is shooted by Gun")
  print("Sorry! You Lose")
elif computer_choice == computer_choices[2] and user_choice == computer_choices[1]:
  print(f"Computer Chose: {computer_choice}")
  print("Gun dips in Water")
  print("Hurray! You Win")
elif computer_choice == computer_choices[2]and user_choice == computer_choices[2]:
  print(f"Computer Chose: {computer_choice}")
  print("Its a Draw")
  print(f"Computer chose : {computer_choice}")
else:
  print("You have typed an invalid character. Please Restart the Game.")

