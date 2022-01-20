import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50", prompt = "What's another state's name?").title()
    
    if answer_state == "Exit":
        df = pd.DataFrame(all_states)
        df.to_csv("missing_states.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_state_data = data[data.state == answer_state]
        t.goto(int(answer_state_data.x), int(answer_state_data.y))
        t.write(answer_state)
        all_states.remove(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()

