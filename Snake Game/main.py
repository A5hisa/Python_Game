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

game_is_on = True

def stop_game():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkey(snake_main.up, "w")
screen.onkey(snake_main.down, "s")
screen.onkey(snake_main.left, "a")
screen.onkey(snake_main.right, "d")
screen.onkey(stop_game, "space")

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake_main.move()

    if snake_main.head.distance(food) < 15:
        food.refresh()
        snake_main.extend()
        scoreboard.score_plus()

    if abs(int(snake_main.head.xcor())) > 280 or abs(int(snake_main.head.ycor())) > 280:
        scoreboard.reset()
        snake_main.reset()

    for tail in snake_main.body_snake[1:]:
        if snake_main.head.distance(tail) < 10:
            scoreboard.reset()
            snake_main.reset()