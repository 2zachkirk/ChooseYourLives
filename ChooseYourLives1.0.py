# Programmer: Zach Kirk
# Date: 3.15.24
# Program: Choose Your Lives

from time import sleep

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
sleep(2.5)
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
sleep(2.5)
# Cave Scenario
if health > 0:
    print("\nYou continue walking with a health level of", health)
    print("You see a cave in the distance. Do you want to enter?")
    sleep(2.5)
    cave_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No: ")
    if cave_choice == "y":
        print("As you enter the cave, you see a bear attacking a woman.")
        sleep(5)
        print("You decide to intervene and defeated the bear and a kiss from the woman.")
        # Logic for the bear fight goes here
    else:
        print("You chose not to enter the cave.")
        sleep(2.5)
        print("As you turn to leave, the bear comes out and attacks you.")
        # Logic for the bear attack goes here
else:
    sleep(2.5)
    print("Sorry, you did not escape the Dark forest!")

sleep(2.5)
# Road Scenario
if health > 0:
    print("\nYou continue walking with a health of", health)
    sleep(5)
    print("You then see a road in the distance, with a very nice car with nobody near it.")
    print("However, there is a cop nearby and a volvo semi coming in your direction.")
    Road_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No:")
    if Road_choice == "y":
      print("You cross the road, barely missed the truck, get near the car and find the keys lying on the ground.")
    sleep(2.5)
    print("Do you pick up the keys?")
    sleep(2.5)
    Keys_choice = input_yes_or_no("Type 'Y' for Yes or 'N' for No:")
    if Keys_choice == "y":
      print("You grab the keys, get in the car, and drive off after escaping the cop.")
    sleep(2.5)
    print("The car turned out to be just a car that was forgotten, the cop was there for another reason not involving the car, therefore it is now yours.")
    sleep(5)
    print("We are so close for escaping, Then we can ride off into the sunset; and off to the Bahamas we go!")
    sleep(5)
    print("Oh! Look, I know that we should probally escape, but how about a quick stop at the lake?")
    sleep(3.5)
# Lake Decision
    Lake_Choice = input_yes_or_no("Type 'y' for yes or 'n' for No:")
    if Lake_Choice == "y":
        print("You said to me sure, and we are now on our way to the lake where something unexpected is waiting.")
        sleep(2.5)
        print("We then arrive at the lake, where I begin to take pictures of fish underwater.")
        sleep(2.5)
        print("I then take a photo of a truck and said we are good to go now, when suddenly...")
        sleep(2.5)
        print("ROAR!")
        sleep(2.5)
        print("What the---!")
        sleep(2.5)
        print("An angry crocodile crosses our path and it's enormous and with bad attitude!")
        sleep(2.5)
        print("Most likely has family issues.")
        sleep(2.5)
        print("ROAR!")
        sleep(2.5)
        print("The crocodile begins chewing up our car and its tires, we now cant go anywhere!")
        sleep(2.5)
        print("We could go out an fight the gator, but we will probally be killed.")
        sleep(2.5)
        print("Or, we can make a run for it; but that may not end well either.")
        sleep(2.5)
        print("What should we do?!")
        sleep(5)
# Crocodile Issues
    Crocodile_Choice = input_yes_or_no("Type 'y' for yes or 'n' for No:")
    if Crocodile_Choice == "y":
        print("What?! Are you crazy?! Attacking a rogue alligator?")
        sleep(2.5)
        print("Well, I mean I got something crocodiles really hate, Crocodile Spray!")
        sleep(2.5)
        print("Lets spritz this man!")
        sleep(7)
        print("The crocodile calls on a few of its mates and they are closing in!")
        sleep(2.5)
        print("I spray the crocodile spray, the gators are in love with the spray!")
        sleep(2.5)
        print("UGH! This stuff smells like feet!")
        sleep(2.5)

        print("You: Look!")
        sleep(2.5)
        print("The gators are bowing to you and me....")
        sleep(2.5)
        print("What the heck is happening?")
        sleep(2.5)
        print("The gators are apparently now our servants!")
        sleep(2.5)
        print("The gators lead us out of the forest and we are SAFE AT LAST!")
        sleep(10)
        print("We arrive safely back on home, where the gators are warming up to our house quick and began being our butlers.")
        sleep(2.5)
        print("So our story is over, we are safe but....")
        sleep(5)
        print("Where's the root beer? There was like seven bottles!")
        sleep(2.5)
        print("A gator walks by balancing a root beer on its nose and flips it in the air and drinks it.")
        sleep(2.5)
        print("bruh, It just goes to show you: Never hire gators that gorge root beer.")
        print("Epilouge")
        sleep(10)
        print("Crocodiles all get together while we are asleep, then to surprise one speaks!")
        print("Fellow Crocodile brothers, the time has come!")
        print("No more will we be murdered and disrespected and no more will we be ridiculed!")
        print("All the gators cheer.")
        sleep(5)
        print("Prepare to say goodbye to you lives humans and LONG LIVE THE GATORS!")
        print("The gators cheer and roar.")
        print("HAHAHAHAHAHA!!!!!! ROAR!!!")

    print("To be continued?")
    sleep(5)
    print("Gator: Get me some root beer will ya, and you have seen nothing! ROAR!")


