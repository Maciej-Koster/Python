from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Eneter a color")
#print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_start = -100

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=y_start)
    y_start += 40
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won, The {winning_color} is the winner")
            else:
                print(f"You have lost, , The {winning_color} is the winner")
            is_race_on = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()