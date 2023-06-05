# This program will simulate random walk using turtle
import turtle
import numpy as np

heading = [0, 1, 2, 3] # 0-move right, 1-move up, 2-move left, 3-move down
steps = 1000
direction = np.random.choice(heading, size=steps)

x = turtle.getscreen()
x = turtle.Turtle()
x.speed(10)
for i in direction:
    x.setheading(90*i)
    x.forward(10)
