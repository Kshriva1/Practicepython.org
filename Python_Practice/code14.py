icount  = input("Enter the number of elements in the list")
count = int(icount)
def setadd(iilist):
    print(list(set(iilist)))
def listmaker(x):
    lst = []
    for i in range(x):
        x = input("Enter the element to be inserted in the list")
        ix = int(x)
        lst.append(ix)
    return lst
ilist = listmaker(count)
setadd(ilist)
