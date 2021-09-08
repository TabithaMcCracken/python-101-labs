# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_num = int(input("Please enter a number between 0 and 1,000,000,000 : "))
i = 1

while i < 1000000000:
    if i == user_num:
        break
    i += 1

print(i)
