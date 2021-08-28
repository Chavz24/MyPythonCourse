"""Review Exercises 12.2"""

import pathlib

# Create a new Path object to a file called my_file.txt in a folder called
# my_folder/ in your computer’s home directory. Assign this Path object
# to the variable name file_path.

file_path = pathlib.Path.home() / pathlib.Path(r'my_folder/my_file.txt')

# Check whether or not the path assigned to file_path exists.

print(file_path.exists())

# Print the name of the path assigned to file_path. The output
# should be my_file.txt.

print(file_path.name)

# Print the name of the parent directory of the path assigned to
# file_path. The output should be my_folder.

print(file_path.parent.name)