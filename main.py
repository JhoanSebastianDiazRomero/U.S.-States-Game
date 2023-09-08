import string
import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed = []

writer = Writer()

game_is_on = True
while game_is_on:
    if len(guessed) == 0:
        answer = string.capwords(screen.textinput(title="Guess the State", prompt="What's another state name?"))
    else:
        answer = string.capwords(
            screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state name?"))

    if answer == "Exit":
        game_is_on = False
    else:
        state_info = data[data.state == answer]
        state_dataframe = state_info.state
        state = state_dataframe.to_string(index=False)

        if not state_info.empty and state not in guessed:
            x = state_info.x.item()
            y = state_info.y.item()
            writer.write_state(x, y, state)
            guessed.append(state)

list_of_states = data.state.tolist()
missing_states = [state for state in list_of_states if state not in guessed]

missing_states_data = pandas.DataFrame(missing_states)
missing_states_data.to_csv("states_to_learn.csv")

screen.exitonclick()
