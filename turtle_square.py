from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
print(timmy_the_turtle)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green4")

#To make a square

for _ in range(5):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()