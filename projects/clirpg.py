# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

player_name = str(input("Please enter your name: \n"))
print(
    f"Welcome, {player_name}! Enjoy the game, we hope you make it out alive! \n")


end_game = False
sword = False

while end_game == False:
    # Present them with a choice between two doors.
    door_choice = str(input(
        "You are in a dark hallway, there are 2 doors in front of you. Would you like to go through the left door or the right door? \n"))
    door_choice = door_choice.lower()
    if "left" in door_choice or "right" in door_choice:
        print(f"You have selected the {door_choice} door.")

    if "left" in door_choice:  # If they choose the left door, they'll see an empty room.
        enter_empty = str(
            input("The room appears to be empty. \nWould you like to enter it? \n"))
        enter_empty = enter_empty.lower()
        if "yes" in enter_empty and sword == False:  # enters the room and doesn't have the sword
            get_sword = str(input(
                "You have decided to enter the room. As you look around you see a sword. \nWould you like to take it? \n"))
            get_sword = get_sword.lower()
            if "yes" in get_sword:  # gets the sword
                sword = True
                print("You've got the sword! You head back out of the room.")
            if "no" in get_sword:  # doesn't get the sword
                print("You didn't take the sword.")
        else:  # enters the room, but already has the sword
            print(
                "You have decided to enter the room. The room is empty, so you leave the room.")

    # If they choose the right door, then they encounter a dragon.
    elif "right" in door_choice:
        enter_right = str(input(
            "There is a large dragon in the room. Would you like to enter the room? \n"))
        enter_right = enter_right.lower()
        if "yes" in enter_right:
            fight_dragon = str(input(
                "You have entered the room with the dragon. Would like to fight the dragon? \n"))
            fight_dragon = fight_dragon.lower()
            if "yes" in fight_dragon:  # player must fight the dragon to end the game
                end_game = True  # breaks the while loop
                if sword == True:  # allows them to win if they have the sword
                    print(
                        f"You had the sword, fought the dragon, and won! Congratulations {player_name}!")
                else:  # allows them to loose since they don't have the sword
                    print(
                        f"I'm sorry {player_name}! You didn't have any weapons and were eaten by the dragon! You loose!")
            if "no" in fight_dragon:  # if the player chooses not to fight the dragon
                print("You have left the room.")
        if "no" in enter_right:
            end_game = False
    else:
        # if user doesn't put left or right as an answer
        print("Please answer with 'left' or 'right'")
