# week 4 Loops

from turtle import *

def square():
    for counter in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)

def triangle():
    for counter in range(1):
        forward(200)
        right(135)
        forward(141.42)
        right(90)
        forward(141.42)
def envelope():
    triangle()
    right(135)
    square()

envelope()
done()
