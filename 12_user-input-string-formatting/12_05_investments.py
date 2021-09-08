# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

# Option 1- Shows the total at the end of the time period only
investment_amount = int(input("Investment Amount:"))
interest_rate = int(input("Interest Rate:"))
years = int(input("Number of years to invest:"))

future_value = 0
future_value = investment_amount * (1 + (interest_rate * .01))**years
print("The future value of your investment after " + str(years) + " years will be: $" + str(round(future_value,2)))

# Option 2- Shows the total at the end of each year and the grand total
investment_amount = int(input("Investment Amount: "))
interest_rate = int(input("Interest Rate: "))
years = int(input("Number of years to invest: "))

future_value = investment_amount * (1 + (interest_rate * .01))
print("$" + str(round(future_value,2)))
i = 2
while i <= years:
    future_value = future_value * (1 + (interest_rate * .01))
    print("$" + str(round(future_value,2)))
    i += 1
print("Your total after 10 years will be: $" + str(round(future_value,2)))
