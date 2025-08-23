
import turtle
import random as ran

# Question 1
# Draw a dotted line with 5 dots
def dottedLine():
    turtle.showturtle()
    turtle.shape('dot')
    turtle.pensize(10)
    for _ in range(5):
        turtle.dot()
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()

# Question 2
# Draw a rectangle with large corner dots
def superRictangle():
    turtle.showturtle()
    turtle.shape('square')
    for _ in range(2):
        turtle.pensize(30)
        turtle.dot()
        turtle.pensize(10)
        turtle.forward(100)
        turtle.pensize(30)
        turtle.dot()
        turtle.pensize(10)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

# Question 3
# Draw a net with arrows and stamps rotated by given angle
def net(angle):
    turtle.showturtle()
    turtle.shape('arrow')
    turtle.pensize(10)
    turtle.dot()
    turtle.pensize(2)
    for _ in range(angle):
        turtle.forward(100)
        turtle.stamp()
        turtle.penup()
        turtle.left(180)
        turtle.forward(100)
        turtle.left(180)
        turtle.left(360/angle)
        turtle.pendown()

# Question 4
# Draw a circular net of turtle stamps
def netPro():
    turtle.showturtle()
    turtle.shape('turtle')
    turtle.stamp()
    turtle.penup()
    for _ in range(10):
        turtle.forward(50)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(50)
        turtle.left(180)
        turtle.left(35)

# Question 5
# Draw a turtle-themed clock with 12 hour marks
def turtleClock():
    turtle.showturtle()
    turtle.Screen().bgcolor('blue')
    turtle.shape('turtle')
    turtle.stamp()
    turtle.penup()
    for _ in range(12):
        turtle.forward(50)
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(70)
        turtle.left(180)
        turtle.left(30)

# Question 6
# Draw a stamped spiral with increasing steps
def turtleSpiral():
    turtle.showturtle()
    turtle.Screen().bgcolor('lightgreen')
    turtle.shape('turtle')
    turtle.penup()
    counter = 0
    for i in range(30):
        turtle.stamp()
        turtle.right(30)
        turtle.forward(5 + counter * 2)
        counter += 1

# Question 7
# Draw a multicolor spiral with increasing pen size
def coolSpiral():
    turtle.showturtle()
    counter = 2
    colours = ['red', 'green', 'orange', 'purple', 'blue', 'yellow', 'black']
    for i in range(30):
        turtle.pencolor(ran.choice(colours))
        turtle.forward(counter)
        turtle.left(40)
        turtle.pensize(i)
        counter += 2

# Question 8
# Draw two connected triangles as a simple star
def star():
    turtle.showturtle()
    for _ in range(2):
        turtle.pendown()
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.penup()
        turtle.goto(100, 50)
        turtle.left(180)
    turtle.hideturtle()

# Question 9
# Draw a net of colored dots radiating from center
def wierdNet():
    turtle.showturtle()
    turtle.pencolor('red')
    turtle.dot()
    turtle.pencolor('green')
    for i in range(10):
        turtle.goto(-200 + i * 40, -200)
        turtle.pencolor('blue')
        turtle.dot()
        turtle.pencolor('green')
        turtle.goto(0, 0)

# Question 10
# Draw Olympic rings in correct positions and colors
def olimpics():
    turtle.showturtle()
    turtle.pensize(5)

    radius = 50

    points = {1: {"pos": (0, 0),                 "colour" : "blue"},
              2: {"pos": (radius * 2, 0),        "colour" : "black"},
              3: {"pos": (radius * 4, 0),        "colour" : "red"},
              4: {"pos": (radius, -radius),      "colour" : "yellow"},
              5: {"pos": (radius * 3, -radius),  "colour" : "green"}
             }
    
    for i in range(1, 6):
        turtle.penup()
        turtle.pencolor(points[i]["colour"])
        turtle.goto(points[i]["pos"])
        turtle.pendown()
        turtle.circle(radius)

# Question 11
# Draw a bear face with head, eyes, nose, mouth, and ears
def bear():
    turtle.showturtle()
    turtle.pensize(3)
    turtle.pencolor("brown")
    turtle.penup()
    turtle.goto(0, -100)

    #Head
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()

    #Mouth
    turtle.pendown()
    turtle.circle(50)
    
    #Nose
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.pencolor("red")
    turtle.circle(10)
    turtle.penup()
    
    #Eyes
    turtle.pencolor("black")
    turtle.goto(-40, 40)
    turtle.pendown()
    turtle.pensize(20)
    turtle.dot()
    turtle.penup()
    turtle.goto(40, 40)
    turtle.pendown()
    turtle.dot()
    turtle.penup()
    
    #Left Ear
    turtle.pencolor("brown")
    turtle.goto(-68, 75)
    turtle.pendown()
    turtle.pensize(3)
    turtle.left(60)
    turtle.circle(30)
    turtle.penup()
    
    #Right Ear
    turtle.goto(68, 75)
    turtle.pendown()
    turtle.pensize(3)
    turtle.right(120)
    turtle.circle(30)
