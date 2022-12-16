from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johans coola snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(position)
    segments.append(segment)

screen.exitonclick()

#testar igen och igen
