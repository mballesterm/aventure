# work on your adventure game below!
import random

print("""
Find the Dragon Egg
===================

Your quest starts.
""")

room = "The Closet"
light = False
transport = False
place = False


while room != "cat":
        choose_1 = input(f"You are now in {room} where the Magic beginns.Suddenly, while trying to figure out what the hell happened yesterday, you realize that there is a Golden Hamster telling you to approach him.The Golden Hamster sneaks through a slot in the closet.Do you want to follow him, get out of the closet or stay in the Closet? F/O/S ").lower()
        while choose_1 not in ["f","o","s"]:
            choose_1 = input("that is not an option, try again!")
        if choose_1 == "f":
            choose_1 = input("You shrink to the size of a Hamster and when you come out of the closet you are on a beach.next to the hamster that has turned into a lion. The lion tells you that you need to find the dragon's egg, to have 3 wishes. The egg is in a Cave Where do you want to go?").lower()
            room = "beach"
            while choose_1 not in["cave" , "to the cave"]:
                choose_1 = input("You wont find the egg there, try another place").lower()
            if choose_1 == "cave" or "to the cave":
                place = True    
        elif choose_1 == "o":
             room = "Kitchen"
        elif choose_1 == "s":
            print("You wake up after an hour and go to the Kitchen for some watter")
            room ="Kitchen"
        if room == "Kitchen":
            choose_1 = input("in the kitchen you find a newspaper on the table that says 'Dragon's eggs wanted, millionaire's sum to be paid'. After reading the Berliner Zeitung you think that waking up in a closet believing you have talked to a Hamster isn't a good life and that you wish you were a millionaire.Then you remember that you have met some dragon experts on your trip to Brazil. So you decide to go to the airport to catch the next flight. There is flights for Paris, London and Brazil. Where do you want to go?")
            while choose_1 not in ["London","Brazil","Paris"]:
                 choose_1 = input("there is not flight to that place, choose london, paris or brazil")
            cities ={"London":"You had an english breakfast. Nothinmg about the Egg", "Brazil":"The right choice", "Paris":"you fall in love, but you dont believe in love and there is also nothing about the Egg here, try other city"}
            while choose_1 != "Brazil":
                if choose_1 == "London":
                 choose_1 = input(cities["London"])
                elif choose_1 =="Paris":
                 choose_1 = input(cities["Paris"])
            if choose_1 =="Brazil":
                print(cities["Brazil"])
                room = "Caipi"
        if room =="Caipi":
            choose_1 = input("You arrive Brizil and Meet the dragon experts. They tell you about a Beach, and the Mith of finding Dragon's Eggs on a cave. Where do you want to go?")
            while choose_1 not in ["cave" , "to the cave"]:
                choose_1 = input("There you wont find the eggs!! Try again").lower()
            if choose_1 == "cave" or "to the cave":
                place = True
        if place == True:
            choose_1 = input('You arrive to the Cave and noticed you need a flashlight from the Store but the Store is 5 Km away. You see a bike on the floor. You want to take the bike? Yes/No').lower()
            while choose_1 not in ["yes","no"]:
                choose_1 = input("that is not a valid option").lower()
            if choose_1 == "yes":
                transport = True
                choose_1 = input("You take the bike, go to the Store and get the Flashlight.You were fast! Where do you want to go?").lower()
                light = True
                while choose_1 not in ["cave" , "to the cave"]:
                    choose_1 = input("you wont find the egg there. Try again").lower()
                if choose_1 =="cave" or "to the cave":
                    print("Now you arrive the Cave and you can see")
            elif choose_1 =="no":
                choose_1 = input("You walk many hours until you get to the Store and buy the Flashlight. Where do you wanna go now?").lower()
                light = True
                transport= True
                while choose_1 not in ["cave" , "to the cave"]:
                    choose_1 = input (" you dont have so many energie better walk back")
                if choose_1 == "cave" or "to the cave":
                    print("after many hours you finilly make it to the cave")
        if place and transport and light:
            choose_1 = input ("As you move forward into the Cave you found a Door that contains the followin message 'You can only pass if you solve the Riddle: What goes up and down but never moves?' Resolve the Riddle to open the Door").lower()
            if choose_1 == "stairs" or "the stairs":
                room = "cat"
            while choose_1 not in ["the stairs" , "stairs"]:
                choose_1 = input("try again loser!") .lower()    
if room == "cat":                  
 print("Yes you got it!when the door opens, you see a cat. It says to you: Congratulations you made it! follow the pad and you will find what you are looking for")


 print("""
 
On a hidden clearing you discover the dragon egg.


Your quest has been successful!
""")

