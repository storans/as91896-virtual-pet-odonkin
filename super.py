# Check if your person is eligible for superannuation

# Age is a constant because it's not changed in the program
SUPER_AGE = 65

# Loop to allow testing of different values
keep_going = ""

while keep_going == "":
    age = int(input("What is your age?: "))

# Must be greater than or equal to catch 65 year olds.
    if age >= SUPER_AGE:
        print("You can get super! :)")
    else:
        print("No super for you, come back later.")

    keep_going = input("Continue? Press enter or q")
