from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body_snake = [] 
        self.create_snake() 
        self.head = self.body_snake[0] 
        
    def create_snake(self):
        for position in START_POS:
            self.add_snake(position)

    def add_snake(self, pos):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(pos)
        self.body_snake.append(snake)

    def extend(self):
        self.add_snake(self.body_snake[-1].position())

    def move(self):
        for body in range(len(self.body_snake) - 1, 0, -1):
            x = self.body_snake[body - 1].xcor()
            y = self.body_snake[body - 1].ycor()
            self.body_snake[body].goto(x, y)
        self.head.forward(MOVE_SNAKE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)