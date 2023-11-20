import turtle
from turtle import Screen
import pandas as pa

screen = Screen()
image = 'blank_states_img.gif'

screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

is_game_on = True

while is_game_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ").title()
    df = pa.read_csv('50_states.csv')
    states = df['state']
    states_list = states.tolist()
    for state in states_list:
        if answer_state == state:
            print("Damnnnnn")


turtle.mainloop()
