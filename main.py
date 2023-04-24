import turtle
import pandas

BG_IMAGE_NAME = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BG_IMAGE_NAME)
turtle.shape(BG_IMAGE_NAME)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []
attempts = 0

while attempts <= 50:
    answer_state = screen.textinput(title=f"{attempts}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in states:
        guessed_states.append(answer_state)
        label_name = turtle.Turtle()
        label_name.hideturtle()
        label_name.penup()
        state_data = data[data.state == answer_state]
        label_name.goto(x=int(state_data.iloc[0].x), y=int(state_data.iloc[0].y))
        label_name.write(answer_state, align="left")

    attempts += 1
