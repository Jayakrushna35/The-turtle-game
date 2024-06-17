from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()
print(timmy_the_turtle)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green4")

timmy_the_turtle.speed(14)

def tcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = "#%02x%02x%02x" % (r, g, b)  # Convert to hexadecimal
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.color(tcolor())
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+ size_of_gap)

draw_spirograph(4)
screen = Screen()
screen.exitonclick()