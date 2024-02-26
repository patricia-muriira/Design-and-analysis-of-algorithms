import turtle
import random
import math

# Create a Turtle object
screen = turtle.Screen()
screen.bgcolor("black")
celestial = turtle.Turtle()
celestial.speed(0)  # Set the drawing speed (you can adjust this)

# Function to draw a star
def draw_star(size):
    celestial.begin_fill()
    for _ in range(5):
        celestial.forward(size)
        celestial.right(144)
    celestial.end_fill()

# Function to draw a crescent moon
def draw_crescent_moon(radius):
    celestial.begin_fill()
    celestial.left(90)
    for _ in range(360):
        x = radius * math.sin(math.radians(_))
        y = radius * math.cos(math.radians(_)) - radius
        celestial.goto(x, y)
    celestial.goto(0, -radius)
    celestial.end_fill()

# Set the number of stars and their random positions
num_stars = 50

for _ in range(num_stars):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    celestial.penup()
    celestial.color(random.choice(["white", "yellow"]))
    celestial.goto(x, y)
    celestial.pendown()
    star_size = random.randint(5, 20)
    draw_star(star_size)

# Draw a crescent moon
celestial.penup()
celestial.color("white")
celestial.goto(100, 50)
celestial.pendown()
moon_radius = 30
draw_crescent_moon(moon_radius)

# Close the Turtle graphics window on click
screen.exitonclick()
