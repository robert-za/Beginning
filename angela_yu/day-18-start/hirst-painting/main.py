# import colorgram

# colors = colorgram.extract('image.jpg', 10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

color_list = [(113, 98, 59), (39, 22, 35), (19, 14, 35), (65, 41, 28), (148, 141, 82), (180, 165, 98), (81, 102, 75), 
              (80, 69, 37), (91, 71, 80), (239, 203, 111)]


from turtle import Screen, Turtle
import random
import turtle

turtle.colormode(255)
#Init
johnny = Turtle()
johnny.penup()
johnny.backward(500)
johnny.right(90)
johnny.forward(300)
johnny.left(90)
#End of Init
# johnny.pendown()
johnny.pensize(20)
johnny.speed(0)

for y in range(10):
    for x in range(10):
        johnny.dot(20, random.choice(color_list))
        if x < 9:
            johnny.forward(50)
    if y % 2 == 0 and y != 9:
        johnny.left(90)
        johnny.forward(50)
        johnny.left(90)
        johnny.dot(20, random.choice(color_list))
    elif y % 2 != 0 and y != 9:
        johnny.right(90)
        johnny.forward(50)
        johnny.right(90)
        johnny.dot(20, random.choice(color_list))

screen = Screen()
screen.exitonclick()