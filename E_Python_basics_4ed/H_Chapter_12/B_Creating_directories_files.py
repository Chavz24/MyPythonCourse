"""Review Exercises 12.3"""

import pathlib, shutil

# Create a new directory in your home folder called my_folder/.

new_dir = pathlib.Path.home() / 'my_folder'
# new_dir.mkdir(exist_ok=True, parents=True)

#  Inside my_folder/ create three files. file1.txt, file2.txt, image1.png

# files = ['file1.txt', 'file2.txt', 'image1.png']
#
# for file in files:
#     file_path = new_dir / file
#     file_path.touch(exist_ok=True)

# Move the file image1.png to a new directory called images/ inside of
# the my_folder/ directory

source = new_dir / 'image3.png'
images_folder = new_dir / 'images'
images_folder.mkdir(exist_ok=True, parents=True)
destination = images_folder / 'image3.png'
# source.replace(destination)

#  Delete the file file1.txt

file_path = new_dir / 'file1.txt'
# file_path.unlink(missing_ok=True)   # only in python 3.8 and above.

#  Delete the my_folder/ directory.

print(new_dir)
shutil.rmtree(new_dir)
