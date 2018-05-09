#List of known users
known_users = ["Alice", "Jim", "Kelsey", "George", "Harry", "Bill", "Patrick", "Lenny"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize() #strip whitespace and capitalizes user input's first letter

    if name in known_users:
        print("Hello {}!".format(name)) #{} takes user's input
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name) #"remove" built in function removes from list. "del" function can look into as well, gets more specific
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Haven't met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around.")
            #how to stop asking questions?
           
