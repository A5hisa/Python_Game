from turtle import Screen
from player import Player
from car import CarsManage
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Turtle crossing the road Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player1 = Player()
screen.onkey(player1.go_forward, "Up")
screen.onkey(player1.go_backward, "Down")

cars = CarsManage()
score = Scoreboard()

game = True

while game:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    
    for car in cars.cars_list:
        if player1.distance(car) < 15:
            game = False
            score.game_over()

    if player1.finish() == True:
        score.level_up()
        if score.level % 2 == 0:
            cars.more_car_speed()

screen.exitonclick()