from turtle import Turtle
import pandas as py

df = py.read_csv('50_states.csv')

x_loc = int(df[df['state'] == answer]['x'])
y_loc = int(df[df['state'] == answer]['y'])

class Displaystate(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("state", align='center')
        self.goto(self.get_location())

    def get_location(self, answer):
        self.x_loc = int(df[df['state'] == answer]['x'])
        self.y_loc = int(df[df['state'] == answer]['y'])
        self.goto(self.x_loc, self.y_loc)
