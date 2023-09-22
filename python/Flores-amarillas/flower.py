import turtle
import random
import math

def drawPolygon(myTurtle, sides, length):
    angle = 360 / sides
    for side in range(sides):
        myTurtle.forward(length)
        myTurtle.left(angle)

def drawCircle(myTurtle, radius):
    circumference = 2 * math.pi * radius
    sides = 100
    length = circumference / sides
    drawPolygon(myTurtle, sides, length)

def drawArc(myTurtle, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    sides = int(arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = angle / sides

    for side in range(sides):
        myTurtle.forward(step_length)
        myTurtle.left(step_angle)

def drawPetal(myTurtle, radius, angle):
    drawArc(myTurtle, radius, angle)
    myTurtle.left(180-angle)
    drawArc(myTurtle, radius, angle)
    myTurtle.left(180-angle)

def drawFlower(myTurtle, petals, radius, angle):
    for petal in range(petals):
        drawPetal(myTurtle, radius, angle)
        myTurtle.left( 360 / petals )

def drawRandomFlower(myTurtle):
    petals = random.randint(5, 10)
    radius = random.randint(50, 150)
    angle = random.randint(5, 72)
    color = random.choice(['red', 'blue', 'green', 'black', 'orange'])

    distance = random.randrange(250)
    theta = random.randrange(359)

    # Set new color
    myTurtle.color(color)

    # Move to random position
    myTurtle.up()
    myTurtle.left(theta)
    myTurtle.forward(distance)

    # Draw Random Flower
    myTurtle.down()
    drawFlower(myTurtle, petals, radius, angle)

    # Go back to the home position.
    myTurtle.up()
    myTurtle.left(180)
    myTurtle.forward(distance)

window = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")
george.speed(0)

for i in range(15):
    drawRandomFlower(george)
