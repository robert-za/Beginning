class Snake:

    def initialize():
        for position in starting_positions:
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(position)
            segments.append(snake_body)
        screen.update()

    def move():
        segments = []
        for segment_num in range(len(segments) - 1, 0, -1):
                new_x = segments[segment_num - 1].xcor()
                new_y = segments[segment_num - 1].ycor()
                segments[segment_num].goto(new_x, new_y)
        segments[0].forward(20)