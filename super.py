SUPER_AGE = 65

keep_going = ""

while keep_going == "":
    age = int(input("What is your age?: "))
    if age >= SUPER_AGE:
        print("You can get super! :)")
    else:
        print("No super for you, come back later.")

    keep_going = input("Continue? Press enter or q")
