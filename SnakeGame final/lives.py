from turtle import Turtle

# Positions where the lifeline indicators will be placed on the screen
POSITIONS = [(370, 230), (340, 230), (310, 230)]

class Lifeline:
    def __init__(self):
        """Initialize the Lifeline with the initial set of lives."""
        self.currLives = []  # List to hold the current life indicators
        self.create_lives()  # Create and display the initial set of lives
        
    def create_lives(self):
        """Create the lifeline indicators at predefined positions."""
        for position in POSITIONS:
            self.add_life(position)  
        
    def add_life(self, position):
        """Add a life indicator (red circle) at the specified position."""
        new_segment = Turtle(shape="circle")  # Create a new turtle shaped as a circle
        new_segment.fillcolor("red")          
        new_segment.penup()                   # Disable drawing lines when moving
        new_segment.goto(position)            # Place the indicator at the given position
        self.currLives.append(new_segment)    # Add the indicator to the current lives list
        
    def reduceLife(self):
        """Remove one life indicator and return whether lives are still remaining."""
        if self.currLives:
            life = self.currLives.pop()  # Remove the last life indicator from the list
            life.hideturtle()            # Hide the life indicator from the screen
        return self.numberOfLives() > 0  # Return True if there are lives remaining, False otherwise
        
    def numberOfLives(self):
        """Return the current number of lives remaining."""
        return len(self.currLives)  # Return the count of remaining life indicators

    
        