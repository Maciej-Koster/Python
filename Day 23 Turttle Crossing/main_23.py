import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

car_list = list()
i = 0
time_to_make_car = 0
game_speed = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    new_cars_create = random.randrange(0, 3, 1)

    if time_to_make_car == 5:
        for i in range(new_cars_create):
            car_list.append(CarManager())
        time_to_make_car = 0

    for new_car in car_list:
        new_car.move_car()

        if new_car.xcor() < -300:
            new_car.hideturtle()
            car_list.remove(new_car)

        if new_car.distance(player) < 20:
            car_list.clear()
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 270:
        player.next_lvl()
        scoreboard.score += 1
        scoreboard.update_scoreboard()

        for new_car in car_list:
            new_car.hideturtle()
        car_list.clear()
        game_speed *= 0.9

    time_to_make_car += 1


screen.exitonclick()