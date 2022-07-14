from turtle import Turtle
POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(POSITION)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 1
        self.speed_up()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(POSITION)
        self.bounce_x()
        self.move_speed = 0.1

    def speed_up(self):
        self.ball_speed += 1
        self.speed(self.ball_speed)
