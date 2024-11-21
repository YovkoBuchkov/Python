import pandas
import turtle

screen = turtle.Screen()
screen.title = ("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

state_data = pandas.read_csv("50_states.csv")
list_state = state_data.state.to_list()
quessed_states = []

while len(quessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(quessed_states)}/50 States Correct",
                                    prompt="What`s another state`s name:").title()

    if answer_state in list_state:
        quessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state_data[state_data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)




turtle.mainloop()