print("The END?")


if Crocodile_Choice == 'n':
    print("You have decided to RUN!")
    sleep(10)
    print("The Crocs on our tail!")
    sleep(5)
    print("You pass by a stand where they are selling weapons and tazers, we could use one to "
          "zap the crocodile!")
    sleep(2.5)
    print("The problem is it's five hundred dollars, and you only got 400.")
    sleep(2.5)
    print("500 dollars?! That's HIGHWAY ROBBERY!")
    sleep(2.5)
    print("We gotta find a way to earn extra money, cause this salesman doesn't know prices and "
          "is better off his head in the trash!")
    sleep(2.5)
    print("ROAR!")
    sleep(2.5)
    print("And avoid Mr.Green Scales.")



# Tazer Descision

    print("Oh look!, there's a man selling tazers for twenty dollars!, lets buy some!")
    sleep(2.5)
    print("You think its rather suspicious that a man is only selling tazers for twenty dollars...")
    sleep(2.5)
    print("What should we do? Because Scales is closing in fast!")
    sleep(2.5)
    print("Should we buy the tazer from a man or try to beat that gator senseless with our hands?")
    sleep(5)
Tazer_choice = input_yes_or_no("Type 'y' for yes or 'n' for No:")
if Tazer_choice == 'y':
    sleep(5)
    print("You have decided to buy the twenty dollar tazer. Let's go!")
    sleep(5)
    print("We are walking over to the man and as we do, he spoke with a mischievous austrailian accent.")
    sleep(2.5)
    print("G'Day mates!, Are you tired of having your daily salesmen treating you like trash?")
    print("yes.")
    print("You tired of salesmen scamming you every chance they get?")
    print("yea...")
    sleep(2.5)
    print("Then come on down to my shop and buy some stuff!, Jake's Weapons Corner; right around the"
          "corner!")
    sleep(2.5)
    print("Okay!")
    sleep(10)
    print("We arrive at the so called: Jake's Weapons corner...")
    sleep(5)
    print("Well hello again mates!, welcome to my shop!")
    print("We got tazers that shock, we got darts to make your enemies drop, and we got swords and "
          "guns galore!")
    print("What's your kids' desire?")
    print("We want to buy a tazer gun to zap a crocodile chasing us!")
    print("To tazer a croc?, yea those scaly things are quite the pests.")
    print("That'll be one hundred dollars!")
    sleep(10)
    print("What? I thought it was only twenty dollars?")
    print("That mate was just for a 5 second sale that I was having....")
    sleep(10)
    print("But how are...")
    print("Oh!, look at that! The one hundred dollar event is over, they are now two hundred dollars!")
    print("UGGHHHHH!")
    print("Just pay this man bro.")
    print("Pleasure doing business with ya mate! Happy hunting!")
    print("Ok.....")
    sleep(10)
    print("Oh the event for two hundred dollars is over, now they are one penny for 10 seconds!")
    print("People crowd the shop as we walk out.")
    print("We hear the man counting down from ten.")
    sleep(10)
    print("Ten, Nine, eight, seven, six...")
    print("NOW THEY ARE TWO THOUSAND DOLLARS, ALL SALES MADE ARE FINAL!!!!!")
    print("Crowd gets angry and goes after him with the weapons they grabbed.")
    print("Let's get out of here and zap that gator!")
    sleep(5)
    print("ROAR!")
    sleep(5)
    print("YIPE!")
    sleep(2.5)
    print("The people look at the gator and scream and run off, including Mr.Scammy the salesman.")
    print("IS IT JUST ME, OR DID THIS GUY GET BIGGER?!")
    sleep(5)
    print("ROAR!")
    print("Ok, focus.. IM TERRIFIED!!!!")
    sleep(5)
    print("Ok (Deep breath)")
    sleep(10)
    print("You go and kick that gator's butt or we are done for!")
    print("G'day mates, ill help ya!")
    print("Where did you come from?")
    print("The closet.")
    print("oh.... kayyy...")
    sleep(10)
    print("Why you helping us?")
    print("I have a score to settle with Professor Scrummy Scales!")
    print("Scrummy scales? What kind of a name is Scrummy Scales?")
    print("And what did he do?")
    sleep(10)
    print("All will be revealed....")
    sleep(10)
    print("In the next part of this game!")
    print("OOOOOHHHHHHHHHHHHHHHH!!!!!!!!")

    sleep(10)
    print("ROAR!")
    print("To be continued...")

if Keys_choice == "n":
    print("You chose not to grab the keys, then suddenly; there is a thunderstorm and you get struck by lightning.")

if Road_choice == "n":
    print("You decide not to cross to get to the car, then the bear shows up for revenge and attacks you.")
    print("You got attacked by a bear and lost", decrease_health_minor,"health. Your health is now", health)


