def quiz():
    answer_count = 0
    print("Welcome to my quiz!")
    print()
    print("Question 1")
    print("What is the capital of France?")
    answer = input()
    if answer.lower() == "paris":
        print("Correct!")
        answer_count = answer_count + 1
    else:
        print("Wrong!")
    print()

    print("Question 2")
    print("What is the chemical symbol for Hydrogen?")
    answer = input()
    if answer.lower() == "h":
        print("Correct!")
        answer_count = answer_count + 1
    else:
        print("Wrong!")
    print()

    print("Question 3")
    print("What continent is New Zealand in?")
    answer = input()
    if answer.lower() == "oceania":
        print("Correct!")
        answer_count = answer_count + 1
    else:
        print("Wrong!")
    print()

    print("Question 4")
    print("What is 4 squared?")
    answer = int(input())
    if answer == 16:
        print("Correct!")
        answer_count = answer_count + 1
    else:
        print("Wrong!")
    print()

    print("Question 5")
    print("Who sang the song 'Runaway Baby'?")
    answer = input()
    if answer.lower() == "bruno mars":
        print("Correct!")
        answer_count = answer_count + 1
    else:
        print("Wrong!")
    print()

    print("That's all the questions!")
    print(f"Your score was {answer_count}/5")
quiz()