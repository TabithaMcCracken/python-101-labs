# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
flag = False

# Reverse the string
reverse_string = ""
index = len(filename)
while index>0:
    reverse_string += filename[index-1]
    index = index -1
print(reverse_string)

# First attempt
# Compare first 4 characters
file_type = "fdp."

if reverse_string[0] == file_type[0] and reverse_string[1] == file_type[1] and reverse_string[2] == file_type[2] and reverse_string[3] == file_type[3]:
    print("This is a pdf")
else:
    print("This is not a pdf")

# Second Attempt- doesn't work
# Can't get 'string index our of range' error fixed, is related to what happens when the length of the strings is different
counter = 0
index=0
while index < 3:
    for char in reverse_string:
        if reverse_string[counter] == file_type[counter]: 
            counter += 1
            print(counter)
        else:
            break
    index += 1

if counter == 4:
    print("This is a pdf file")
else:
    print("This is not a pdf")



# Another Attempt
final_string = ""
for char in filename[:-5:-1]: # This a string slice
    if char == "f":
        final_string += char
    if char == "d":
        final_string += char
    if char == "p":
        final_string += char
    if char == ".":
        final_string += char

if final_string == "fdp.":
    print("This is a pdf")
else:
    print("This is not a pdf")

