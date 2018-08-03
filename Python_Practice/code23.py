f=open("prime.txt").read().split("\n")
f2=open("happy.txt").read().split("\n")

print(set(f).intersection(set(f2)))
