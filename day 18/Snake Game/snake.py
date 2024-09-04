from turtle import Turtle

# Constants for the snake's starting positions and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves with each step
UP = 90  # Angle to move up
DOWN = 270  # Angle to move down
RIGHT = 0  # Angle to move right
LEFT = 180  # Angle to move left

class Snake:
    def __init__(self):
        self.segments = []  # List to hold the snake's segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Set the head of the snake to the first segment

    def create_snake(self):
        """Create the initial snake with segments at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each segment to the snake

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")  # Create a new turtle segment
        new_segment.color("white")  # Set the segment color to white
        new_segment.penup()  # Lift the pen so it doesn't draw lines
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the list

    def extend(self):
        """Add a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())  # Add a new segment at the position of the last segment

    def move(self):
        """Move the snake forward by updating the position of each segment."""
        # Move each segment to the position of the previous segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward

    def up(self):
        """Change the direction of the snake to up."""
        if self.head.heading() != DOWN:  # Prevent the snake from reversing direction
            self.head.setheading(UP)  # Set the heading to up

    def down(self):
        """Change the direction of the snake to down."""
        if self.head.heading() != UP:  # Prevent the snake from reversing direction
            self.head.setheading(DOWN)  # Set the heading to down

    def right(self):
        """Change the direction of the snake to right."""
        if self.head.heading() != LEFT:  # Prevent the snake from reversing direction
            self.head.setheading(RIGHT)  # Set the heading to right

    def left(self):
        """Change the direction of the snake to left."""
        if self.head.heading() != RIGHT:  # Prevent the snake from reversing direction
            self.head.setheading(LEFT)  # Set the heading to left
