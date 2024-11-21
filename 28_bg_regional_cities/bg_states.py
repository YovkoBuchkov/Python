import pandas
import turtle

screen = turtle.Screen()
screen.title = ("Bulgaria States Game")
image = "bg_states.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Courier", 18, "normal")

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

state_data = pandas.read_csv("bg_states.csv")
list_state = state_data.state.to_list()
guessed_states = []

for state in list_state:
    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    state_data_row = state_data[state_data.state == state]
    p.goto(state_data_row.x.item(), state_data_row.y.item() - 20)
    p.write(f"{state_data_row.people.item()}")

while len(guessed_states) < 28:
    guess = turtle.Turtle()
    guess.hideturtle()
    guess.penup()
    guess.goto(0, 250)
    guess.write(f"Познай областните градове, като виждаш населението в района!", align="center", font=FONT)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 Познати градове",
                                    prompt="Какъв е следващият областен град:").title()

    if answer_state in list_state and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data_row = state_data[state_data.state == answer_state]
        t.goto(state_data_row.x.item(), state_data_row.y.item())
        t.write(f"{answer_state}")


turtle.mainloop()