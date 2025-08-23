
import turtle
from random import *
import math

# Question 1
# Draw a house with a blue square base and brown triangular roof
def house():
    turtle.showturtle()
    turtle.begin_fill()
    turtle.fillcolor("blue")

    for _ in range(4):
        turtle.forward(80)
        turtle.left(90)

    turtle.end_fill()
    turtle.penup()

    turtle.goto(-20, 80)

    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("brown")

    for _ in range(3):
        turtle.forward(120)
        turtle.left(120)

    turtle.end_fill()

# Question 2
# Draw a vertical traffic light with green, yellow, and red lights
def traffic_light():
    turtle.showturtle()
    colours = ["green", "yellow", "red"]
    counter = 0

    turtle.begin_fill()
    turtle.fillcolor("black")

    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)

    turtle.end_fill()
    turtle.penup()

    for i in range(3):
        turtle.begin_fill()
        turtle.fillcolor(colours[i])
        turtle.goto(25, 10 + counter)
        turtle.circle(15)
        turtle.end_fill()
        counter += 40

    turtle.hideturtle()

# Question 3
# Draw an optical illusion triangle with black and white filled circles
def ilusion():
    turtle.showturtle()
    triangle_coords = [(0, 50), (100, 50), (50, -35)]

    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    
    turtle.penup()

    for i in range(3):
        turtle.begin_fill()
        turtle.fillcolor('black')
        turtle.goto(triangle_coords[i][0], triangle_coords[i][1])
        turtle.circle(15)
        turtle.end_fill()

    turtle.goto(0, 65)
    turtle.pencolor("white")
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.fillcolor("white")

    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

    turtle.end_fill()

# Question 4
# Draw 10 rainbow-colored concentric circles
def rainbow_circles():
    colours = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", "#1E56FC","#4800FF","#CC00FF","#FF5099"]
    radius = 100
    turtle.hideturtle()
    turtle.speed(7)

    for i in range(10):
        turtle.penup()
        turtle.goto(0, 10 * i)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(colours[i])
        turtle.circle(radius)
        turtle.end_fill()
        radius -= 10

# Question 5
# Draw a crescent moon using two overlapping circles
def moon():
    turtle.Screen().bgcolor("blue")
    turtle.hideturtle()
    turtle.pencolor("blue")

    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(100)
    turtle.end_fill()

    turtle.goto(20, 0)
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.circle(100)
    turtle.end_fill()

# Question 6
# Animate a sun being covered by a moving blue circle simulating day to night
def day_night():
    screen = turtle.Screen()
    screen.setup(400, 400)
    screen.bgcolor("blue")
    screen.tracer(0)

    sun = turtle.Turtle()
    cover = turtle.Turtle()

    sun.hideturtle()
    sun.speed(0)
    cover.hideturtle()
    cover.speed(0)

    for i in range(400):
        sun.clear()
        cover.clear()
        sun.penup()
        sun.begin_fill()
        sun.fillcolor("yellow")
        sun.goto(0, -100)
        sun.circle(100)
        sun.end_fill()

        cover.penup()
        cover.begin_fill()
        cover.fillcolor("blue")
        cover.goto(200 - i, -100)
        cover.circle(100)
        cover.end_fill()
        screen.update()

# Question 7
# Draw a filled regular polygon with n sides and given area
def shapes(n, area):
    size = math.sqrt((4 * area * math.tan(math.pi / n)) / n)
    colour = tuple(randint(0, 255) for _ in range(3))
    turtle.fillcolor(colour)
    turtle.begin_fill()

    turtle.forward(size / 2)
    turtle.left(360 / n)
    for i in range(n - 1):
        turtle.forward(size)
        turtle.left(360 / n)
    turtle.forward(size / 2)

    turtle.end_fill()

# Question 8
# Draw a grid of 5x5 random polygons
def main():
    turtle.Screen().setup(500, 500)
    turtle.speed(5)
    turtle.hideturtle()
    x, y = -150, 130 

    for i in range(5):
        for j in range(5):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            shapes(randint(3, 6), 1800)
            x += 75
        x = -150
        y -= 75

# Question 9
# Draw a chessboard with alternating black squares
def chess_board():
    turtle.Screen().setup(500, 500)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-240, 240)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(480)
        turtle.right(90)

    choice = 1

    for x in range(-240, 240, 96):
        for y in range(240, -240, -96):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            if choice == 1:
                turtle.begin_fill()
                turtle.fillcolor("black")

            for _ in range(4):
                turtle.forward(96)
                turtle.right(90)

            if choice == 1:
                turtle.end_fill()

            choice = 0 if choice == 1 else 1

# Question 10
# Draw a compass with four labeled directions
def compass():
    turtle.Screen().setup(400, 400)
    turtle.hideturtle()
    coords = [["Восток", "center"], ["Север", "center"], ["Запад", "center"], ["Юг", "center"]]
    turtle.circle(20)
    turtle.penup()
    turtle.goto(0, 20)

    for i in range(4):
        turtle.pendown()
        turtle.forward(80)
        turtle.penup()
        turtle.forward(20)
        turtle.write(coords[i][0], align=coords[i][1])
        turtle.left(180)
        turtle.forward(100)
        turtle.right(90)

# Question 11
# Draw a planetary system with labeled colored planets, including Saturn's ring
def planet(planets, colours):
    turtle.Screen().setup(900, 200)
    turtle.Screen().bgcolor('black')
    turtle.hideturtle()
    turtle.speed(0)

    for i in planets:
        x, y = planets[i][0]
        if i == 'Saturn':
            r = planets[i][1]
            radius_x = r + 25
            radius_y = r // 2 + 5

            turtle.penup()
            turtle.pencolor('gray')
            turtle.goto(x + radius_x, y + 50)
            turtle.pendown()

            for angle in range(0, 361):
                rx = radius_x * math.cos(math.radians(angle))
                ry = radius_y * math.sin(math.radians(angle))
                turtle.goto(x + rx, y + ry + 50)

        turtle.penup()
        turtle.goto(x, y)
        turtle.pencolor("black")
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(colours[i])
        turtle.circle(planets[i][1])
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x, y - 10)
        turtle.pencolor('white')
        turtle.pendown()
        turtle.write(i, align='center', font=('Arial', 8, 'normal'))

# Question 12
# Draw a STOP sign with black border and red fill, write "STOP" in center
def stop_sign():
    turtle.Screen().setup(400, 400)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-75, -190)
    turtle.pendown()

    turtle.begin_fill()
    turtle.fillcolor("black")
    for i in range(8):
        turtle.forward(150)
        turtle.left(45)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-72, -184)
    turtle.pendown()
    for i in range(8):
        turtle.forward(144)
        turtle.left(45)

    turtle.penup()
    turtle.goto(-66, -178)
    turtle.pencolor("white")
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    for i in range(8):
        turtle.forward(138)
        turtle.left(45)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 0)
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.pendown()
    turtle.write("STOP", align='center', font=('Arial', 60, 'normal'))
    turtle.end_fill()
