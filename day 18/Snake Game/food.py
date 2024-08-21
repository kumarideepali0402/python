from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Set up the appearance of the food
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen so no drawing happens when the food moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale down the food size by half
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the movement speed to the fastest to avoid any delay
        self.refresh()  # Place the food at a random location

    def refresh(self):
        """Move the food to a new random location on the screen."""
        rand_x = random.randint(-280, 280)  # Generate a random x-coordinate within screen bounds
        rand_y = random.randint(-280, 280)  # Generate a random y-coordinate within screen bounds
        self.goto(rand_x, rand_y)  # Move the food to the new random location
