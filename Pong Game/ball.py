from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.07
        
    def moveball(self):
        pos_x = self.xcor() + self.x_move
        pos_y = self.ycor() + self.y_move
        self.goto(pos_x, pos_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.ball_speed = 0.07
