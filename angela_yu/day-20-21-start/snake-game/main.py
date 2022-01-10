from turtle import Turtle, Screen, forward, st
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

starting_positions = [(0, 0), (0, 20), (0, 40)]
segments = []

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
screen.exitonclick()