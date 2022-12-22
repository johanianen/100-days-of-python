from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

class Player:
    
    def __init__(self):
        self.player_turtle = Turtle(shape="turtle")
        self.player_turtle.penup()
        self.player_turtle.setheading(UP)
        self.player_turtle.goto(STARTING_POSITION)

    def move(self):
        self.player_turtle.forward(MOVE_DISTANCE)