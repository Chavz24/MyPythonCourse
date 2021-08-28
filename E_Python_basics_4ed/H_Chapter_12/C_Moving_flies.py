"""Challenge: Move All Image Files To a New Directory 12.4"""

from pathlib import Path

# Create a new folder in the Practice Files folder called images/ and move
# all image files to that folder.

files_path = Path('Path_to_folder')
destination_folder = files_path / 'images'
destination_folder.mkdir(exist_ok=True, parents=True)

for path in files_path.rglob('*.???'):
    if path.name.endswith(('.png', '.gif', '.jpg')):
        print(path.name)
        source = path
        destination = destination_folder / path.name
        source.replace(destination)
    else:
        continue
