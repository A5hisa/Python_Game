from turtle import Turtle

FONT = ("Arial", 25, "bold")
ALIGN = "center"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_paddle1 = 0
        self.score_paddle2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Player1          Player2", False, align=ALIGN, font=FONT)

    def score_plus_paddle1(self):
        self.score_paddle1 += 1
        self.clear()
        self.write(f"{self.score_paddle1}          {self.score_paddle2}", False, align=ALIGN, font=FONT)

    def score_plus_paddle2(self):
        self.score_paddle2 += 1
        self.clear()
        self.write(f"{self.score_paddle1}          {self.score_paddle2}", False, align=ALIGN, font=FONT)
  
    def winner(self, winner):
        self.clear
        self.goto(0, 0)
        self.write(f"{winner} is winner!!!", False, align=ALIGN, font=FONT)