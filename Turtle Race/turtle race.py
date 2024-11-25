from turtle import Turtle, Screen
import random

race = True
screen = Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_pos = -125

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos)
    all_turtle.append(new_turtle)
    y_pos += 50
    

while race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race = False
            winning = turtle.pencolor()
            if winning == user:
                print(f"You've won! The {winning} turtle is the winner!")
            else:    
                print(f"You've lose! The {winning} turtle is the winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()