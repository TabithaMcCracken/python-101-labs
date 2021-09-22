# from emoji import emojize
# print (emojize(":thumbs_up:"))

# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/Users/tabithamccracken/Desktop")

# Create a new folder
new_path = pathlib.Path('/Users/tabithamccracken/Desktop/screenshot')
new_path.mkdir(exist_ok = True)

for filepath in desktop.iterdir():
    if filepath.suffix == ".png":
        print(filepath.name)


# .suffix returns file extensions
# .is_dir() checks if the path is a directory
# .parent returns the parent of each file
# .stem returns the final path component
