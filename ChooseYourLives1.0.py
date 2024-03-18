# Programmer: Zach Kirk
# Date: 3.15.24
# Program: Choose Your Lives

print("Our mission is to escape the Dark forest!")
print("One wrong turn and.....")

print("Your mission is to escape the Dark Woods!")
print("One wrong turn and you'll be stuck in the Dark Woods forever!")

health = 15
decrease_health_major = 5
decrease_health_minor = 3
increase_health_major = 5
increase_health_minor = 3

def input_yes_or_no(prompt):
    while True:
        choice = input(prompt).lower()
        if choice == "y" or choice == "n":
            return choice
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

# Apple Tree Scenario
print("\nYou have just started strolling in the woods with a health level of", health)
print("You come across an apple tree. Do you want to eat an apple from the tree?")
apple_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No: ")
if apple_choice == "y":
    health -= decrease_health_minor
    print("You ate a toxic apple and lost", decrease_health_minor, "health. Your health is now", health)
else:
    print("You chose not to eat the apple. Your health remains at", health)

# Fork Scenario
if health > 0:
    print("\nYou continue walking near a river with a health level of", health)
    print("You find a river. Do you want to drink water from it?")
    water_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No: ")
    if water_choice == "y":
        health += increase_health_minor
        print("You drank water and gained", increase_health_minor, "health. Your health is now", health)
    else:
        health -= decrease_health_minor
        print("You chose not to drink the water and lost", decrease_health_minor, "health. Your health is now", health)
else:
    print("Sorry, you did not escape the Dark Woods!")

# Cave Scenario
if health > 0:
    print("\nYou continue walking with a health level of", health)
    print("You see a cave in the distance. Do you want to enter?")
    cave_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No: ")
    if cave_choice == "y":
        print("As you enter the cave, you see a bear attacking a woman.")
        print("You decide to intervene.")
        # Logic for the bear fight goes here
    else:
        print("You chose not to enter the cave.")
        print("As you turn to leave, the bear comes out and attacks you.")
        # Logic for the bear attack goes here
else:
    print("Sorry, you did not escape the Dark Woods!")





