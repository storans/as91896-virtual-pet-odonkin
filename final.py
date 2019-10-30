# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
exercises = {"park playdate": 0, "beach time": 0, "jumbo jog":0}
exercise_calories = {"park playdate": 0.2, "beach time": 0.3, "jumbo jog":0.4}

# Food options for pet (dictionary)
food_list = {"kibble": 3, "carrot":2, "canned food":4, "seaweed":2, "vegetables": 3, "water":1}

# Prints welcome screen
print("Welcome to Virtual Pet!")

# List for pets available in Virtual Pet
pets = ["dog", "cat",  "bunny", "turtle"]

# Prints pet list
print(pets)

# Dictionary to help code work
pets = ["dog", "cat",  "bunny", "turtle"]

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
      print("This is not am available weight")
    else:
      print("Awesome!")
       # Prints animals name and weight
      print("{}'s weight is {} kgs.".format(pet_name, weight))
      break
  except ValueError:
    print("That was not a valid number!")

# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
exercises = {"park playdate": 1, "beach time": 2, "jumbo jog":3}

end_weight = 35

def choose_activity():
    if option == 1:
        activity = "park playdate"
    elif option == 2:
        activity = "beach time"
    else:
        activity = "jumbo jog"
    return activity


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

WEIGHT = 35

# This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
if pet_activities == "exercise":
  print("Awesome, let's have a look at the exercises!")
while True:
  print("1. Enter Park Playdate\n"
  "2. Enter Beach Time\n"
  "3. Enter Jumbo Jog\n"
  "4. Exit\n")

  option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option")

  if option == 1 or option == 2 or option == 3:
    activity = choose_activity()
    print(end_weight)
    print("Your pet now weights {}".format(end_weight))
    if end_weight > 200:
      print("Your pet has not had enough exercise! It has passed away!")
      break

    elif end_weight < 5:
      print("You pet has done too much exercise and not had enough to eat, it has passed away!")
      break

    else:
        print("At the moment, your pet is healthy! Good Job! :)")

          food_list = {"kibble": 3, "canned food":4, "seaweed":2, "vegetables": 3, "water":1}

if pet_activities == "feed":
  print("Awesome, let's open the pantry!")
while True:
  print("1. Kibble\n"
  "2. Vegetables\n"
  "3. Canned Food\n"
  "4. Seaweed\n"
  "5. Vegetables\n"
  "6. Water\n"
  "7. Exit\n")

  option = check_integer("Please enter number of the choices above:", 1, 7, "This is not an option")

  if option == 1 or option == 2 or option == 3 or option == 4 or option == 5 or option == 6:
    activity = choose_food()
    print(food_weight)
    print("Your pet now weights {}".format(food_weight))
    if foood_weight > 200:
      print("Your pet has been fed too much! It has passed away!")
      break

    elif end_weight < 5:
      print("You pet has not had enough to eat, it has passed away!")
      break

    else:
        print("At the moment, your pet is healthy! Good Job! :)")



