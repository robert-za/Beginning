from turtle import Turtle, Screen
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win?: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
xaxis = -220
yaxis = -100

for color in colors:
    name = color
    name = Turtle("turtle")
    name.color(color)
    name.penup()
    name.goto(xaxis, yaxis)
    yaxis += 40
    all_turtles.append(name)

  
if user_bet:
    is_race_on = True

while is_race_on:
    for name in all_turtles:
        if name.xcor() > 230:
            is_race_on = False
            winning_turtle = name.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won. The {winning_turtle} turtle won!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        name.forward(rand_distance)


screen.exitonclick()