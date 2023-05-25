import random
from turtle import Screen,Turtle


screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Please inter the color: \n green yellow,gold,teal,pink,blue,green")
colors=["green yellow","gold","teal","pink","blue","green"]
y_position=[-70,-40,-10,20,50,80]
all_turtle=[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You win. The {winning_color} turtle is the winner ")
            else:
                print(f"You Lose. The {winning_color} turtle is the winner ")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)









screen.exitonclick()