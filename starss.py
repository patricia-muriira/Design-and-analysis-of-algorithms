import turtle
import random

# Create a Turtle object
screen = turtle.Screen()
screen.bgcolor("black")
star = turtle.Turtle()
star.speed(0)  # Set the drawing speed (you can adjust this)

# Function to draw a star
def draw_star(size):
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Set the number of stars and their random positions
num_stars = 5000

for _ in range(num_stars):
    x = random.randint(-700, 700)
    y = random.randint(-700, 700)
    star.penup()
    star.color(random.choice(["white", "yellow", "lightblue", "red", "green"]))
    star.goto(x, y)
    star.pendown()
    star_size = random.randint(10, 30)
    draw_star(star_size)

# Close the Turtle graphics window on click
screen.exitonclick()
