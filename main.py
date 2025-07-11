import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player=Player()
new_car=CarManager()
my_score=Scoreboard()

screen.listen()
screen.onkey(new_player.moveUp,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car.create_car()
    new_car.move_car()

    #Detect collision with Car
    for car in new_car.all_cars:
        if car.distance(new_player) < 20:
            my_score.game_over()
            game_is_on=False


    #Detect Succesful crossing
    if new_player.if_at_finishline():
        new_player.go_to_start()
        new_car.level_up()
        my_score.increase_level()

screen.exitonclick()
