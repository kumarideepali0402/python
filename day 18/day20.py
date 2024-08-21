# import turtle as t
# import time
# screen=t.Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.tracer(0)

# positions=[(0,0),(-20,0),(-40,0)]

# segments=[]
# is_game_on=False
# for position in positions:
#     segment=t.Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(position)
#     segments.append(segment)
# screen.update()
# is_game_on=True
# while (is_game_on):
#     screen.update()
#     time.sleep(0.1)

#     for (seg_num) in range(len(segments)-1,0,-1):
#         new_x=segments[seg_num-1].xcor()
#         new_y=segments[seg_num-1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)



# screen.exitonclick()


from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)