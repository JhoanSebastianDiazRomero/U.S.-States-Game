from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, x, y, state):
        self.goto(x, y)
        self.write(state)
