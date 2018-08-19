from sys import exit

def food_room():
    print("There is a room full of food and drink.")
    print("But the door which you get in is disappear,and then there appear two door in front of you.")
    print("1.first room.")
    print("2.second room.")
    print("3.eat and wait.")

    choice = input("> ")

    if "1" in choice:
       print("You can see nothing,because it's very dark inside.")
       print("Suddenly a strong light appear and you blind,then a snake came and bite you.")
       dead

    elif "2" in choice:
         print("You see a bear and want to run, but you failed.")
         dead

    elif "3" in choice:
         print("After 1min later, a sword appeared,and you picked it up.")    
         another_room()

def another_room():
    print("There is a dragon is sleeping.")
    print("1.walk away.")
    print("2.kill the dragon when it sleeping")
    print("3.communication with the dragon")

    action = input("> ")

    if "1" in action:
       print("The dragon is still sleeping,but you can't find a door to get out.")
       dead("The dragon wake up and eat you.")

    elif "2" in action:
         print("You suucceed and the you kill the dragon.")
         print("You are alive.")

    elif "3" in action:
         print("The dragon can't understand you and eat you.")
         dead("Eat by dragon.")

def start():
    print("You are get into a dark room.")
    print("But the door disappeared,and there appear a room.")
    print("You can choose get in or do not get in.")

    choice = input("> ")

    if choice == "get in":
        food_room()
    elif choice == "do not get in":
        dead("Because of hungry.")


def dead(why):
    print(why,"well down!")
    exit(0)

start()    