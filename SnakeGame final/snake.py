from turtle import Turtle

# Constants for the initial setup and movement of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance each segment moves per step
UP = 90    # Heading angle for moving up
DOWN = 270 # Heading angle for moving down
LEFT = 180 # Heading angle for moving left
RIGHT = 0  # Heading angle for moving right

class Snake:
    def __init__(self):
        self.segments = []  # List to hold the snake segments
        self.create_snake() # Initialize the snake with default segments
        self.head = self.segments[0]  # Head of the snake is the first segment
        self.head.color("#FFFFFF")    # Set the head color

    def create_snake(self):
        """Create the initial snake with predefined starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add segments at the specified positions
            
    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle(shape="square")
        new_segment.color("#32CD32")  # Set segment color
        new_segment.penup()           # Disable drawing line when the segment moves
        new_segment.goto(position)    # Move the segment to the starting position
        self.segments.append(new_segment)  # Append the new segment to the list

    def extend(self):
        """Add a new segment to the snake at the last segment's position."""
        self.add_segment(self.segments[-1].position())  # Add segment at the tail's position
        
    def move(self):
        """Move the snake forward by updating the position of each segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Update the position of each segment to follow the one in front of it
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def reset_position(self):
        """Reset the snake's position to the center and spread out horizontally."""
        for segment in self.segments:
            segment.goto(0, 0)  # Move all segments to the center (temporary overlap)
        for i, segment in enumerate(self.segments):
            segment.setx(-i * 20)  # Reposition segments horizontally at 20 units apart
        self.head.setheading(RIGHT)  # Reset the snake's direction to right
    
    def right(self):
        """Turn the snake right if it's not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def up(self):
        """Turn the snake up if it's not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        """Turn the snake left if it's not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):
        """Turn the snake down if it's not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def disAppear(self):
        """Hide all segments of the snake (used for clearing the start screen)."""
        for segment in self.segments:
            segment.hideturtle()

            