from turtle import Turtle,Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(height=600, width=600)  # Set the screen size to 600x600 pixels
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the window title
screen.tracer(0)  # Turn off the screen updates for smoother animations

# Create game objects
snake = Snake()  # Initialize the snake
food = Food()  # Initialize the food
scoreboard = Scoreboard()  # Initialize the scoreboard

# Listen for key presses to control the snake
screen.listen()
screen.onkey(snake.up, "Up")  # Move the snake up when the "Up" key is pressed
screen.onkey(snake.down, "Down")  # Move the snake down when the "Down" key is pressed
screen.onkey(snake.left, "Left")  # Move the snake left when the "Left" key is pressed
screen.onkey(snake.right, "Right")  # Move the snake right when the "Right" key is pressed

# Start the game loop
is_game_on = True
while is_game_on:
    screen.update()  # Update the screen to reflect the new state
    time.sleep(0.1)  # Pause for a short time to control the game speed
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:  # Check if the snake is close enough to the food
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Update the score

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        is_game_on = False  # End the game if the snake hits the wall
        scoreboard.game_over()  # Display the "Game Over" message

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Loop through each segment except the head
        if snake.head.distance(segment) < 10:  # Check if the snake collides with its own tail
            is_game_on = False  # End the game if collision occurs
            scoreboard.game_over()  # Display the "Game Over" message

# Close the game window when clicked
screen.exitonclick()
