inum = int(input("Enter the dimensions of the game board"))

for i in range(inum):
    for i in range(inum):
        print("---",end=" ")
    print("\n")
    for i in range(inum+1):
        print("|  ",end="")
    print("\n")
for i in range(inum):
    print("---",end = " ")

print("\n")
