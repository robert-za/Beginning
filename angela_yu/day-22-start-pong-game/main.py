import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()

left_paddle = Paddle((-380,0))
right_paddle = Paddle((380,0))

ball = Ball()
screen.update()
score = Scoreboard()

screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(left_paddle.move_up, "w")

screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(right_paddle.move_up, "Up")

is_game_on = True

while is_game_on:

    time.sleep(ball.swiftness)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 360:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()

