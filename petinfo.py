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
    print("That was not a valid weight or number, please enter a weight between 5 and 200!")
