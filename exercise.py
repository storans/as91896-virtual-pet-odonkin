# Dictionaries for pet activities
PET_ACTIVITY = {"exercise": 2, "feed": 1}

# Pets exercise options (dictionary)
exercises_dict = {"park play date": 1, "beach time": 2, "jumbo jog": 3}
exercises_list = ['park play date', 'beachtime', 'jumbo jog']


pet_weight = 1.9

# pet_weight -= exercises

def choose_activity(pet_weight):
    activity_menu = []
    activity_choice = input("Would you like to exercise or feed your pet?: ").strip().lower()
    if activity_choice == "exercise":
        print("Awesome, let's have a look at the exercises!")


# Function for showing pet weight
# Function to allow user to choose a food and feed pet said food
def user_choice_exercise(exercises_list, exercise_dict):
    initial_weight = 2
    low = 1
    high = 3
    activity_menu = []
    print("What would you like to do with your pet?:")

    number = 1
    for action in exercises:
        print("{}.  {}".format(number, exercises))
        number += 1
        activity_menu.append(exercises)

    choice = check_integer("Please choose the number with the activity you want to do with your pet.", low, high, "Please enter a number")

    chosen_exercise = activity_menu[choice - 1]

    print("You will take your pet and you guys will {}.".format(chosen_exercise.title()))

    initial_weight += exercises[chosen_exercise]
    # print(pet_activity)
    # if option == 1:
    # pet_activity = "park playdate"
    # print(pet_activity)
    # elif option == 2:
    #  activity = "beach time"
    # else:
    # activity = "jumbo jog"
    # return activity


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
# pet_activities = input("Would you like to exercise or feed your pet?: ").strip().lower()

weight = 35

# This allows the user to see the options and pick one they would like to do if they choose to exercise their pet
alive = True
while alive:

    choose_activity(weight)
    option = user_choice_exercise(exercises_dict)
    if option == 1 or option == 2 or option == 3:
        activity = choose_activity(weight)
        print(weight)
        # print("Your pet now weights {}".format(weight))
        # if weight > 200:
        # print("Your pet has not had enough exercise! It has passed away!")
        #   break

    # elif weight < 5:
    #    print("You pet has done too much exercise and not had enough to eat, it has passed away!")
    #   break

    # else:
    #  print("At the moment, your pet is healthy! Good Job! :)")

# else:
# print("Would you like to quit the game?")
