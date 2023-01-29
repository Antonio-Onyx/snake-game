from turtle import Turtle
MOVES = Turtle(shape="square")


class Keys:

    def __init__(self):
        pass

    def up(self):
        MOVES.penup()
        MOVES.setheading(90)
        MOVES.forward(10)

    def right(self):
        MOVES.penup()
        MOVES.setheading(0)
        MOVES.forward(10)

    def down(self):
        MOVES.penup()
        MOVES.setheading(270)
        MOVES.forward(10)

    def left(self):
        MOVES.penup()
        MOVES.setheading(180)
        MOVES.forward(10)
