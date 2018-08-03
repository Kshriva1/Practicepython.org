import json
from collections import Counter
birthday = {}
month = []


def add_choice():
    choice1 = input("Enter the name of the friend whose birthday u want to add to json")
    date = input("When is {} born in?".format(choice1))
    birthday[choice1] = date
    with open('birthday.json','r+') as k:
        json.dump(birthday,k)
    print('{} was added to my birthday list\n'.format(choice1))

def find_choice():
    
    with open('birthday.json','r') as w:
        birthday = json.load(w)
    for x in birthday.values():
        month.append(x.split('/')[1])
    print(Counter(month))


while True:
    choice = input("Please enter if u want to add or find").capitalize()
    if choice == 'Exit':
        print("Exiting")
        quit()
    if choice == 'Add':
        add_choice()
    if choice == 'Find':
        find_choice()
