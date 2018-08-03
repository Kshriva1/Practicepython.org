import sys
if(len(sys.argv)) < 4:
    print("Usage<Value1><Value2><Value3>")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

def maxfunction(n1,n2,n3):
    if (n1 > n2) and (n1 > n3):
        print(n1,"is the largest")

    elif (n2 > n3) and (n2 > n1):
        print(n2,"is the largest")

    else:
        print(n3,"is the largest")
maxfunction(arg1,arg2,arg3)
