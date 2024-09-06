from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Initialize the Food object with specific attributes."""
        super().__init__()                    # Initialize the Turtle superclass
        self.shape("circle")                  # Set the shape of the food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale down the size of the food
        self.penup()                          # Disable drawing lines when moving
        self.fillcolor("#FF1493")           
        self.speed("fastest")                 # Set the movement speed to the fastest
        self.refresh()                        # Position the food randomly on the screen
        
    def refresh(self):
        """Move the food to a new random location within screen bounds."""
        random_x = random.randint(-380, 380)  # Random x-coordinate within screen limits
        random_y = random.randint(-240, 180)  # Random y-coordinate within screen limits
        self.goto(random_x, random_y)         # Move the food to the new random position



