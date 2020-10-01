def add():
    name = input("Enter the name of contact :")
    while True:
        try:
            numb = int(input("Enter the number :"))
            break
        except:
            print("\nEnter a Valid number !!!")
            continue
    with open("data.txt", "a+") as f:  # Open a text file
        f.writelines(name + " " + str(numb) + "\n")  # write name and number in the text file.
    print("Your contact saved successfully...")


def get_cont():
    cont = {}  # A blank dictionary
    with open("data.txt", "r+") as f:
        for line in f:
            key, value = line.split()
            cont[key] = value
    name_list = list(cont.keys())
    print("Contact's list :", name_list)
    who = input("\nWhat contact you wanna know? :")
    while True:
        if who in name_list:
            print(who + "'s Number :", cont[who], "\n")  # Getting the value which is number by using key which is name
            break
        else:
            print("Contact Not Available !")
            print("Try Again...\n")
            print("Contact's list :", name_list)
            who = input("Enter a name from the given list :")


def start():
    with open("welcome.txt", 'r+') as f:
        welcome = f.read()
    print(welcome)
    ch = input("\nWhat's your choice? <1 or 2> :")
    if ch == '1':
        add()
    elif ch == '2':
        get_cont()
    else:
        print("You entered something else !")


# Here comes the main part...--->>>
while True:
    start()
    nexta = input("<Press r to run again> | <Any other key to quit> :")
    if nexta == 'r' or nexta == 'R':
        continue
    else:
        print("\nThanks for using our program.\nBye...\n")
        break
