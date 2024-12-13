from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=260)
        self.write(f"level {self.level}", False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"level {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!!", False, align="center", font=FONT)