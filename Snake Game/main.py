from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=620, height=660)  
screen.setworldcoordinates(-295, -300, 305, 340) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_main = Snake() 
food = Food()
scoreboard = Scoreboard()
border_screen = Border()

screen.listen()
screen.onkey(snake_main.up, "w")
screen.onkey(snake_main.down, "s")
screen.onkey(snake_main.left, "a")
screen.onkey(snake_main.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake_main.move()

    if snake_main.head.distance(food) < 15:
        food.refresh()
        snake_main.extend()
        scoreboard.score_plus()

    if abs(int(snake_main.head.xcor())) > 280 or abs(int(snake_main.head.ycor())) > 280:
        game_is_on = False
        scoreboard.game_over()

    for tail in snake_main.body_snake[1:]:
        if snake_main.head.distance(tail) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()