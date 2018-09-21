#sudo apt-get install python-tk

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
