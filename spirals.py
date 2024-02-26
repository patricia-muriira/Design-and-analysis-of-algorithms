import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
spiral = turtle.Turtle()
spiral.shape("turtle")
spiral.color("white")
spiral.speed(0)

# Function to draw a colorful spiral
def draw_spiral(sides, length, angle):
    for _ in range(sides):
        spiral.forward(length)
        spiral.right(angle)
        spiral.color("red")
        length += 5
        angle += 2

# Draw the colorful spiral
draw_spiral(100, 50, 90)

# Close the Turtle graphics window on click
screen.exitonclick()
