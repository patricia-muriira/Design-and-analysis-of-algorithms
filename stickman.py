import turtle

# Create a smaller Turtle object
heart = turtle.Turtle()
heart.speed(0)
heart.penup()
heart.shapesize(5)  # Set the Turtle size to make it smaller
heart.color("red")

# Function to draw a red heart
def draw_heart(size):
    heart.shape("classic")
    heart.stamp()
    heart.hideturtle()
    heart.shape("triangle")

# Draw many small red hearts
for _ in range(20):
    x = -200 + _ * 50  # Adjust the x-coordinate for positioning
    y = 0  # Adjust the y-coordinate for positioning
    size = 5 # Adjust the size of the hearts
    heart.goto(x, y)
    draw_heart(size)

# Close the Turtle graphics window on click
turtle.done()
