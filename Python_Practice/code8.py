user1 = input("choose rock,paper or scissor: ")
user2 = input("choose rock,paper or scissor: ")


def compare(u1,u2):
    if u1 == 'rock':
        if u2 == 'scissor':
            print("user1 won")
        elif u2 == 'rock':
            print("Tied")
        else:
            print("user2 won")
    if u1 == 'scissor':
        if u2 == 'paper':
            print("user1 won")
        elif u2 == 'scissor':
            print("Tied")
        else:
            print("user2 won")
    if u1 == 'paper':
        if u2 == 'rock':
            print("user1 won")
        elif u2 == 'paper':
            print("Tied")
        else:
            print("user2 won")
compare(user1,user2)
