import requests

# URL = URL = f"https://uzby.com/api.php?min={name_len}&max={name_len}"


def get_user_name():
    name_len = 0
    while not (name_len >=2 and name_len <=40):
        user_name = str(input("Please enter your name: \n"))
        name_len = len(user_name)
    return user_name

def get_user_name_len(user_name): # Tested
    """Get the users name and return the length of their name."""
    name_len = len(user_name)

    return name_len

def make_url_for_getting_a_random_name(length): # Tested
    """Make a url with the length of the users name"""
    url = "https://uzby.com/api.php?min=" + str(length) + "&max=" + str(length)
    print(f"You're url is: {url}")
    
    return url

def get_user_game_name(url): # Tested
    """Get a new random name that is the same length of the users name."""
    response = requests.get(url)
    new_name = response.text
    print(f"You're game name is: {new_name}")

    return new_name

def choose_a_door():
    door_choice = str(input(
        "You are in a dark hallway, there are 2 doors in front of you. Would you like to go through the left door or the right door? \n"))
    door_choice = door_choice.lower()
    if "left" in door_choice or "right" in door_choice:
        print(f"You have selected the {door_choice} door.")
    return door_choice

def room_with_sword():
        global sword
        global end_game
        enter_empty = str(
            input("The room appears to be empty. \nWould you like to enter it? \n"))
        enter_empty = enter_empty.lower()
        if "yes" in enter_empty and sword == False:  # enters the room and doesn't have the sword
            get_sword = str(input(
                "You have decided to enter the room. As you look around you see a sword. \nWould you like to take it? \n"))
            get_sword = get_sword.lower()
            if "yes" in get_sword:  # gets the sword
                sword = True
                print(sword)
                print("You've got the sword! You head back out of the room.")
            if "no" in get_sword:  # doesn't get the sword
                print("You didn't take the sword.")
        else:  # enters the room, but already has the sword
            print(
                "You have decided to enter the room. The room is empty, so you leave the room.")

def room_with_dragon():
    global sword
    global end_game
    enter_right = str(input(
            "There is a large dragon in the room. Would you like to enter the room? \n"))
    enter_right = enter_right.lower()

    if "yes" in enter_right:
        fight_dragon = str(input(
            "You have entered the room with the dragon. Would you like to fight the dragon? \n"))
        fight_dragon = fight_dragon.lower()

        if "yes" in fight_dragon:  # player must fight the dragon to end the game
            end_game = True  # breaks the while loop
            if sword == True:  # allows them to win if they have the sword
                print(
                    f"You had the sword, fought the dragon, and won! Congratulations!")
            else:  # allows them to loose since they don't have the sword
                print(
                    f"I'm sorry! You didn't have any weapons and were eaten by the dragon! You loose!")
        if "no" in fight_dragon:  # if the player chooses not to fight the dragon
            print("You have left the room.")

    if "no" in enter_right:
        end_game = False

if __name__ == "__main__":
    # Setup
    sword = False
    end_game = False
    user_name = get_user_name()
    # len_of_user_name = get_user_name_len(user_name)
    # naming_url = make_url_for_getting_a_random_name(len_of_user_name)
    # user_game_name = get_user_game_name(naming_url)

    print(f"Welcome, {user_name}! In this game, your new name will be: {user_name}")
    print("Enjoy the game, we hope you make it out alive! \n")


    # Play the game
    while end_game == False:
        door_choice = choose_a_door()
        if "left" in door_choice:
            room_with_sword()

        elif "right" in door_choice:
            room_with_dragon()

        else:
            # if user doesn't put left or right as an answer
            print("Please answer with 'left' or 'right'")




    # End the game

