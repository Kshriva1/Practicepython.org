inum1 = input("Enter the number of elements in 1st list: ")
num1 = int(inum1)

inum2 = input("Enter the number of elements in the 2nd list: ")
num2 = int(inum2)
lst1 = list()
lst2 = list()
for i in range(num1):
    ix = input("Enter the element in the 1st list")
    x = int(ix)
    lst1.append(x)

for i in range(num2):
    iy = input("Enter the element in the 2st list")
    y = int(iy)
    lst2.append(y)
lst3 = list()
for k in lst1:
    for n in lst2:
        if n == k:
            lst3.append(n)
print(list(set(lst3)))
