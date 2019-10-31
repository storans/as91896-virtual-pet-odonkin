# Dictionary to help code work
pets = ["dog", "cat",  "bunny", "turtle"]

# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
exercises = {"park playdate": 1, "beach time": 2, "jumbo jog":3}

# Food options for pet (dictionary)
food_list = {"water":1, "vegetables": 2,"canned food":3}


# Prints welcome screen
print("Welcome to Virtual Pet!")

# Prints pet list
print(pets)

# This allows the user to input what animal they would like as their virtual pet
virtual_pet = input("Please choose an animal off the list to be your virtual pet: ").strip().lower()

# This tells the user when the pet they have entered is okay in the program and part of the pet list.
if virtual_pet in pets:
  print("Congratulations! You have chosen a {} as a Virtual Pet!".format(virtual_pet))

 # This tells the user the animal they have chosen is not allowed in the program as it is not in the list and allows them to pick again.
else:
  print("Sorry, {} is not an option in this Virtual Pet game today :) Try another from our list!".format(virtual_pet))
  virtual_pet = input("Please choose an animal off the list to be your virtual pet: ").strip().lower()

# This allows the user to input a name to personalise their animal.
pet_name = input("Please choose a name for your {}: ".format(virtual_pet).strip().title())

# Show the user their animal and name
print("Awesome! You now own a {} named {}! ".format(virtual_pet, pet_name))

#Allows user to make sure they are entering a number with digits not with letters
# Creates loop if it does not fit the criteria
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
      print("{}'s weight is {} kgs.".format(pet_name, weight))
      break
  except ValueError:
    print("That was not a valid weight or number, please enter a weight between 5 and 200!")


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
pet_activities = input("Would you like to exercise or feed {}?: ".format(pet_name)).strip().lower()

def exercise_pet(activity, weight):
    weight -= exercises[activity]
    return weight

# This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
if exercises == "exercise":
    print("Awesome, let's have a look at the exercises!")
while True:
    print("1. Enter Park Playdate\n"
    "2. Enter Beach Time\n"
    "3. Enter Jumbo Jog\n"
    "4. Exit\n")

    option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option")


    if option == 1:
        activity = "park playdate"
    elif option == 2:
        activity = "beach time"
    elif option ==3:
        activity = "jumbo jog"
    elif option == 4:
        print("You have chosen to quit game! Thank you playing :)")
    else:
        print("This is not an option. Please choose another number.")

    weight = exercise_pet(activity, weight)
    print("{} now weights {}".format(pet_name, weight))
    if weight > 200:
        print("Your pet has not had enough exercise! It has passed away!")
        print("Thank you for playing, rerun program to start again.")
        break

    elif weight < 5:
        print("{} has done too much exercise and not had enough to eat, they has passed away!".format(pet_name))
        print("Thank you for playing, rerun program to start again.")
        break

    else:
        print("At the moment, {} is healthy! Good Job! :)".format(pet_name))
    break


