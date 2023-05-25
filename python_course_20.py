import random
number_for_guess=random.randint(1,100)
if input(f"Please select your difficulty(easy/hard): ")=="hard":
    number_of_guess=5
else:
    number_of_guess=10

print(f"You have {number_of_guess} attempt to guess the number")
is_game_over=False
while not is_game_over:

    user_guess=int(input("Please inter your guessed number: "))
    if user_guess==number_for_guess:
        print("You guess it and you Win")
        is_game_over = True
    elif user_guess<number_for_guess:
        print(f"Too low\n guess again\n You have {number_of_guess -1} attempt")
        number_of_guess -= 1
    else:
        print("Too high")
        print(f"Too low\n guess again\n You have {number_of_guess - 1} attempt")
        number_of_guess -= 1
    if number_of_guess==0:
        print("Your quessed number finished")
        is_game_over=True

