#etch-a-sketch app
import random
import turtle



johnny = turtle.Turtle()
screen = turtle.Screen()
johnny.pendown()



def f():
    johnny.forward(10)

def b():
    johnny.backward(10)

def l():
    new_heading = johnny.heading() + 10
    johnny.setheading(new_heading)

def r():
    new_heading = johnny.heading() - 10
    johnny.setheading(new_heading)

screen.listen()
screen.onkeypress(f,"w")
screen.onkeypress(b,"s")
screen.onkeypress(l,"a")
screen.onkeypress(r,"d")
screen.onkeyrelease(johnny.reset,"c")


screen.exitonclick()