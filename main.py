import random
# How to calculate an angle -> 360° / N° Sides
#Turtle graphics documentation https://docs.python.org/3/library/turtle.html
#Color reference documentation https://cs111.wellesley.edu/reference/colors
import turtle
from turtle import Turtle, Screen
#import turtle as t -> We can create aliases for the imports that we do

tim = Turtle()
tim.shape("turtle")
tim.color("brown", "green")

#TO DO -> Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon

"""Angela's solution"""

colors = ["red", "blue", "purple", "black", "green", "gray", "pink","orange"]
def draw_shape(num_sides,colors):
    angle = 360 / num_sides #formula to define the angle
    for i in range(num_sides):
        random_color = random.choice(colors)
        tim.color(random_color, random_color)
        tim.forward(100)
        tim.right(angle)

for sides_n in range(3,11): #pretty interesting way to iterate from a for loop
    draw_shape(sides_n, colors)

"""def shape(tim, angle, sides): My solution to the challenge
    for i in range(sides):
        tim.forward(50)
        tim.right(angle)
        tim.forward(50)

shape(tim,120, 3) # draw a triangle
shape(tim, 90, 4) # draw a square
shape(tim, 72, 5) # draw a pentagon
shape(tim, 60, 6) # draw a hexagon
shape(tim, 51.42857142857143, 7) # draw a pentagon
shape(tim, 45, 8) # draw an octagon
shape(tim,40 , 9) # draw a nonagon
shape(tim,36 , 10) # draw a decagon """

""" How to create a dashed line 
for i in range(18):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()
"""




#DRAW A SQUARE WITH THE TURTLE
"""for i in range(4):
    tim.forward(100)
    tim.right(90)"""

#IMPORTING AN EXTERNAL MODULE, YOU NEED TO INSTALL IT
"""import heroes
print(heroes.gen())"""












screen = Screen()
screen.exitonclick()