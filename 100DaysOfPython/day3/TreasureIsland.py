
if __name__ == "__main__":
    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
    print("Welcome to Treasure Island.")
    print("Your mission is ot find the treasure.")
    option1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
    
    if option1 == "left":
        option1a = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()

        if option1a == "wait":
            option1b = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()

            if option1b == "red":
                print("It's a room full of fire. Game Over.")
            elif option1b == "blue":
                print("Inside the room is an open crate with gold coins spilling over the sides. Congratulations you found the Treasure!")
            elif option1b == "yellow":
                print("The room had a trap floor. Game Over.")
            else:
                print("Invalid option please try again.")
        elif option1a == "swim":
            print("While swimming to the island, you were attack by the lake monster. Better luck next time!")
        else:
            print("Invalid option please try again.")           
    elif option1 == "right":
        option2a = input("You find a gas station in the middle of nowhere. Type \"help\" to ask for directions. Type \"continue\" to continue walking down the road.\n").lower()

        if option2a == "help":
            print("The clerk tells the police about a pirate, and you get busted. Game Over.")
        elif option2a == "continue":
            print("You continue walking down the road never finding any hints of the hidden treasure. You realize this was the wrong path and give up. Game Over.")
        else:
            print("Invalid option please try again.")    
    else:
        print("Invalid option please try again.")    