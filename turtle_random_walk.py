from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()
print(timmy_the_turtle)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green4")

direction = [0 , 90, 180, 270]
timmy_the_turtle.width(12)
timmy_the_turtle.speed(14)

def tcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = "#%02x%02x%02x" % (r, g, b)  # Convert to hexadecimal
    return random_color


for _ in range(200):
    timmy_the_turtle.color(tcolor())
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()