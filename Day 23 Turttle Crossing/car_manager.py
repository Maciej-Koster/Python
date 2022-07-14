from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.random_start()
        self.seth(180)

    def random_start(self):
        random_x = 300
        random_y = random.randint(-240, 270)
        self.goto(x=random_x, y=random_y)

    def move_car(self):
        self.forward(10)