from sys import exit

def food_room():
    print("There is a room full of food and drink.")
    print("But the door which you get in is disappear,and then there appear two door in front of you.")
    print("1.first room.")
    print("2.second room.")
    print("3.eat and wait.")

    choice = input("> ")

    if choice == "first room":
       print("You can see nothing,because it's very dark inside.")
       print("Suddenly a strong light appear and you blind,then a snake came and bite you.")
       dead

    elif choice == "second room":
       print("You see a bear and want to run, but you failed.")
       dead

    elif choice == "eat and wait":
    print("After 1min later, a sword appeared,and you picked it up, then you get into {another_room}.")    

def another_room():
    print("1.There is a dragon is sleeping.")
    print("2.walk away.")
    print("3.kill the dragon when it sleeping")
    print("4.communication with the dragon")

    choice == input(">")

    if choice == "walk away":
    print("The dragon is still sleeping,but you can't find a door to get out.")
    dead("The dragon wake up and eat you.")

    elif choice == "kill the dragon when it sleeping":
    print("You suucceed and the you kill the dragon.")
    print("You are alive.")

    elif choice == "communication with the dragon":
    print("The dragon can't understand you and eat you.")
    dead