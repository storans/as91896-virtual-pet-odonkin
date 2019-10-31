# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Food options for pet (dictionary)
food = {"water":1, "vegetables": 2,"canned food":3}

while True:
  try:
    weight = int(input("Please enter your pet's weight: "))
    if weight > 200:
      print("This is not an available weight!")
    elif weight < 5:
      print("This is not an available weight")
    else:
      print("Awesome!")
       # Prints animals name and weight
      print("Livs's weight is {} kgs.".format(weight))
      break
  except ValueError:
    print("That was not a valid number!")

#def choose_activity()

def check_integer(question, low, high, error):
    valid = False
    while not valid:
        try:
            number = int(input("{}".format(question)))
            if low <= number <= high:
                return number
            else:
                print(error)
                print()

 # If an invalid input is made, the prompt comes up again
        except ValueError:
            print(error)

# Give the user to pick whether they want to exercise or feed their pet.
pet_activities = input("Would you like to exercise or feed your pet?: ").strip().lower()

def feed_pet(activity, weight):
    weight += food[activity]
    return weight

# This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
if pet_activities == "feed":
    print("Awesome, let's take a look in the cupboards!")
while True:
    print("1. Enter Water\n"
    "2. Enter Vegetables\n"
    "3. Enter Canned Food\n"
    "4. Exit\n")

    option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option")


    if option == 1:
        activity = "water"
    elif option == 2:
        activity = "vegetables"
    else:
        activity =  "canned food"

    weight = feed_pet(activity, weight)
    print("Your pet now weights {}".format(weight))
    if weight > 200:
        print("Your pet has had too much to eat! It has passed away!")
        break

    elif weight < 5:
        print("You pet has not had enough to eat, it has passed away!")
        break

    else:
        print("At the moment, your pet is healthy! Good Job! :)")
    break
