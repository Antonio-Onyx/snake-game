from turtle import Screen
from keys import Keys

screen = Screen()
tecla = Keys()

screen.listen()
screen.onkey(key="Up", fun=tecla.up)
screen.onkey(key="Right", fun=tecla.right)
screen.onkey(key="Left", fun=tecla.left)
screen.onkey(key="Down", fun=tecla.down)
screen.exitonclick()
