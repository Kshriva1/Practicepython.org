dic = dict()

dic['Raj'] = '01/17/2018'
dic['Sam'] = '02/14/2018'
dic['pam'] = '03/01/1995'

key = input("Enter the person whose birthday u want")

for i in dic.keys():
    if i == key:
        print(dic[i])
