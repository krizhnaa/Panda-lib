import turtle
from turtle import Screen

screen = Screen()
image = 'blank_states_img.gif'

screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ")
print(answer_state)


turtle.mainloop()
