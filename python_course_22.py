import random
from turtle import Turtle,Screen,colormode
import colorgram

tim=Turtle()
tim.ht()
tim.penup()
tim.shape("turtle")
tim.color("blue")
num_sides=5
colormode(255)
size=[3,6,7,8,3,10,11,13,20]
# colours=["green yellow","gold","teal","pink","blue"]
rgb_colour=[]
extract_color=colorgram.extract("test.jpg",30)
for color in extract_color:
    #or rgb_colour.append(color.rgb)
     r = color.rgb.r
     g = color.rgb.g
     b = color.rgb.b
     color_rgb = (r, g, b)
     rgb_colour.append(color_rgb)


def random_colour():

    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour=(r,g,b)
    return colour


direction=[0,90,180,270]
tim.speed("fastest")
# tim.pensize(15)

'''
for _ in range(100):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(direction))
'''
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random.choice(rgb_colour))
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=100
for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(rgb_colour))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




'''
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle=360/num_sides
        tim.forward(100)
        tim.right(angle)

for _ in range(2,7):
    tim.color(random.choice(colours))
    draw_shape(_)
'''





screen=Screen()
screen.exitonclick()