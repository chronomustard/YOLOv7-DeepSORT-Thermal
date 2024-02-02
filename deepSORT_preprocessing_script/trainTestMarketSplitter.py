import os
import shutil
import random

# Paths for source and destination folders
train_folder = 'reformat-combined-ir-thermal/train/'
test_folder = 'reformat-combined-ir-thermal/test/'

# Get a list of folders in the train directory
folders = [folder for folder in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, folder))]

for folder_name in folders:
    # Create the same folder in the test directory if it doesn't exist
    test_folder_path = os.path.join(test_folder, folder_name)
    os.makedirs(test_folder_path, exist_ok=True)

    # Get a list of files in the train folder for the current folder
    files = [file for file in os.listdir(os.path.join(train_folder, folder_name)) if os.path.isfile(os.path.join(train_folder, folder_name, file))]

    if files:
        # Group files by extension
        file_extension_map = {}
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension not in file_extension_map:
                file_extension_map[file_extension] = []
            file_extension_map[file_extension].append(file)

        # Choose a random extension and a random file with that extension
        if file_extension_map:
            random_extension = random.choice(list(file_extension_map.keys()))
            files_with_extension = file_extension_map[random_extension]
            random_file = random.choice(files_with_extension)

            # Define source and destination paths for the file
            source_file_path = os.path.join(train_folder, folder_name, random_file)
            dest_file_path = os.path.join(test_folder, folder_name, random_file)

            # Move the file from train to test folder
            shutil.move(source_file_path, dest_file_path)
            print(f"Moved '{random_file}' from {train_folder}{folder_name} to {test_folder}{folder_name}")
        else:
            print(f"No files with extensions found in {train_folder}{folder_name}")
    else:
        print(f"No files found in {train_folder}{folder_name}")

print("Process completed.")