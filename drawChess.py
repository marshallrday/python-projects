'''Program that draws a chessboard with inputs from the user'''

import turtle

t = turtle.Turtle()

width = int(input("What is the width? "))
height = int(input("What is the height? "))
x = int(input("What is the x location? "))
y = int(input("What is the y location? "))

def drawChessboard(startX, startY, width = 250, height = 250):

    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.penup()

    for j in range(4):
        t.goto(startX, startY)
        startY = startY + (height * 2 / 8)

        for i in range(4):
                t.begin_fill()
                t.forward(width / 8)
                t.left(90)
                t.forward(height / 8)
                t.left(90)
                t.forward(width / 8)
                t.left(90)
                t.forward(width / 8)
                t.end_fill()
                t.penup()
                t.left(90)
                t.forward((width * 2) / 8)

    startY = startY - (height)
    startX = startX + (width / 8)

    for k in range(4):

            startY = startY + (height / 8)
            t.goto(startX, startY)
            startY = startY + (height / 8)

            for m in range(4):
                t.begin_fill()
                t.forward(width / 8)
                t.left(90)
                t.forward(height / 8)
                t.left(90)
                t.forward(width / 8)
                t.left(90)
                t.forward(width / 8)
                t.end_fill()
                t.penup()
                t.left(90)
                t.forward((width * 2) / 8)
    return

if width == "" and height == "":
        drawChessboard(x, y)
elif height == "":
        drawChessboard(x, y, (width))
elif width == "":
        drawChessboard(x, y, (height))
else:
        drawChessboard(x, y, (width), (height))




