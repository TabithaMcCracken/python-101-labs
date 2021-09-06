# You wake up in a maze of `if` statements and you need
# to find the path to get out:
#
# .--.--.--.  .--.--.
# |     |        |  |
# :  :--:  :  :  :  :
# |  |     |  |     |
# :  :  :  :--:--:--:
# |  |  |           |
# :  :  :--:--:--:  :
# |  |   You  |  |  |
# :  :--:--:  :  :  :
# |     |     |  |  |
# :--:  :  :--:  :  :
# |        |        |
# :--:--:--:--:--:--:
#
# However, this maze has a BIG limitation!
# There are only two actions you can take, you can only ADD
# either one of the following lines of code:
#
#     flag = True
#     flag = False
#
# You can add as many of them as you want to, but you can't change
# any of the code that is already there.
#
# Add the code so when you run it, it will print out all steps
# that you need to take in order to get out of the maze!
# You are always facing North and you can take sideways steps
# without changing the direction that you're looking.

# Directions- Left, straight 4x's, right, straight 2x's, right, straight, exit

flag = True

# True
if flag == True:
    print("left") # Goes left
# True

flag = False
# False
if flag == False:
    print("straight ahead") # Goes Straight
# False
if flag == True:
    print("left")# Doesn't execute
# False
if flag == False:
    print("straight ahead")# Goes Straight
# False
flag = True
# True
if flag == True:
    print("straight ahead") # Goes straight
#True

if flag == True:
    print("straight ahead") # Goes Straight
# True
flag = False
# False
if flag == True:
    print("DEAD END") # Doesn't Execute
#False

if flag == True:
    print("left") # Doesn't Execute
#False

if flag == False:
    print("right") # Goes Right
#False

flag = True
# True
if flag == True:
    print("straight ahead") # Goes Straight
# True

flag = False
# Flase
if flag == False:
    print("straight ahead") # Goes Straight
# False

flag = True
if flag == False:
    print("DEAD END") # Doesn't Execute
# True

if flag == True:
    print("right") #Goes Right
# True

if flag == True:
    print("straight ahead") # Goes Straight
# True

flag = False
# False
if flag == True:
    print("left") # Doesn't Execute
# False

if flag == False:
    print("EXIT!!") # Prints Exit
# False

if flag == True:
    print("DEAD END") # Doesn't Execute
