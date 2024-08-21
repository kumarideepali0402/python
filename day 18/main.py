# from turtle import Turtle,Screen
# timmy_the_turtle=Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.forward(200)
# timmy_the_turtle.color("black")
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.color("white")
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.color("black")
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.color("white")
# timmy_the_turtle.right(90)


# screen=Screen()
# screen.exitonclick()


# from turtle import Turtle,Screen
# tim=Turtle()
# for i in range(15):
#     tim.forward(10)
    
#     tim.penup()
#     tim.forward(10)
 
#     tim.pendown()

# screen=Screen()
# screen.exitonclick()


# from turtle import Turtle,Screen
# import random
# tim=Turtle()
# colors=["olive","red","orange","blue","green","black","pink"]
# def drawShape(side):
#     for i in range(side):
#         tim.forward(100)
#         tim.right(360/side)

# for i in range(3,11):
#     tim.color(random.choice(colors))
#     drawShape(i)
# screen=Screen()
# screen.exitonclick()



# import turtle as t
# import random

# tim=t.Turtle()
# colors=["red","green","black","yellow","pink","orange"]
# angles=[0,90,180,-90]
# tim.pensize(15)
# tim.speed("fastest")

# for i in range(200):
#     tim.forward(30)
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(angles))

# screen=Screen()
# screen.exitonclick()

# import turtle as t
# import random
# tim=t.Turtle()
# tim.pensize(15)
# tim.speed("fastest")
# angle=[0,180,90,-90]
# t.colormode(255)

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=(r,g,b)
#     return random_color



# for i in range(200):
#     tim.forward(30)
#     tim.color(random_color())
#     tim.setheading(random.choice(angle))

# screen=t.Screen()
# screen.exitonclick()

import turtle as t
import random
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return (r,g,b)

tim=t.Turtle()
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()

