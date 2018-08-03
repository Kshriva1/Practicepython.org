gameBoard = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def displayboard(gameBoard):
    i=0
    for item in gameBoard:
        print(gameBoard[i])
        i += 1

def check(gameBoard):
    lst = []
    for item in gameBoard:
        for value in item:
            lst.append(value)
        return all(lst)

def update(listl,str):
    global gameBoard
    gameBoard[listl[0]][listl[1]] = str
    displayboard(gameBoard)


def getcoord(player):
    global gameBoard
    num = input("Enter the coordinates for your choice")
    choice = num.split(",")
    values = [int(x) for x in choice]
    game = [x-1 for x in values]
    if type(gameBoard[game[0]][game[1]]) is str:
        print("Sorry that choice has already been taken")
        alternate = getcoord(player)
        return alternate
    return game


while True:
    print("Welcome to tic tac toe")
    ply1 = 'x'
    ply2 = 'o'
    player1 = 'player1'
    player2 = 'player2'
    update(getcoord(player1),ply1)
    if check(gameBoard) is True:
        break

    update(getcoord(player2),ply2)
    if check(gameBoard) is True:
        break

print("Game over no valid moves left for you")
