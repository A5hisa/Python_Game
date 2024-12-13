from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_backward(self):
        if self.ycor() <= -280:
            pass
        else:
            self.backward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() == FINISH_LINE_Y :
            self.setpos(STARTING_POSITION)
            return True