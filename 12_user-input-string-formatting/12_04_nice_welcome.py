# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

user_name = input("Please enter your name:")
first_name = ""

for char in user_name:
    if char == " ":
        break
    first_name += char
print("Welcome, " + first_name + " to my program!")