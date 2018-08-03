icount  = input("Enter the number of elements in the list")
count = int(icount)
lst = []
for i in range(count):
    x = input("Enter the element to be inserted in the list")
    ix = int(x)
    lst.append(ix)

def firstandlast(x):
    return([x[0],x[len(x)-1])

lst1 = firstandlast(lst)
print(lst)
       
