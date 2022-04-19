import turtle
import random

turtle.speed(0)
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
    tile[i] = list(cl.split(" "))


def draw_tiles(color, x, y, border):
    square = turtle.Turtle()
    square.speed(0)
    square.hideturtle()
    if(border == 1):
        square.speed(0)
        square.penup()
        square.goto(x, y)
        square.pendown()
        square.pensize(2.5)
        square.begin_fill()
        for i in range(4):
            square.forward(60)
            square.left(90)

        square.fillcolor(color)
        square.end_fill()

    else:
        square.speed(0)
        square.penup()
        square.goto(x, y)
        square.pendown()
        square.pensize(2.5)
        square.pencolor("white")
        square.begin_fill()
        for i in range(4):
            square.forward(60)
            square.left(90)

        square.fillcolor(color)
        square.end_fill()


def board():
    for i in range(5):
        for j in range(5):
            tile[(i*5) + j].append(x_axis + (j*65))
            tile[(i*5) + j].append(y_axis - (i*65))
            tile[(i*5) + j].append(0)

    for i in range(25):
        draw_tiles(tile[i][0], tile[i][1], tile[i][2], tile[i][3])


def plate():
    for i in range(5):
        color_plate[i].append(-240 + (i*65))
        color_plate[i].append(-185)
        color_plate[i].append(1)

    for i in range(5):
        draw_tiles(color_plate[i][0], color_plate[i][1],
                   color_plate[i][2], color_plate[i][3])


def logic(tile_selected, color_selected):
    pass


def catch_color(x, y):
    tile_selected = []
    color_plate_selected = []

    for i in range(25):
        if((x > tile[i][1]) and (x < tile[i][1] + 60) and (y > tile[i][2]) and (y < tile[i][2] + 60)):
            tile[i][3] = 1
            tile_selected.append(tile[i][0])
        else:
            tile[i][3] = 0

        draw_tiles(tile[i][0], tile[i][1], tile[i][2], tile[i][3])

    for i in range(5):
        if((x > color_plate[i][1]) and (x < color_plate[i][1] + 60) and (y > color_plate[i][2]) and (y < color_plate[i][2] + 60)):
            print(color_plate[i][0])
            color_plate_selected.append(color_plate[i][0])


board()
plate()

turtle.onscreenclick(catch_color)
turtle.mainloop()
