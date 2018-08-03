fstring = input("Enter a long string: ")
lst = fstring.split()
def inreverse(flist):
    flist.reverse()
    return flist

llst = inreverse(lst)
result = " ".join(llst)
print(result)
