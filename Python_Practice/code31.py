print("Lets play hangman")
word = 'EVAPORATE'
guessed = "_" * 9
lstword = list(word)
lstguessed = list(guessed)
lstl = list()
guess = input("Guess the alphabet")
while True:
    if guess.upper() in lstl:
        print("Incorrect choice")

    elif guess.upper() in lstword:
        index = lstword.index(guess.upper())
        lstguessed[index] = guess.upper()
        lstword[index] = '_'

    elif guess.upper() not in lstword:
        lstl.append(guess.upper())


    if '_' not in lstguessed:
        print("You won")
        break
    guess = input("Guess the alphabet again")
