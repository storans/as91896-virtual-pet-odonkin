# Function to check whether the choice is an option in feed and exercise
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

# Equation for exercise to minus calories from weight
def exercise_pet(activity, weight):
    weight -= EXERCISES[activity]
    return weight

# Equation for feeding to add calories from weight
def feed_pet(activity, weight):
    weight += FOOD[activity]
    return weight


# Dictionary to help code work
PETS = ["dog", "cat",  "bunny", "turtle"]

# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
EXERCISES = {"park playdate": 1, "beach time": 2, "jumbo jog":3}

# Food options for pet (dictionary)
FOOD = {"water":1, "vegetables": 2,"canned food":3}

# Prints welcome screen
print("Welcome to Virtual Pet!")

# Prints pet list
print(PETS)

# This allows the user to input what animal they would like as their virtual pet
virtual_pet = input("Please choose an animal off the list to be your virtual pet: ").strip().lower()

# This tells the user when the pet they have entered is okay in the program and part of the pet list.
if virtual_pet in PETS:
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
    if weight > 30:
      print("This is not an available weight!")
    elif weight < 2:
      print("This is not an available weight")
    else:
      print("Awesome!")
       # Prints animals name and weight
      print("{}'s weight is {} kgs.".format(pet_name, weight))
      break
  except ValueError:
    print("That was not a valid weight or number, please enter a weight between 2 and 30!")

# This is the start of the main routine.
if __name__ == "__main__":
    # First is a variable set to True to check whether the program should continue running.
    tracking_on = True
    while tracking_on == True:
        # Start an infinite loop to prompt for a correct option value
        while True:
        # Create an option variable to store the user's chosen option.

# Give the user to pick whether they want to exercise or feed their pet.
            pet_activities = input("Would you like to exercise or feed your pet?: ").strip().lower()

            # This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
            if pet_activities == "exercise":
                    print("Awesome, let's have a look at the exercises!")
                    print("1. Enter Park Playdate (Pet loses 1kg)\n"
                    "2. Enter Beach Time (Pet loses 2kg)\n"
                    "3. Enter Jumbo Jog (Pet loses 3kg)\n"
                    "4. Exit\n")

                    option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option, please try another from the list above and type in numbers!")

                    if option == 1:
                        activity = "park playdate"
                    elif option == 2:
                        activity = "beach time"
                    elif option ==3:
                        activity = "jumbo jog"
                    else:
                        print("{} ended up being a {}kg {}! {} will miss you! ".format(pet_name, weight, virtual_pet, pet_name))
                        print("You have chosen to quit game! Thank you playing :)")
                        tracking_on = False
                        break

                    weight = exercise_pet(activity, weight)
                    print("Your pet now weights {}kgs".format(weight))
                    if weight > 30:
                        print("Your pet has not had enough exercise! It has passed away!")
                        print("Thank you for playing, rerun program to start again.")

                    elif weight < 2:
                        print("You pet has done too much exercise and not had enough to eat, it has passed away!")
                        print("Thank you for playing, rerun program to start again.")

                    else:
                        print("At the moment, your pet is healthy! Good Job! :)")

            # This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
            elif pet_activities == "feed":
                    print("Awesome, let's take a look in the cupboards!")
                    print("1. Enter Water (Pet gains 1kg)\n"
                    "2. Enter Vegetables (Pet gains 2kg)\n"
                    "3. Enter Canned Food (Pet gains 3kg)\n"
                    "4. Exit\n")

                    option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option, please try another from the list above and type in numbers!")


                    if option == 1:
                        activity = "water"
                    elif option == 2:
                        activity = "vegetables"
                    elif option ==3:
                        activity = "canned food"
                    else:
                        print("{} ended up being a {}kg {}! {} will miss you! ".format(pet_name, weight, virtual_pet, pet_name))
                        print("You have chosen to quit game! Thank you playing :)")
                        tracking_on = False
                        break

                    weight = feed_pet(activity, weight)
                    print("Your pet now weights {}kgs".format(weight))
                    if weight > 30:
                        print("Your pet has had too much to eat! It has passed away!")
                        print("Thank you for playing, rerun program to start again.")

                    elif weight < 2:
                        print("You pet has not had enough to eat, it has passed away!")
                        print("Thank you for playing, rerun program to start again.")

                    else:
                        print("At the moment, your pet is healthy! Good Job! :)")

