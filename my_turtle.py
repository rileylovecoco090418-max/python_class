import turtle

# Create the screen (canvas)
screen = turtle.Screen()
screen.title("My First Turtle Art")
#screen.screensize(600, 400, "white")
screen.setup(width=800, height=800)

# Create the turtle (the drawing pen)
t = turtle.Turtle()
t.shape("turtle") # Can be 'arrow', 'turtle', 'circle', 'square'

# Keep the window open
turtle.done()