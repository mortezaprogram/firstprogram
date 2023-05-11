import random
my_list=["rock", "paper", "scissors"]
user_choice=int(input("Please inter 0=rock, 1=paper, 2=scissors\n"))
computer_choice=random.randint(0,2)
print(f"Your choice is {my_list[user_choice]}")
print(f"Computer choice is {my_list[computer_choice]}\n")
# print(f"Computer choice is {computer_choice}")
if user_choice == 0 and computer_choice == 1:
  print("You Lose")
elif user_choice == 0 and computer_choice == 2:
  print("You Win")
elif user_choice == 1 and computer_choice == 0:
  print("You win")
elif user_choice== 1 and computer_choice== 2:
  print("You lose")
elif user_choice== 2 and computer_choice== 0:
  print("You lose")
elif user_choice== 2 and computer_choice== 1:
  print("You Win")
elif (user_choice == 0 and computer_choice == 0)or (user_choice == 1 and computer_choice == 1)or(user_choice == 2 and computer_choice == 2):
    print("Please try again")


