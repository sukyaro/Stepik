
import turtle

# Question 1
# Draw a rectangle with given width and height
def rectangle(width, height):
    turtle.showturtle()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

# Question 2
# Draw an equilateral triangle with given side length
def triangle(side):
    turtle.showturtle()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)

# Question 3
# Draw 18 rotated squares in a circular pattern
def square(side):
    turtle.showturtle()
    for i in range(18):
        turtle.left(20)
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

# Question 4
# Draw two overlapping squares with a rotated angle in between
def square2(side):
    turtle.showturtle()

    for _ in range(4):
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.left(90)

    turtle.left(45)
    
    for _ in range(4):
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.left(90)

# Question 5
# Draw a regular hexagon
def hexagon(side):
    turtle.showturtle()
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

# Question 6
# Draw a honeycomb-like pattern of hexagons
def honeycomb(side):
    turtle.showturtle()
    for _ in range(6):
        for _ in range(6):
            turtle.forward(side)
            turtle.left(60)

        turtle.left(60)
        turtle.forward(side)
        
# Question 7
# Draw a rhombus
def rhombus(side):
    turtle.showturtle()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(60)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)

# Question 8
# Draw 10 connected rhombuses rotated slightly each iteration
def rhombus2(side):
    turtle.showturtle()
    turtle.right(30)

    for _ in range(10):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(45)

# Question 9
# Draw a 6-point star by extending lines from the center
def star():
    turtle.showturtle()
    for _ in range(6):
        turtle.forward(50)
        turtle.backward(100)
        turtle.forward(50)
        turtle.left(30)

# Question 10
# Draw a 5-pointed star with given size
def realStar(size):
    turtle.showturtle()
    turtle.left(36)
    for _ in range(5):
        turtle.forward(size)
        turtle.left(144)

# Question 11
# Draw concentric squares increasing in size
def squareInSquare():
    turtle.showturtle()
    turtle.left(90)
    counter = 0

    for i in range(31):
        for _ in range(4):
            turtle.forward(15 + counter)
            turtle.left(90)
        counter += 5

# Question 12
# Draw a square spiral pattern
def spiral():
    turtle.showturtle()
    turtle.left(90)
    counter = 0
    for _ in range(20):
        turtle.forward(10 + counter)
        turtle.left(90)
        counter += 5


# Example calls to display shapes
rectangle(100, 50)
triangle(100)
square(200)
square2(100)
