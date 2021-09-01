# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

## (f-32)* (5/9) = C

Fahrenheit = int(input ("What is the temperature in Fahrenheit?"))
Celsius = (Fahrenheit - 32) * (5/9)
print ("That temperature in Celsius is:", Celsius)
