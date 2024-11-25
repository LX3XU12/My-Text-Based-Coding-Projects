import random

def easy():
    #EASY
    word_list = ["six", "ten", "cat", "dog", "sun", "sky", "car", "bed", "fun", "eat", "run", "try"]
    word = random.choice(word_list)
    guesses = 0

    while True:
        guessed = input('Please guess a 3-letter word: ').lower()
        guesses += 1

        if guessed == word:
            print("Well Done! You Got It Right!")
            print(f"You took {guesses} guesses")
            break
        else:
            print("Sadly, wrong.")

#END OF EASY

def mid():
    #MID
    word_list = ["apple", "grape", "lemon", "focus", "bread", "finch", "peach", "mango", "berry", "water", "melon", "coconut", "dragon"]
    word = random.choice(word_list)
    guesses = 0

    while True:
        guessed = input('Please guess a 5-letter word: ').lower()
        guesses += 1

        if guessed == word:
            print("Well Done! You Got It Right!")
            print(f"You took {guesses} guesses")
            break
        else:
            print("Sadly, wrong.")

#END OF MID

def hard():
    #HARD
    word_list = ["include", "between", "because", "through", "country", "however", "picture"]
    word = random.choice(word_list)
    guesses = 0

    while True:
        guessed = input('Please guess a 7-letter word: ').lower()
        guesses += 1

        if guessed == word:
            print("Well Done! You Got It Right!")
            print(f"You took {guesses} guesses")
            break
        else:
            print("Sadly, wrong.")

#END OF HARD

gamemode = input("Please select your gamemode, easier, middle or harder: ").lower()

if gamemode == "easier":
    easy()
elif gamemode == "middle":
    mid()
elif gamemode == "harder":
    hard()
else:
    print("Invalid gamemode.")
