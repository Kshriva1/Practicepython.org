icount  = input("Enter the number of elements in the list")
count = int(icount)
lst = []
for i in range(count):
    x = input("Enter the element to be inserted in the list")
    ix = int(x)
    lst.append(ix)
lst2 = []
for counter in lst:
    if counter < 5:
        lst2.append(counter)
print(lst2)

num = input("Enter a number")
inum = int(num)

lst3 = []
for count1 in lst:
    if count1 < inum:
        lst3.append(count1)
print(lst3)
