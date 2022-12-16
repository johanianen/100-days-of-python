from turtle import Turtle

class Scoreboard(Turtle):

    score = 0
    score_text = "Score: " + str(score)

    def __init__(self):
        super().__init__()
        self.goto(0, 290)
        self.speed("fastest")
        self.penup
        self.update_score
        
    def update_score(self):
        self.clear()
        self.write(self.score_text, align="center", font=("Comic sans MS", 12, "normal"))