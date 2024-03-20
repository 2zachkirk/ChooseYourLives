# Programmer: Zach Kirk
# Date: 3.15.24
# Program: Choose Your Lives

print("Our mission is to escape the Dark forest!")
print("One wrong turn and.....")
print("We should get out of here!")

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
    print("Sorry, you did not escape the Dark forest!")

# Cave Scenario
if health > 0:
    print("\nYou continue walking with a health level of", health)
    print("You see a cave in the distance. Do you want to enter?")
    cave_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No: ")
    if cave_choice == "y":
        print("As you enter the cave, you see a bear attacking a woman.")
        print("You decide to intervene and defeated the bear and a kiss from the woman.")
        # Logic for the bear fight goes here
    else:
        print("You chose not to enter the cave.")
        print("As you turn to leave, the bear comes out and attacks you.")
        # Logic for the bear attack goes here
else:
    print("Sorry, you did not escape the Dark forest!")


# Road Scenario
if health > 0:
    print("\nYou continue walking with a health of", health)
    print("You then see a road in the distance, with a very nice car with nobody near it.")
    print("However, there is a cop nearby and a volvo semi coming in your direction.")
    Road_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No:")
    if Road_choice == "y":
      print("You cross the road, barely missed the truck, get near the car and find the keys lying on the ground.")
      print("Do you pick up the keys?")
    Keys_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No:")
    if Keys_choice == "y":
      print("You grab the keys, get in the car, and drive off after escaping the cop.")
      print("The car turned out to be just a car that was forgotten, the cop was there for another reason not involving the car, therefore it is now yours.")

    print("We are so close for escaping, Then we can ride off into the sunset; and off to the Bahamas we go!")
    print("I know that we should probally escape, but how about a quick stop at the lake?")
# Lake Decision
    Lake_Choice = input_yes_or_no("Type 'y' for yes or 'n' for No:")
    if Lake_Choice == "y":
        print("You said to me sure, and we are now on our way to the lake where something unexpected is waiting.")

        print("We then arrive at the lake, where I begin to take pictures of fish underwater.")

        print("I then take a photo of a truck and said we are good to go now, when suddenly...")

        print("ROAR!")
        print("What the---!")
        print("An angry crocodile crosses our path and it's enormous and with bad attitude!")
        print("Most likely has family issues.")
        print("ROAR!")
        print("The crocodile begins chewing up our car and its tires, we now cant go anywhere!")
        print("We could go out an fight the gator, but we will probally be killed.")
        print("Or, we can make a run for it; but that may not end well either.")
        print("What should we do?!")
# Crocodile Issues
    Crocodile_Choice = input_yes_or_no("Type 'y' for yes or 'n' for No:")
    if Crocodile_Choice == "y":
        print("What?! Are you crazy?! Attacking a rogue alligator?")
        print("Well, I mean I got something crocodiles really hate, Crocodile Spray!")
        print("Lets spritz this man!")
        print("The crocodile calls on a few of its mates and they are closing in!")
        print("I spray the crocodile spray, the gators are in love with the spray!")
        print("UGH! This stuff smells like feet!")

        print("You: Look!")

        print("The gators are bowing to you and me....")
        print("What the heck is happening?")

        print("The gators are apparently now our servants!")

        print("The gators lead us out of the forest and we are SAFE AT LAST!")

        print("We arrive safely back on home, where the gators are warming up to our house quick and began being our butlers.")

        print("So our story is over, we are safe but....")

        print("Where's the root beer? There was like seven bottles!")

        print("A gator walks by balancing a root beer on its nose and flips it in the air and drinks it.")

        print("bruh, It just goes to show you: Never hire gators that love root beer.")

print("The END.")





if Keys_choice == "n":
      print("You chose not to grab the keys, then suddenly; there is a thunderstorm and you get struck by lightning.")

if Road_choice == "n":
    print("You decide not to cross to get to the car, then the bear shows up for revenge and attacks you.")
    print("You got attacked by a bear and lost", decrease_health_minor,"health. Your health is now", health)
else: print("Sorry, you did not escape the Dark forest!")

