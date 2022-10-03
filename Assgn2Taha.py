"""This code is a solution to Q1,2,3 in the assignment. The solution was implemented by Taha Naveed, Syed Ibrahim, Shuja Ahmad and Omar Kasab"""

# importing the turtle module
import turtle

# Defining global variables
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def initialise():
    '''Initializes the turtle by defining the pen color, fill color, speed, and position
    Parameters: None
    Returns: None'''
    turtle.up()
    turtle.pencolor("black")
    turtle.speed(0)
    turtle.fillcolor("white")
    turtle.goto(-300,300)
    turtle.tracer(False)
def draw_pixel(pixel_colour):
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor(pixel_colour)
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)

def draw_black_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_white_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_red_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_yellow_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_orange_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()


def draw_green_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_yellowgreen_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("yellowgreen")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_sienna_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("sienna")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_tan_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("tan")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_gray_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

def draw_darkgray_pixel():
    '''This funciton draws a pixel and fills the given color
    Parameters: pixel color
    Returns: None'''
    count = 0
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    turtle.down()
    while count != 4:
        turtle.fd(PIXEL_SIZE)
        turtle.rt(90)
        count = count + 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(PIXEL_SIZE)
    turtle.exitonclick()

###complete for all of these function colors, green has been done as an example##


def draw_grid():
    '''This function draws the whole grid 
    Parameters: None
    Returns: None'''
    for x in range(ROWS):
        for y in range(COLUMNS):
            draw_pixel("white")
        turtle.goto(-300, turtle.ycor()-PIXEL_SIZE)
        turtle.setheading(0)

def pixart_move(rows_across, column_down):
    '''This function moves the pointer to the given coordination
    Parameters: Row index and column index
    Returns: None'''
    turtle.goto(turtle.xcor() + (PIXEL_SIZE*rows_across), turtle.ycor() - (PIXEL_SIZE*column_down))

def draw_row(rows_across, column_down, row_length):
    '''This function draws a row with colour at a given postion
    Parameters:
    Row index, column index and length of the row
    Retunrs:
    None'''
    pixart_move(rows_across, column_down)
    for x in range(row_length):
        draw_pixel("red")

def draw_checkers():
    '''This function draws a checkers board
    Parameters: None
    Returns: None'''
    color = "black"
    for x in range(ROWS):
        for y in range(COLUMNS):
            if (x+y)%2 == 0:
                color = "black"
            else:
                color = "red"
            draw_pixel(color)
        turtle.goto(-300, turtle.ycor()-PIXEL_SIZE)
        turtle.setheading(0)
        

def main():
    '''This function calls the other functions'''
    initialise()
    draw_checkers()
   # turtle.exitonclick()
    #draw_green_pixel()
    input("stop: ")
    
if __name__ == '__main__':
    main()