# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
exercises = {"park playdate": 1, "beach time": 2, "jumbo jog": 3}


# pet_weight = 35

#pet_weight -= exercises

def choose_activity(pet_weight):
    activity_menu = []
    activity_choice = input("Would you like to exercise or feed your pet?: ").strip().lower()
    if activity_choice == "exercise":
        print("Awesome, let's have a look at the exercises!")

        print("1. Enter Park Playdate\n"
              "2. Enter Beach Time\n"
              "3. Enter Jumbo Jog\n"
              "4. Exit\n")

        option = check_integer("Please enter number of the choices above:", 1, 4, "This is not an option")

        pet_activity = activity_menu[option - 1]

        #if option == 1:
           # pet_activity = "park playdate"
            #print(pet_activity)
       # elif option == 2:
          #  activity = "beach time"
        #else:
           # activity = "jumbo jog"
        #return activity


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
#pet_activities = input("Would you like to exercise or feed your pet?: ").strip().lower()

weight = 35

# This allows the user to see the options and pick one they would like to do if they choose to exercise their pet

while True:

    choose_activity(weight)
    #if option == 1 or option == 2 or option == 3:
        #activity = choose_activity(weight)
       # print(weight)
       # print("Your pet now weights {}".format(weight))
       # if weight > 200:
         #   print("Your pet has not had enough exercise! It has passed away!")
         #   break
3
       # elif weight < 5:
        #    print("You pet has done too much exercise and not had enough to eat, it has passed away!")
         #   break

       # else:
          #  print("At the moment, your pet is healthy! Good Job! :)")

#else:
    #print("Would you like to quit the game?")
