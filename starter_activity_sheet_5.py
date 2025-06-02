from turtle import *

## Task 1: Look at the following code and decide which picture it will generate.
# Then download it from the shared drive, then save and run it, to check.

def demo():
  pencolor("blue")
  for counter in range (100):
    forward (150)
    right(95)

def single(col):
  fillcolor(col)
  begin_fill()
  circle(50,120)
  left(60)
  circle(50,120)
  end_fill()

def flower():
  for i in range(10):
    if i % 2 == 0:
      single("red")
    elif i == 5:
      right(30)
      i=i-1
    else:
      single("yellow")

def triangle():
  for i in range(3):
    forward(100)
    right(120)

def trishape():
  for i in range(8):
    right(45)
    triangle()

trishape()