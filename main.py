#turtle crossing game
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup( 600 , 600)
screen.tracer(0)

player  = Player()
Car_manager = CarManager()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    Car_manager.create_car()
    Car_manager.move_cars()

    for car in Car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on =False
            Scoreboard.game_over()

    #detect crossing
    if player.is_at_finish_line():
        player.go_to_start()      
        Car_manager.level_up()
        Scoreboard.increase_level()




screen.exitonclick()