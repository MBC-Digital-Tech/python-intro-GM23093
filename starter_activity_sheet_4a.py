# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python

def square():
    color('white', 'green')
    begin_fill()
    forward (10) 
    right (45)
    forward (10) 
    right (45) 
    forward (10) 
    right (45) 
    forward (10)
    right (45)
    forward (10) 
    right (45)
    forward (10) 
    right (45) 
    forward (10) 
    right (45) 
    forward (10)
    right (45)
    end_fill()


def triangle():
    penup()
    forward(200)
    pendown()
    color('orange', 'purple')
    begin_fill()
    forward (50)
    right (120)
    forward (50)
    right (120)
    forward (50)
    end_fill()
triangle()
square()
done()