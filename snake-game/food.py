from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-15,15)*20, random.randint(-15,15)*20)
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))