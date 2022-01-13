import turtle

MOVE_DISTANCE = 20

class Paddle(turtle.Turtle):

    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.penup()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.setposition(position)

    def move_down(self):
        new_y_cor = self.ycor() - MOVE_DISTANCE
        self.goto((self.xcor(), new_y_cor))

    def move_up(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.goto((self.xcor(), new_y_cor))
        
