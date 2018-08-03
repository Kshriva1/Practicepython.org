print("Guess a number 0 to 100")

count = 0
min = 0
max = 50
ans = ""
while ans != 'same':
    mid = (max-min)//2
    ans = input("My guess is %s. Is that high, low or same? "%(mid))
    count += 1

    if ans == 'high':
        max = mid
    elif ans == 'low':
        min = mid
    elif ans == 'same':
        print("Congrats u guessed it in: ",count,'attempts')
