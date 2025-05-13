# starter program week 2 - perhaps this could be a task

def conversation():
    print("Welcome to my conversation program")
    print()

    # ask user how many cities are in england
    answer = int(input("How many cities in England? "))

    # change this so that the user can enter YES as well.
    while answer != 51:
        print('WRONG!')
        answer = int(input('How many cities are in England? '))
    print('CORRECT')

    # prints "goodbye" before ending the function
    print("Goodbye")
conversation()
# Add command here to run the function

