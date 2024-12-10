from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, pos_x, pos_y):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=pos_x, y=pos_y)

    def up(self):
        if self.ycor() == 260:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() == -240:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
