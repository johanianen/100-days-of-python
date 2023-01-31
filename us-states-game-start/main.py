import turtle
import pandas
import numpy
import time

ERROR_POSITION = (0, 200)
ERROR_FONT = ("consolas", 20)
ERROR_SLEEPTIME = 2

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.penup()
text.hideturtle()

error_text = turtle.Turtle()
error_text.penup()
error_text.hideturtle()
error_text.color("red")

states_data = pandas.read_csv("./50_states.csv")
states_list = states_data["state"].to_list()
correct_guesses = []
wrong_guesses = []
strikes = 0
score = len(correct_guesses)

while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Type the name of a U.S. state")
    answer = answer.title()
    if answer not in states_list:
        strikes += 1
        wrong_guesses.append(answer)
        error_text.goto(ERROR_POSITION)
        error_text.write("Nope, that's not a U.S. State", align="center", font=ERROR_FONT)
        time.sleep(ERROR_SLEEPTIME)
        error_text.clear()

    elif answer in correct_guesses:
        strikes += 1
        error_text.goto(ERROR_POSITION)
        error_text.write("You've already guessed that state", align="center", font=ERROR_FONT)
        time.sleep(ERROR_SLEEPTIME)
        error_text.clear()


    elif answer in wrong_guesses:
        strikes += 3
        error_text.goto(ERROR_POSITION)
        error_text.write("I already told you once this wasn't a U.S. State! You lose!", align="center", font=ERROR_FONT)
        time.sleep(ERROR_SLEEPTIME)
        error_text.clear()

    else:
        xcor = states_data.loc[states_data["state"] == answer, "x"].item()
        ycor = states_data.loc[states_data["state"] == answer, "y"].item()
        text.goto(xcor, ycor)
        text.write(answer, align="center")

        correct_guesses.append(answer)
        
    if strikes >= 3:
        break

rgb_weights = [0.2989, 0.5870, 0.1140]
grayscale_image = numpy.dot(image[...,:3], rgb_weights)
screen.addshape(image)
turtle.shape(image)

turtle.mainloop()

