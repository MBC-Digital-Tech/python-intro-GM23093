# activity 6a

def conversation ():
    print()
    print('Welcome to my conversation program')
    print()

    bball = input('Do you watch basketball? Answer yes or no. ')
    if bball.lower() == 'yes':
        print()
        print('No way! I do too!')
        team = input("What's your favourite team? Answer team last name i.e. 'Lakers'. ")

        if team.lower() == 'wizards':
            print('Same. Go Wizards!')
        else:
            print("That's cool. I prefer the wizards.")       
    else:
        print()
        sport = input("Oh, what sport do you enjoy? ")
        print()
        print(f"{sport.title()} is a cool sport too.")
    print()
    print("That's all I have to talk about today. Goodbye!")

conversation()