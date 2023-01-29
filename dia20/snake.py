from turtle import Turtle
TAIL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_tail = []
        self.create_snake()
        self.head = self.snake_tail[0]

    def create_snake(self):
        for position in TAIL_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.snake_tail.append(new_square)

    def extends(self):
        self.add_segments(self.snake_tail[-1].position())

    def move(self):
        for tail in range(len(self.snake_tail)-1, 0, -1):
            new_x = self.snake_tail[tail-1].xcor()
            new_y = self.snake_tail[tail-1].ycor()
            self.snake_tail[tail].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
