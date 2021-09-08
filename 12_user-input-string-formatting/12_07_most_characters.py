# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first_string = input("Please give me your first string: ")
second_string = input("Please give me your second string: ")
third_string = input("Please give me your third string: ")

longest_string = first_string
string_length = len(first_string)
# print(str(string_length) + " , " + longest_string)

if len(second_string) > len(longest_string):
    longest_string = second_string

if len(third_string) > len(longest_string):
    longest_string = third_string

print(str(len(longest_string)) + " , " + str(longest_string))