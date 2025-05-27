## What would you expect the computer to do? Write the output exactly as you think it will appear.

def starter():
  number = 0
  while number <= 5:
    print ("Hello")
    number = number + 1
  print ("Goodbye")

def monday():
  counter = 0
  while counter < 100:
    print("Today is Monday")
    counter = counter + 1

def storm():
  answer = input("What is the name of the recent storm? ")
  while answer.lower() != 'doris':
    print("WRONG!")
    answer = input("Try again: ")
  print("CORRECT!")

def ninetynine():
  answer = int(input("Enter a number: "))
  while answer != 99:
    answer = int(input("Enter a number: "))
  print("Thank you - 99 was the number I was looking for!")

def bored():
  bored = input("Are you bored? ")
  while bored.lower() != 'n':
    bored = input("Are you bored? ")
  print("Got to you in the end!")

def excersize5():
  list = 1
  while list <= 10:
    print(list)
    list = list + 1

def excersize6():
  list = 10
  while list >= 1:
    print(list)
    list = list - 1

def logging_in():
  count = 0
  password = input("What is the correct password? ")
  while password.lower() != "secret":
    count = count + 1
    print("INCORRECT!")
    password = input("Try again: ")
  print("That's the correct password!")

def question():
  number = int(input("How many cities are in England? "))
  while number != 51:
    print("INCORRECT!")
    number = int(input("Try again: "))
  print("CORRECT!")