from turtle import Turtle
from time import sleep
FONT = ("consolas", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()

        self.level = 1

        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-270, 250)
        self.write("Level:" + str(self.level), font=FONT)

    def next_level(self):
        self.level += 1
        self.goto(0, 0)
        self.write("Level complete!", font=FONT, align=ALIGN)
        sleep(3)
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", font=FONT, align=ALIGN)

        
