from turtle import Screen, Turtle
from snake import Snake  # Custom class for snake functionalities
import time
from food import Food    # Custom class to manage food for the snake
from scoreboard import ScoreBoard  # Custom class for managing the scoreboard
from lives import Lifeline  # Custom class for managing the lifelines

# Setting up the screen
screen = Screen()
screen.setup(width=810, height=500)  # Set screen dimensions
screen.bgcolor("#001F3F")  # Set background color
screen.title("My Snake Game")  # Set window title

# Dummy snake for the start screen
dummy = Snake()

# Display start screen text
start = Turtle()
start.hideturtle()
start.penup()
start.goto(-180, -20)
start.color("white")
start.write("Press S ", align='left', font=('Arial', 28, 'normal'))  # Display 'Press S'
start.goto(10, -20)
start.write(" Start Game", align='left', font=('Arial', 28, 'normal'))  # Display 'Start Game'

game_is_on = False  # Flag to check if the game is running

# Initialize game objects
snake = Snake()  # Main snake object
food = Food()    # Food object
sb = ScoreBoard()  # Scoreboard object
life = Lifeline()  # Lifeline object

# Screen listens to keyboard events
screen.listen()
screen.onkey(snake.up, "Up")      # Move snake up
screen.onkey(snake.down, "Down")  # Move snake down
screen.onkey(snake.right, "Right")  # Move snake right
screen.onkey(snake.left, "Left")  # Move snake left

# Function to reset the game state
def reset_game():
    snake.reset_position()  # Reset snake position and segments
    food.refresh()          # Refresh the food position

# Function to start the game
def turnOnGame():
    dummy.disAppear()  # Hide the dummy snake from the start screen
    start.clear()      # Clear the start screen text
    game_is_on = True  # Set the game state to running
    
    # Main game loop
    while game_is_on:
        time.sleep(0.1)  # Control the speed of the game
        snake.move()     # Move the snake forward
       
        # Check for collision with food
        if snake.head.distance(food) < 15:
            sb.updateScore()  # Update the score
            food.refresh()    # Refresh food position
            screen.tracer(0)  # Turn off screen updates
            snake.extend()    # Extend the snake
            screen.tracer(1)  # Turn on screen updates
            
        # Check for collision with the wall
        if snake.head.xcor() > 390 or snake.head.xcor() < -400 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
            if life.reduceLife():  # Check if lifeline is available
                reset_game()       # Reset the game state
            else:
                game_is_on = False # End game if no lifeline left
                sb.game_over()     # Display game over

        # Check for collision with itself
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                if life.reduceLife():  # Check if lifeline is available
                    reset_game()       # Reset the game state
                else:
                    game_is_on = False # End game if no lifeline left
                    sb.game_over()     # Display game over
                    screen.update()    # Update screen to reflect game over
                break  # Exit the loop on collision
    
screen.onkey(turnOnGame, "S")  # Bind 'S' key to start the game

screen.exitonclick()  # Keep the window open until clicked
