import random
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("classic")
tim.color("red")
tim.pensize(10)
walks = [tim.lt(90), tim.rt(90), tim.back(10)]

print(random.choice(walks))
