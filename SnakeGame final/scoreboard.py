from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with initial settings and display the score."""
        super().__init__()         # Initialize the Turtle superclass
        self.hideturtle()          # Hide the turtle cursor
        self.color("white")        # Set the scoreboard color
        self.penup()               # Disable drawing lines when moving
        self.goto(0, 210)          # Position the scoreboard at the top center
        self.score = 0             # Initialize the score to 0
        self.updateScore()         # Display the initial score
        
    def updateScore(self):
        """Update the score display and increment the score."""
        self.clear()  # Clear the previous score display
        self.write(arg=f"Score is {self.score}", align='center', font=('Arial', 20, 'normal'))  # Display the current score
        self.score = self.score + 1  # Increment the score by 1
    
    def game_over(self):
        """Display the game over message at the center of the screen."""
        self.goto(0, 0)  # Position the message at the center
        self.write(arg="Game is over", align='center', font=('Arial', 20, 'normal'))  # Display 'Game over' message
