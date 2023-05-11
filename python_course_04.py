name1=input("Please input first name: ")
name2=input("Please second first name: ")
name=name1+name2

name_lower=name.lower()

t=name_lower.count("t")
r=name_lower.count("r")
u=name_lower.count("u")
e=name_lower.count("e")
l=name_lower.count("l")
o=name_lower.count("o")
v=name_lower.count("v")
e=name_lower.count("e")
true=t+r+u+e
love=l+o+v+e
true_love=str(true)+str(love)
print(true_love)
true_love=int(true_love)

if (true_love>10) or (true_love<90):
    print(f"Your score is {true_love} and you are together")
elif (true_love > 90) :
    print(f"Your score is {true_love} and you are true_love")
elif (true_love >10) :
    print(f"Your score is {true_love} and you are divorced")