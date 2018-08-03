icount  = input("Enter the number of elements in the list")
count = int(icount)
lst = []
for i in range(count):
    x = input("Enter the element to be inserted in the list")
    ix = int(x)
    lst.append(ix)
inum = input("Enter the number to search")
num = int(inum)

def searchb(my_list,n):
    while True:

        middle_list = int(len(my_list) / 2)

        if n == my_list[middle_list]:
          return True
        elif n < my_list[middle_list]:
            my_list = my_list[:middle_list]
        elif n > my_list[middle_list]:
            my_list = my_list[middle_list+1:]
        if len(my_list) == 1:
            return False

print(searchb(lst,num))
