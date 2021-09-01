# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

int_num = 5
float_num = float(int_num)
print (float_num, type(float_num))

float_num = 6.2
int_num = int(float_num) #Appears to floor the number, not round it
print (int_num, type(int_num))

# Don't need math libray