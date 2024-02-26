import turtle

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (you can adjust this)

# Define the function to draw each letter
def draw_letter(letter, size):
    if letter == 'P':
        pen.penup()
        pen.goto(-50, 0)
        pen.pendown()
        pen.setheading(90)
        pen.forward(100)
        pen.setheading(0)
        pen.forward(40)
        pen.setheading(-90)
        pen.forward(100)
    elif letter == 'a':
        pen.penup()
        pen.goto(20, 0)
        pen.pendown()
        pen.setheading(0)
        pen.circle(50, 360)
        pen.penup()
        pen.goto(40, 0)
    elif letter == 't':
        pen.penup()
        pen.goto(100, 0)
        pen.pendown()
        pen.setheading(90)
        pen.forward(100)
        pen.setheading(180)
        pen.forward(30)
        pen.penup()
        pen.goto(70, 0)
    elif letter == 'r':
        pen.penup()
        pen.goto(150, 0)
        pen.pendown()
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(215)
        pen.circle(30, 90)
        pen.penup()
        pen.goto(140, 0)
    elif letter == 'i':
        pen.penup()
        pen.goto(180, 0)
        pen.pendown()
        pen.setheading(90)
        pen.forward(100)
        pen.penup()
        pen.goto(190, 0)
    elif letter == 'c':
        pen.penup()
        pen.goto(220, 0)
        pen.pendown()
        pen.setheading(90)
        pen.circle(50, 180)
        pen.penup()
        pen.goto(220, 0)
    elif letter == 'a':
        pen.penup()
        pen.goto(300, 0)
        pen.pendown()
        pen.setheading(0)
        pen.circle(50, 360)
        pen.penup()
        pen.goto(320, 0)

# Write the name "Patricia"
name = "Patricia"
pen.penup()
pen.goto(-100, 0)

for letter in name:
    draw_letter(letter, 30)

# Close the Turtle graphics window on click
turtle.done()
