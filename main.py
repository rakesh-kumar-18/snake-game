from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
speed = 0.1

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
user_level = screen.textinput(title="Select a level", prompt="In which level do you want to play?(Easy,Medium,Hard):")
if user_level.lower() == "easy":
    speed = 0.5
elif user_level.lower() == "medium":
    speed = 0.1
elif user_level.lower() == "hard":
    speed = 0.07


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
