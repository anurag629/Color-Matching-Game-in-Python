import turtle
import random

turtle.speed(0)  # this makes the speed fo turtle to fastest
x_axis = -220  # global variable to store the first block x-axis
y_axis = 160  # global variable to store the first block y-axis


# global variable 'col' to stores color in color plate
col = ["aqua", "red", "blue", "brown", "green"]

# global variable of dictionary to store the block number from 0-24(total 25 blocks)
# key defined number of block and values are of type list which contains [color, x-axis, y-axis, contains norder or not]
tile = {}

# these two list stores the which block is clicked and selected
tile_selected = [-1, 0]
color_plate_selected = [-1, 0]

# this dictionary stores data of color plate below 5*5 tiles
# key is number of color and value contains [color,  x-axis, y-axis]
color_plate = {0: [col[0]],
               1: [col[1]],
               2: [col[2]],
               3: [col[3]],
               4: [col[4]]}


# below block of code selects random colors from 'col' and stores in the tile dictionary
for i in range(25):
    cl = random.choice(col)
    tile[i] = list(cl.split(" "))


# below function is to draw the tiles of 60*60  size
# this function also checks weather tiles contains border or not
# this function accepts four variable (color:type string, x-axis:type iinteger, y-axis:type iinteger, border: type integer)
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


# this function gives the x and y axis to each tiles in 5*5 board
# this function also call function draw_tiles() to draw tiles
def board():
    for i in range(5):
        for j in range(5):
            tile[(i*5) + j].append(x_axis + (j*65))
            tile[(i*5) + j].append(y_axis - (i*65))
            tile[(i*5) + j].append(0)

    for i in range(25):
        draw_tiles(tile[i][0], tile[i][1], tile[i][2], tile[i][3])


# this function gives the x and y axis to each color in color plate
# this function also call function draw_tiles() to draw color plate
def plate():
    for i in range(5):
        color_plate[i].append(-240 + (i*65))
        color_plate[i].append(-185)
        color_plate[i].append(1)

    for i in range(5):
        draw_tiles(color_plate[i][0], color_plate[i][1],
                   color_plate[i][2], color_plate[i][3])


# this is logic function this function accepts the selected tiles from board and selected color from color plate
# this function checks near by tiles weather its color is same of not if its same then it calls itself recusevely
def logic(tile_selected, color_selected):
    colorr = tile[tile_selected][0]
    tile[tile_selected][0] = color_plate[color_selected][0]
    draw_tiles(tile[tile_selected][0], tile[tile_selected][1],
               tile[tile_selected][2], tile[tile_selected][3])

    if(tile_selected // 5 == 0):
        if(tile_selected % 5 == 0):
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected + 6][0] == colorr):
                logic(tile_selected+6, color_selected)
        elif(tile_selected % 5 == 4):
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected + 4][0] == colorr):
                logic(tile_selected+4, color_selected)
        else:
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected + 6][0] == colorr):
                logic(tile_selected+6, color_selected)
            if(tile[tile_selected + 4][0] == colorr):
                logic(tile_selected+4, color_selected)
    elif(tile_selected // 5 == 4):
        if(tile_selected % 5 == 0):
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected - 4][0] == colorr):
                logic(tile_selected-4, color_selected)
        elif(tile_selected % 5 == 4):
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected - 6][0] == colorr):
                logic(tile_selected-6, color_selected)
        else:
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected - 6][0] == colorr):
                logic(tile_selected-6, color_selected)
            if(tile[tile_selected - 4][0] == colorr):
                logic(tile_selected-4, color_selected)
    else:
        if(tile_selected % 5 == 0):
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected + 6][0] == colorr):
                logic(tile_selected+6, color_selected)
            if(tile[tile_selected - 4][0] == colorr):
                logic(tile_selected-4, color_selected)
        elif(tile_selected % 5 == 4):
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected - 6][0] == colorr):
                logic(tile_selected-6, color_selected)
            if(tile[tile_selected + 4][0] == colorr):
                logic(tile_selected+4, color_selected)
        else:
            if(tile[tile_selected + 1][0] == colorr):
                logic(tile_selected+1, color_selected)
            if(tile[tile_selected - 5][0] == colorr):
                logic(tile_selected-5, color_selected)
            if(tile[tile_selected - 1][0] == colorr):
                logic(tile_selected-1, color_selected)
            if(tile[tile_selected + 5][0] == colorr):
                logic(tile_selected+5, color_selected)
            if(tile[tile_selected + 6][0] == colorr):
                logic(tile_selected+6, color_selected)
            if(tile[tile_selected + 4][0] == colorr):
                logic(tile_selected+4, color_selected)
            if(tile[tile_selected - 6][0] == colorr):
                logic(tile_selected-6, color_selected)
            if(tile[tile_selected - 4][0] == colorr):
                logic(tile_selected-4, color_selected)


# this function catch the x and y axis of mouse click and checks weather it is from board tiles or from color plate
# when select tiles from board and then we select what color we want to choose from color plate
# after selecting tiles and color it calls logic() function
def catch_color(x, y):
    if((x > -220) and (x < 100) and (y < 220) and (y > -100)):
        for i in range(25):
            if((x > tile[i][1]) and (x < tile[i][1] + 60) and (y > tile[i][2]) and (y < tile[i][2] + 60)):
                tile[i][3] = 1
                tile_selected[1] = tile_selected[1] + 1
                tile_selected[0] = i

            else:
                tile[i][3] = 0

            draw_tiles(tile[i][0], tile[i][1], tile[i][2], tile[i][3])
    if((x < 80) and (x > -240) and (y > -185) and (y < -125)):
        for i in range(5):
            if((x > color_plate[i][1]) and (x < color_plate[i][1] + 60) and (y > color_plate[i][2]) and (y < color_plate[i][2] + 60)):
                color_plate_selected[1] = color_plate_selected[1] + 1
                color_plate_selected[0] = i

    if(tile_selected[1] < 2 and color_plate_selected[1] < 2):
        if tile_selected[0] != -1:
            if color_plate_selected[0] != -1:
                logic(tile_selected[0], color_plate_selected[0])
    else:
        tile_selected[1] = 0
        color_plate_selected[1] = 0


# here we called the board function and plate function to draw board and plate for first time
board()
plate()

# this enables and accepts the mouse click and calls catch_color() fuunction with passing x and y axis
turtle.onscreenclick(catch_color)

# mainloop() is used to do not close automatically screen after completion of color chnages.
turtle.mainloop()
