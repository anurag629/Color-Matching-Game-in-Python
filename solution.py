import turtle
import random

x_axis = -220
y_axis = 160
col = ["aqua", "red", "blue", "brown", "green"]
tile = {}

color_plate = {0: [col[0]],
               1: [col[1]],
               2: [col[2]],
               3: [col[3]],
               4: [col[4]]}

for i in range(25):
    cl = random.choice(col)
    print(cl)
    tile[i] = list(cl.split(" "))


for i in range(25):
    print(tile[i])


def draw_tiles(color, x, y):
    square = turtle.Turtle()
    square.hideturtle()
    square.penup()
    square.goto(x, y)
    square.speed(0)
    square.begin_fill()
    for i in range(4):
        square.forward(60)
        square.left(90)

    square.fillcolor(color)
    square.end_fill()
    square.pendown()


# tile = turtle.Turtle()


def board():
    for i in range(5):
        for j in range(5):
            tile[(i*5) + j].append(x_axis + (j*65))
            tile[(i*5) + j].append(y_axis - (i*65))

    for i in range(25):
        draw_tiles(tile[i][0], tile[i][1], tile[i][2])


def plate():
    for i in range(5):
        color_plate[i].append(-240 + (i*65))
        color_plate[i].append(-185)

    for i in range(5):
        draw_tiles(color_plate[i][0], color_plate[i][1], color_plate[i][2])


board()
plate()

# turtle.onscreenclick(draw_tiles)
turtle.mainloop()
