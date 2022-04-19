import turtle
import random

col = ["aqua", "banana", "blue", "brown", "green"]
tile = {}


for i in range(25):
    cl = random.choice(col)
    print(cl)
    tile[i] = list(cl.split(" "))
    

for i in range(25):
    print(tile[i])


def draw_tiles(x, y):
    square = turtle.Turtle()
    square.hideturtle()
    square.penup()
    square.goto(x, y)
    square.speed(0)
    square.begin_fill()
    for i in range(4):
        square.forward(60)
        square.left(90)

    square.fillcolor("red")
    square.end_fill()
    square.pendown()


turtle.onscreenclick(draw_tiles)
turtle.mainloop()
