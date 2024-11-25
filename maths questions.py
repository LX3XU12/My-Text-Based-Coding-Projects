import random

def question():
    question1 = random.randint(1, 10)
    question2 = random.randint(1, 10)
    correct_answer = question1 * question2

    while True:
        try:
            answer = int(input(f"What is {question1} times {question2}? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if answer == correct_answer:
            print("You are correct!")
            question()
            break
        else:
            print("Sorry, but wrong. Try again.")
            question()

# Start the game
question()