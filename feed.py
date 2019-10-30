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
