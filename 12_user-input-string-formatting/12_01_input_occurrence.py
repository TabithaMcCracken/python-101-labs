# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

input_str = input("String Input:")
input_letter = input("Letter Input:")
i = 0

for char in input_str:
    if char == input_letter:
        print("Result: " + str(i))
        break
    else:
        i += 1