"""this code concerns Q4 and Q5 of the assignment. The solutions were implemented by Taha Naveed, Syed Ibrahim, Shuja Ahmad & Omar Kasab"""

import turtle 


ROWS = 10 
COLUMNS = 10 
PIXEL_SIZE = 30
#user_inputs = [] ##this array takes in user string inputs corresponding to color values 

### SOME GLOBAL VARIABLES HAVE BEEN KEPT CONSTANT, others have been reduced. Initialize and draw pixel modules have been imported ### 


def initialise():
    '''Initializes the turtle by defining the pen color, fill color, speed, and position
    Parameters: None
    Returns: None'''
    turtle.up()
    turtle.pencolor("black")
    turtle.speed(0)
    turtle.fillcolor("white")
    turtle.goto(-300,300)


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







def string_to_colors(): 
    '''THIS FUNCTION IMPLEMENTS A ROW OF COLORS ACCORDING TO THE USER'S REQUEST. THE FUNCTION WILL TERMINATE IF IT DETECTS AN ANOMALOUS INPUT 
    OR IF THE ARRAY INDEX HAS BEEN LEFT EMPTY DUE TO THE USER NOT ENTERING ANYTHING'''
    user_inputs = [] 
    for i in range(20):
        next_pixel = str(input("Enter Hex value for next pixel: "))
        user_inputs.append(next_pixel)
    ##THIS PART OF THE FUNCTION FILLS AN ARRAY WITH THE USERS REQUESTED COLORS###

    count = 0 
    while (count <= 19):
        new_pixel = user_inputs[count]
        if new_pixel == "0":
            draw_pixel("black")
            count = count + 1 
        elif new_pixel == "1":
            draw_pixel("white")
            count = count + 1 
        elif new_pixel == "2":
            draw_pixel("red")
            count = count + 1 
        elif new_pixel == "3":
            draw_pixel("yellow")
            count = count + 1 
        elif new_pixel == "4":
            draw_pixel("orange")
            count = count + 1 
        elif new_pixel == "5":
            draw_pixel("green")
            count = count + 1 
        elif new_pixel == "6":
            draw_pixel("yellowgreen")
            count = count + 1 

        elif new_pixel == "7":
            draw_pixel("sienna")
            count = count + 1 
        elif new_pixel == "8":
            draw_pixel("tan")
            count = count + 1 
        elif new_pixel == "9":
            draw_pixel("gray")
            count = count + 1 
        elif new_pixel == "A":
            draw_pixel("darkgray")
            count = count + 1 
        else:
            return False 
            break



def make_drawing():
    for i in range(20):

        string_to_colors()
        turtle.goto(-300, turtle.ycor()-PIXEL_SIZE)
        turtle.setheading(0)
        print("NOW YOU WILL ENTER VALUES FOR NEXT ROW: ")
        print("")
    turtle.exitonclick
        
        
def main():

    initialise()
    make_drawing()
    input("Enter something to exit")

main()