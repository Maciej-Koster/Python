import turtle as t
import random
import colorgram

colors = colorgram.extract('dot.jpg', 36)
list_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tuple_rgb = (r, g, b)
    list_color.append(tuple_rgb)

screen = t.Screen()

# Setting the screen color-mode
screen.colormode(255)

t.hideturtle()
t.penup()
x_start = -250
x_cor = -250
y_cor = -250

while y_cor <= 200:
    while x_cor <= 200:
        t.goto(x=x_cor, y=y_cor)
        color = random.choice(list_color)
        t.dot(20, color)
        x_cor = x_cor + 50
    x_cor = x_start
    y_cor = y_cor + 50



screen.exitonclick()
