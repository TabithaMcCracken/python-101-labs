# Receive the following arguments from the user:
# kilometers to drive
# liters-per-kilometer usage of the car
# price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console.

print("Welcome to the Trip Cost Calculator. Please provide the following information: \n")

kilometers = float(input("Kilometers to travel: \n"))
liters_kilometer = float(input("Liters per kilometer for your vehicle: \n"))
fuel_price = float(input("Price per liter of fuel: "))

total_cost = ((liters_kilometer*kilometers)*fuel_price)
formatted_cost = "{:.2f}".format(total_cost)
print(f"${formatted_cost}")
