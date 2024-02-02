from PIL import Image
import os
import shutil

PATH_1 = r'C:\Kuliah\skripsi\RegDB-Thermal\train_market'
PATH_2 = r'C:\Kuliah\skripsi\RegDB-Thermal\train_market'
PATH_3 = r'C:\Kuliah\skripsi\deep_sort_pytorch\deep_sort\deep\reformat-combined-ir-thermal\train'

def convert_resize_images(src, dest):
    for root, _, files in os.walk(src):
        relative_path = os.path.relpath(root, src)
        dest_folder = os.path.join(dest, relative_path)

        for file_name in files:
            if file_name.endswith('.jpg'): # Check the format of source file!
                src_file = os.path.join(root, file_name)
                dest_file = os.path.join(dest_folder, os.path.splitext(file_name)[0] + '.bmp') # Check the format of target file!
                os.makedirs(dest_folder, exist_ok=True)

                # Open and resize the image
                img = Image.open(src_file)
                img = img.resize((64, 128))  # Resize to 64x128
                img.save(dest_file, 'BMP')  # Save as target format

def delete_empty_files():
    for root, _, files in os.walk(PATH_3):
        for file_name in files:
            if file_name == ".empty":
                os.remove(os.path.join(root, file_name))

def create_folders_structure():
    for root, _, _ in os.walk(PATH_1):
        relative_path = os.path.relpath(root, PATH_1)
        folder_path_3 = os.path.join(PATH_3, relative_path)
        os.makedirs(folder_path_3, exist_ok=True)

def reformat_folders():
    create_folders_structure()
    folder_list_2 = [folder for folder in os.listdir(PATH_2) if os.path.isdir(os.path.join(PATH_2, folder))]
    folder_list_3 = [folder for folder in os.listdir(PATH_3) if os.path.isdir(os.path.join(PATH_3, folder)) and int(folder) >= 802]
    
    
    for idx, folder in enumerate(folder_list_3):
        print("Copying ",folder_list_2[idx], " to ", folder_list_3[idx])
        if idx < len(folder_list_2):
            folder_path_2 = os.path.join(PATH_2, folder_list_2[idx])
            folder_path_3 = os.path.join(PATH_3, folder)
            convert_resize_images(folder_path_2, folder_path_3)
        else:
            folder_path_3 = os.path.join(PATH_3, folder)
            # Empty the folder if insufficient folders in PATH_2
            for root, dirs, files in os.walk(folder_path_3):
                for file in files:
                    os.remove(os.path.join(root, file))

    delete_empty_files()

def main():
    reformat_folders()

if __name__ == "__main__":
    main()