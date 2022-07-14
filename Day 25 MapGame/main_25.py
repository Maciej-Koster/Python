import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
napis = turtle.Turtle()

napis.color("black")
napis.penup()
napis.hideturtle()


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
essa = pandas.read_csv("HighScore.csv")
essa2 = essa["0"]

correct_answer = essa2.tolist()


while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 States correct", prompt="What's another state's name?").title()
    print(answer_state)
    check = data[data["state"] == answer_state]

    if answer_state == "Exit":
        break
    if not check.empty:
        napis.goto(int(check["x"]), int(check["y"]))
        napis.write(arg=answer_state)
        correct_answer.append(answer_state)

    make_file = pandas.DataFrame(correct_answer)
    make_file.to_csv("HighScore.csv")

