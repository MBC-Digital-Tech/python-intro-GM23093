# starter program lesson 1

# change to your name.
user_name = input("What's your name? ")
print(f"Hello {user_name}! ")
print("We want to know a bit about you!")
print()

# asking user 2 questions
breakfast = input("What did you have for breakfast today? ")
colour = input("What is your favourite colour? ")
print()

# print sentences to questions
print(f"You had {breakfast} for breakfast today.")
print(f"Your favourite colour is {colour}.")
print()

# combine the next 2 lines into one command
print("Lastly...")
answer = input(f"Do you like programming {user_name}? ")

# change to an f string
print(f"Great! You said {answer}!")

print("Let's learn some Python today.")


