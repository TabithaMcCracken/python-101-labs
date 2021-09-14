# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

word = "TIGER"
word = word.upper() #not needed if we are defining the word above
final_word = "_" * len(word)
tries = 6
correct_guess = False
guessed_letters = []
guessed_words = []

print("Hi! Welcome to Hangman! \n") # Print an explanation to the user
print(f"You have this many tries left: {tries} \n")
print(f"Here is the hangman board: \n{final_word}") # Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input

while not correct_guess and tries>0:
    guess = input("What is your letter guess? ").upper()
    if len(guess) == 1 and guess.isalpha(): #input must be 1 letter
        if guess in guessed_letters: #they have already guessed that letter
            print(f"You have already guessed this letter: {guess}") 
        elif guess not in word: #the guess is not in the word
            print(f"{guess} is not in the word")
            tries -= 1 #takes away a try
            print(f"You have this many tries left: {tries}")
            guessed_letters.append(guess) #adds letter to the list of guessed letters
        else: #the guess is in the word
            print(f"Excellent, {guess} is in the word")
            guessed_letters.append(guess)
            word_as_list = list(final_word) #changes word into a list to index it
            indices = [i for i, letter in enumerate(word) if letter == guess] #find indices where guess occurs
            for index in indices: #replaces each underscore with guess
                word_as_list[index] = guess
            final_word = "".join(word_as_list)
            
            if "_" not in final_word: #checks to see if they've guessed all the letters
                correct_guess = True    
    else:
        print("This is not a valid guess, pleae try again and enter 1 letter.")
    print(final_word)
if correct_guess:
    print("Yay! You have guessed the word!")
else:
    print("Sorry, you ran out of tries and did not guess the word!")