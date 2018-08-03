def draw_board(game):
    for i in range(3):
        print(" ---" * 3)
        a = list()
        for j in range(3):
            a.append("| "+game[i][j])
        a.append("|")
        print(" ".join(a))
    print(" ---" * 3)


def checktic(game):
    a = 0

    for i in range(3):
        row = set([game[i][0], game[i][1], game[i][2]])
        if len(row) == 1 and game[i][0] != " ":
            a = game[i][0]

    for i in range(3):
        column = set([game[0][i], game[1][i], game[2][i]])
        if len(column) == 1 and game[0][i] != " ":
            a = game[0][i]

    diag1 = set([game[0][0], game[1][1], game[2][2]])
    diag2 = set([game[0][2], game[1][1], game[2][0]])

    if len(diag1) == 1 or len(diag2) == 1 and game[1][1] != " ":
        a = game[1][1]

    if a == 'X':
        print("Player 1 wins")
        return True
    elif a == 'o':
        print("Player 2 wins")
        return True
    elif not any(" " in i for i in game):
        return True
    else:
        return False



def check(lst,game):
    for i in lst:
        if not 4>i>0:
            return True
        if game[lst[0]-1][lst[1]-1] != ' ':
            return True
        return False




def turn(ply):
    choice = input("player %s please give me your coordinates"%ply).split(",")
    choice = [int(i) for i in choice]

    while check(choice,game):
        print("U have entered the wrong choice. try Again")
        choice = input("Player %d give me the coordinates: \n"%ply).split(",")
        choice = [int(i) for i in choice]

        if ply == 1:
            game[choice[0]][choice[1]] == 'X'
        elif ply == 2:
            game[choice[0]][choice[1]] == 'o'
        draw_board(game)



game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
draw_board(game)
t = 1

while True:
    turn(t)
    if checktic(game) :
        break
    else:
        if t == 1:
            t = 2
        else:
            t =1
