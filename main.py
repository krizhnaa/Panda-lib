import turtle
from turtle import Screen
import pandas as pa

screen = Screen()
image = 'blank_states_img.gif'

screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

s_turtle = turtle.Turtle()

correct_guess = []

is_game_on = True
count = 0

while is_game_on:
    if count == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ").title()
    else:
        answer_state = screen.textinput(title=f"{count_correct}/50", prompt="What's another state's name? ").title()
    df = pa.read_csv('50_states.csv')
    x_loc = int(df[df['state'] == answer_state]['x'])
    y_loc = int(df[df['state'] == answer_state]['y'])
    states = df['state']
    states_list = states.tolist()
    for state in states_list:
        if answer_state == state:
            s_turtle.penup()
            s_turtle.hideturtle()
            s_turtle.goto(x_loc, y_loc)
            s_turtle.write(f"{answer_state}", align='center')
            correct_guess.append(answer_state)
            count_correct = len(correct_guess)

    count = 1

turtle.mainloop()
