import random
with open("sowpods.txt",'r') as f:
    lst = f.readlines()
print("Lets play hangman")
word = random.choice(lst).strip()
guessed = "_" * len(word)
lstword = list(word)
lstguessed = list(guessed)
lstl = list()
chances = 6
guess = input("Guess the alphabet")
while True:

    if guess.upper() in lstl:
        print("Incorrect choice choose again")


    elif guess.upper() in lstword:
        index = lstword.index(guess.upper())
        lstguessed[index] = guess.upper()
        lstword[index] = '_'

    elif guess.upper() not in lstword:
        lstl.append(guess.upper())
        chances = chances-1
        if chances < 1:
            print("You Lose")
            quit()


    if '_' not in lstguessed:
        print("You won")
        break
    guess = input("Guess the alphabet again")
