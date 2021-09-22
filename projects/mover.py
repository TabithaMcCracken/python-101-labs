# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/Users/tabithamccracken/Desktop")

# Create a new folder
new_path = pathlib.Path('/Users/tabithamccracken/newscreenshots')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
    if filepath.suffix == '.png': # Filter for screenshots only
        new_filepath = new_path.joinpath(filepath.name) # Create a new path for each file
        filepath.replace(new_filepath) # Move the screenshot there
