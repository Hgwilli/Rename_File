import os
from datetime import datetime

def rename_files(folder_path, name, start_number):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Sort the files by creation date
    files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    # Loop through the files and rename them
    for i, file in enumerate(files):
        # Get the file extension
        file_ext = os.path.splitext(file)[1]
        # Create the new file name
        new_name = f"{name} {start_number + i}{file_ext}"
        # Create the full path for the old and new file names
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file, new_file)

# Example usage:
folder_path = "\\path\\to\\folder"
name = "x"
start_number = 1
rename_files(folder_path, name, start_number)
