import turtle
import pandas
screen = turtle.Screen()

screen.title("The US State game")
image = "blank_states_img.gif"
screen.setup(width=800, height=600)
screen.addshape(image)

turtle.shape(image)

guessed = []
count = 0

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"you guessed {count}/50", prompt="Whats another states name?").title()

    data = pandas.read_csv("50_states.csv")
    state_list = data["state"].to_list()
    for state in state_list:
        if state == answer_state:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            coor = data[data["state"]==answer_state]
            t.goto(int(coor["x"]), int(coor["y"]))
            t.write(state, align="center", font=("Arial", 7, "bold"))
            count+= 1
            guessed.append(state)
    if answer_state == "Exit":

        missing_states = [state for state in state_list if state not in guessed]

        mis_states = {
            "states you missed": missing_states,
        }

        df = pandas.DataFrame(mis_states)
        df.to_csv("missed.csv")
        break



