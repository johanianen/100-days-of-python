from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from playsound import playsound
import os
import sys

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johans coola snake")
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        playsound("point.wav", False)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_is_on = False
        playsound("gameover.wav", False)
        scoreboard.game_over()
        

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            playsound("gameover.wav", False)
            scoreboard.game_over()

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def shutdown():
    os.exit(0)

while True:
    screen.listen()   
    #screen.onkey(shutdown, "Right")         
    #screen.onkey(restart, "Space")
