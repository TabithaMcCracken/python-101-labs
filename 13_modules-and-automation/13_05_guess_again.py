# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
num = random.randint(1,10)
guess = None
tries = 6

while tries > 0 and guess != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations! You won!")
        break
    else:
        tries -= 1
        if tries > 0:
            print("Nope, sorry! Try Again!")
            print(f"You have {tries} tries left.")
        else:
            print("Sorry, you loose!") 