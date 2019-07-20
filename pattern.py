import turtle
import random


t = turtle.Turtle()

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
randnum = random.randint(1,10)
randX = random.randint(-00, 200)
randY = random.randint(-200, 200)
randoffset = random.randint(0, 100)
randwidth = random.randint(1, 150)
randheight = random.randint(1, 150)
randrotation = random.randint(0, 30)
randradius = random.randint(1, 60)
randcount = random.randint(1, 75)


def setup():
    turtle.setup(width=1000, height=800, startx=0, starty=0)
    t.showturtle()
    t.speed(60)
    return

def setRandomColor():
    color = random.choice(colors)
    t.color(color)
    return


def drawRectangle(newX, newY, width, height, offset, count, rotation):
    t.penup()
    t.goto(newX, newY)
    t.forward(offset)
    t.right(360/count)
    t.right(rotation)
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
    return


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(count):
        setRandomColor()
        drawRectangle(centerX, centerY, width, height, offset, count, rotation)

    return

def drawCircle(newX, newY, offset, radius, count):
    t.penup()
    t.goto(newX, newY)
    t.forward(offset)
    t.right(360 / count)
    t.pendown()
    t.circle(radius)
    t.penup()
    return


def drawCirclePattern(centerX, centerY, offset, radius, count):

    for i in range(count):
        setRandomColor()
        drawCircle(centerX, centerY, offset, radius, count)

    return


def drawSuperPattern(num):
    for i in range(num):
        randnum = random.randint(1, 10)
        randX = random.randint(-200, 200)
        randY = random.randint(-200, 200)
        randoffset = random.randint(0, 100)
        randwidth = random.randint(1, 150)
        randheight = random.randint(1, 150)
        randrotation = random.randint(0, 30)
        randradius = random.randint(1, 60)
        randcount = random.randint(1, 75)
        if (randnum >= 1 and randnum < 6):
                drawRectanglePattern(randX, randY, randoffset, randwidth, randheight, randcount, randrotation)
        elif (randnum > 5):
                drawCirclePattern(randX, randY, randoffset, randradius, randcount)

    return



def reset():
    turtle.clearscreen()
    return


def done():
    turtle.done()


    return