import random
from game_data import data
from replit import clear
def format_data(account):
    """Format data in printable format"""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name},a {account_descr},from {account_country}"


def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

score=0
account_b=random.choice(data)
game_should_continue=True
while game_should_continue:
    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)

    print(f"Account A: {format_data(account_a)}\n")
    print("                    **VS**\n")
    print(f"Account B: {format_data(account_b)}")

    guess=input("who are more folowers, A or B: ").lower()
    a_followers_count=account_a["follower_count"]
    b_followers_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_followers_count,b_followers_count)
    clear()
    if is_correct:
        score+=1
        print(f"You are right,Your Current score is :{score}")
    else:
        game_should_continue=False
        print(f"Sorry,that's wrong,Your Final score is :{score}")