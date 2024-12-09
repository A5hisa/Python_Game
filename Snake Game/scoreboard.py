from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.write(f"Score : {self.score}", False, align=ALIGN, font=FONT)

    def score_plus(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)