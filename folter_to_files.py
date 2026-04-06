import os 
import shutil
#%%

def folder_to_files():
    source_path = input("Enter the source path: ")
    target_path = input("Enter the target path: ")
    dirs = os.listdir(source_path)
    for dir in dirs:
        dir_path = os.path.join(source_path, dir)
        files = os.listdir(dir_path)
        files_path = [os.path.join(dir_path, file) for file in files]
        for file_path in files_path:
            target_file_path = os.path.join(target_path, os.path.basename(file_path))
            shutil.move(file_path, target_file_path)
    return


if __name__ == "__main__":
    folder_to_files()
        