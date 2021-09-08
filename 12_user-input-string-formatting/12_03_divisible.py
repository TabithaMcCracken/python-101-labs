# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

num = int(input("Please enter a number between 1 and 1,000,000,000:"))

if num in range(1 , 1000000000): 
    if num % 3 == 0:
        print("This number is divisible by 3")
    else:
        print("This number is not divisible by 3")
else:
    print("This number is not between 1 and 1,000,000,000")
