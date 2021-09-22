# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.


# Directions say to 'compile a list', does this just mean print or make an actual list?

# Get tools
import pathlib

# Find the path to my desktop
desktop = pathlib.Path('/Users/tabithamccracken/Desktop')

# Create new list
file_list = [] 

for filepath in desktop.iterdir(): # Loop through each file
    if filepath.suffix == '.jpg': # Filter files with .jpg
        file_list.append(str(filepath.name)) #Add to file list

print(file_list) # Print the file list




