import turtle
import pandas

image = "blank_states_img.gif"
FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.hideturtle()
text.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
title = "Guess the State"

correct = 0
correct_list = []

while True:
    answer = screen.textinput(title=title, prompt="Guess the state's name?")

    if answer == None:
        break
    if correct == 50:
        break
    if answer.lower() == "exit":
        break

    if answer.lower() not in correct_list:
        for index, state in enumerate(states):
            if answer.lower() == state.lower():
                correct_list.append(answer.lower())
                correct += 1
                title = f"{correct}/50 States Correct"
                text.goto(data.at[index,"x"], data.at[index, "y"])
                text.write(state, font=FONT)