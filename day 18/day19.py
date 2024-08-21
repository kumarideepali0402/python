# from turtle import Turtle,Screen
# screen=Screen()


# tim=Turtle()
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def turn_right():
#     newheading=tim.heading()-10
#     tim.setheading(newheading)
# def turn_left():
#     new_heading=tim.heading()+10
#     tim.setheading(new_heading)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(key="W",fun=move_forwards)
# screen.onkey(key="S" , fun=move_backwards)
# screen.onkey(key="A" , fun=turn_left)
# screen.onkey(key="D" , fun=turn_right)
# screen.onkey(key="C" , fun=clear_screen)
# screen.exitonclick()

from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=450,height=300)
user_bet=screen.textinput(title="Play",prompt="guess the winner. Enter the color:")
all_turtles=[]
is_race_on=False
colors=["purple","blue","green","yellow","orange"]
for i in range(5):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-200,y=-100+i*50)
    all_turtles.append(tim)

if user_bet:
    is_race_on=True
while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor()>210:
            is_race_on=False
            winning_color=turtle.pencolor()
            if(winning_color==user_bet):
                print(f"you've won the game,{winning_color} won")
            else:
               print(f"you've lost the game,{winning_color} won")
        turtle.forward(random.randint(1,10))




screen.exitonclick()


