# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

input_string = input("String Input: ")
input_symbol = input("Symbol Input:")
first_letter = input_string[0]
final_string = ""

for char in input_string:
    if char == first_letter:
        final_string += input_symbol
    else:
        final_string += char

print(final_string)
