#Turtle graphics documentation https://docs.python.org/3/library/turtle.html
#Color reference documentation https://cs111.wellesley.edu/reference/colors
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("brown", "green")

for i in range(4):
    tim.forward(100)
    tim.right(90)














screen = Screen()
screen.exitonclick()