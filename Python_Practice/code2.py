

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))
def check2(x):
    if x % 4 == 0:
        print(x, "is a multiple of 4")
    elif x % 2 == 0:
        print(x, "is an even number")
    else:
        print(x, "is an odd number")
check2(num)
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)

inum = input("Enter a number")

num2 = int(inum)
