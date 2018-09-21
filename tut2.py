import turtle


win = turtle.Screen()
win.bgcolor("white")

tess = turtle.Turtle()

tess.speed(0)
tess.color("blue")
tess.pensize(5)
offSet=30

def doNextEvent(x,y):

    global offSet
    global win
    tess.forward(20)
    tess.left(1+offSet)
    offSet=offSet-2
    if(offSet<1):
        win.exitonclick()


win.onclick(doNextEvent)
win.listen()
win.mainloop()
