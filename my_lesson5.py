from turtle import*

def triangle(length):
    for counter in range(3):
        forward(length)
        right(120)

def main():
    length = int(input("Length? "))
    triangle(length)
    done()

def shape():
    length = int(input("Length? "))
    sides = int(input("How many sides? "))
    for i in range(sides):
        forward(length)
        left(360/sides)
    done()

shape()
