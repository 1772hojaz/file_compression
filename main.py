#!/usr/bin/python3
import tarfile
import os
import datetime
import shutil


# Extract the tar file
def select_folder():
    folder = input("Enter the folder name: ")
    if os.path.exists(folder):
        print("Folder exists")
    else:
        print("Folder does not exist")
        folder = select_folder()
    return folder

def compress(folder):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_filename = folder + "_" + date + ".tar.gz"
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(folder, arcname=os.path.basename(folder))
    print("File compressed successfully")
    return output_filename


def main():
    folder = select_folder()
    output_filename = compress(folder)
    shutil.move(output_filename, folder)
    print("File moved to the folder successfully")

if __name__ == "__main__":
    main()
