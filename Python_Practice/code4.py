inum = input("Enter the input")
num = int(inum)
lst = []
for i in range(num):
    if num % (i+1) is 0:
        lst.append(i+1)
print(lst)
