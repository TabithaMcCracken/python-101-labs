# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# Get input n
# For loop comparing going through all numbers 1 to n
# 1 if statements inside for loop to compare if its divisible by 3 and 5
# 2 iflese statements inside loop to compare if its divide by 3 or 5
# Else statement inside loop to print n 

n = int(input("Please enter a number"))
final_string = ""

for num in range(1,(n+1)):
    if ((num % 3 == 0) and (num % 5 == 0)):
        final_string += "FizzBuzz"
    elif (num % 3 == 0):
        final_string += "Fizz"
    elif (num % 5 == 0):
        final_string += "Buzz"
    else:
        final_string += str(num)
print(final_string)

