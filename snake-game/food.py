from turtle import Turtle
import random

class Food(Turtle):

    colorlist = []

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.colorlist.append(new_color)
        self.color(new_color)
        

        