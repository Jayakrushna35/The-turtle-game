from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()
print(timmy_the_turtle)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green4")
color = ["Red", "Green", "Blue", "Yellow", "Orange"]
num_sides = 2
while num_sides < 7:
    num_sides += 1
    choose_color = random.choice(color)
    color.remove(choose_color)
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.color(choose_color)
        timmy_the_turtle.right(angle)

     

    

    










screen = Screen()
screen.exitonclick()