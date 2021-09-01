# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

# I have no idea what I am supposed to do here! 

# Wrong + Wrong = Right
# False + False = True
if (((wrong and right) and (not right)) == (wrong or right)):
    print ("Yes")
else: print ("No")

print ((wrong and right)) #False
print ((not right)) #False
print ((wrong or right)) #True
