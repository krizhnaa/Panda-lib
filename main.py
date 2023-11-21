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
to_learn = []

is_game_on = True
count = 0

while is_game_on:
    if count == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ").title()
    else:
        answer_state = screen.textinput(title=f"{count_correct}/50", prompt="What's another state's name? ").title()
    df = pa.read_csv('50_states.csv')
    states = df['state']
    states_list = states.tolist()
    if answer_state == 'Exit':
        for state in states_list:
            if state not in correct_guess:
                to_learn.append(state)
        to_learn_df = pa.DataFrame(to_learn)
        to_learn_df.to_csv('states_to_learn.csv')
        is_game_on = False
    for state in states_list:
        if answer_state == state:
            x_loc = int(df[df['state'] == answer_state]['x'])
            y_loc = int(df[df['state'] == answer_state]['y'])
            s_turtle.penup()
            s_turtle.hideturtle()
            s_turtle.goto(x_loc, y_loc)
            s_turtle.write(f"{answer_state}", align='center')
            correct_guess.append(answer_state)
            count_correct = len(correct_guess)
        else:
            count_correct = len(correct_guess)
    count = 1

screen.exitonclick()
