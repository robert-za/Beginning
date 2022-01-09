# import another_module
# import turtle
# print(another_module.another_variable)
# timmy = turtle.Turtle()
# print(timmy)
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOrchid4")
# timmy.shapesize(5,5,5)
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Raichu", "Geodude", "Jigglypuff"])
table.add_column("Type", ["Electric", "Electric", "Earth", "Fairy"])

table.align = "l"

print(table)