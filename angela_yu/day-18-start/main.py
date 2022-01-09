from turtle import Screen, Turtle
import random
import turtle


johnny = Turtle()
johnny.shape("turtle")
johnny.color("black")
colours = ["blue", "yellow", "pink", "orange", "red", "green", "brown", "violet"]

# # CREATE SHAPES VORTEX += 1 IN RANDOM COLOURS
# johnny.pendown()
# for vortex in range(3,11):
#     johnny.color(random.choice(colours))
#     for edges in range(vortex):
#         turn_angle = 360 / vortex
#         johnny.forward(100)
#         johnny.left(turn_angle)



johnny.pensize(1)
johnny.pendown()
johnny.speed(0)
turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for _ in range(200):
    
#     johnny.pencolor(random_colour())
#     random_angle = random.randint(0,360)
#     random_distance = random.randint(20,40)
#     johnny.left(random_angle)
#     johnny.forward(random_distance)
angle = 5
steps = 360 // angle + 1
for _ in range(steps):
    johnny.pencolor(random_colour())
    johnny.circle(100)
    johnny.left(angle)



screen = Screen()
screen.exitonclick()