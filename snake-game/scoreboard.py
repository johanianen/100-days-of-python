from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("consolas", 20, "normal")
class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.speed("fastest")
        self.penup
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write("Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.goto(0, -25)
        self.write("Play again?", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.goto(0, -50)
        self.write("y/n", align=ALIGNMENT, font=FONT)