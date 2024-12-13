from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarsManage:

    def __init__(self):
        self.cars_list = []
        self.move = 5
        self.num_cars = 20

    def create_car(self):
        if random.randint(1,6) == 1:
            if (len(self.cars_list)) != self.num_cars:   
                car = Turtle(shape="square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.penup()
                car.setheading(-180)
                car.color(random.choice(COLORS))
                car.setposition(x=300, y=random.randint(-230,230))
                self.cars_list.append(car)
        

    def move_car(self):
        for car in self.cars_list:
            car.fd(self.move)
            if car.xcor() <= -320 :
                car.setposition(x=random.randint(320,500), y=random.randint(-230,230))

    def more_car_speed(self):
        self.move += 2
        self.num_cars += 2
