from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade Game")
screen.tracer(0)

paddle1 = Paddle(pos_x=-350, pos_y=0)
paddle2 = Paddle(pos_x=350, pos_y=0)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

game = True
while game:
    time.sleep(ball.ball_speed) 
    screen.update()
    ball.moveball()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_paddle()
    elif ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.setx(320)
        ball.bounce_paddle()

    if ball.xcor() == -420 or ball.xcor() == 420:
        if ball.xcor() == 420:
            score.score_plus_paddle1()
        elif ball.xcor() == -420:
            score.score_plus_paddle2()
        ball.reset()

    if score.score_paddle1 == 5 or score.score_paddle2 == 5:
        game = False
        if score.score_paddle1 == 5:
            score.winner("Player1")
        elif score.score_paddle2 == 5:
            score.winner("Player2")

screen.exitonclick()