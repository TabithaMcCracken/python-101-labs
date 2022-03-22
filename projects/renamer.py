# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib
import os

desktop = pathlib.Path('/Users/tabithamccracken/Desktop')

new_path = pathlib.Path('/Users/tabithamccracken/Desktop/Newfolder')
new_path.mkdir(exist_ok=True)

# for i, filepath in enumerate(files)
for filepath in desktop.iterdir():
    if filepath.suffix == '.png':
        # new_file_name = "Screenshot" + str(i) + filepath.name # Added 
        new_file_name = "Screenshot" + filepath.name
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)

# path = '/Users/tabithamccracken/Desktop/Newfolder'
# files = os.listdir(path)

# for index,file in enumerate(files):
#    os.rename(os.path.join(path,file), os.path.join(path, ''.join(['Shot', str(index), '.png'])))

# home/desktop/file.txt
# home/desktop/folder/file.txt