from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-200, y=250)
        self.write(arg=f"Level: {self.score}", align="center", font=(FONT))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=(FONT))
