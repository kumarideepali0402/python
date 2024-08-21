from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize the scoreboard
        self.score = 0  # Set the initial score to 0
        self.color("white")  # Set the color of the text to white
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen so no lines are drawn
        self.goto(0, 280)  # Position the scoreboard at the top of the screen
        self.update_score()  # Display the initial score

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1  # Increment the score
        self.clear()  # Clear the previous score display
        self.update_score()  # Update the display with the new score

    def update_score(self):
        """Update the score display with the current score."""
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display a 'Game Over' message on the screen."""
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)


