import json
birthday = {}


def add_choice():
    choice1 = input("Enter the name of the friend whose birthday u want to add to json")
    date = input("When is {} born in?".format(choice1))
    birthday[choice1] = date
    with open('birthday.json','r+') as k:
        json.dump(birthday,k)
    print('{} was added to my birthday list\n'.format(choice1))

def find_choice():
    choice2 = input("Enter the name of the person whose birthday u want to find")
    with open('birthday.json','r') as w:
        birthday = json.load(w)
    try:
        print(birthday[choice2])
    except:
        print("That person is not in my birthday list")


while True:
    choice = input("Please enter if u want to add or find").capitalize()
    if choice == 'Exit':
        print("Exiting")
        quit()
    if choice == 'Add':
        add_choice()
    if choice == 'Find':
        find_choice()
