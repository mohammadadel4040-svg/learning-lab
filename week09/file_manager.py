# Week 9 - File Manager using os module

import os


def file_manager():

    # 1 Current directory
    current_dir = os.getcwd()
    print("Current Directory:", current_dir)

    folder = "lab_files"

    # 2 Create folder
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Folder created")

    # 3 Create files
    files = ["file1.txt", "file2.txt", "file3.txt"]

    for file in files:
        path = os.path.join(folder, file)
        with open(path, "w") as f:
            f.write("Sample content")
        print("Created:", file)

    # 4 List files
    print("\nFiles:")
    for file in os.listdir(folder):
        print("-", file)

    # 5 Rename file
    old = os.path.join(folder, "file2.txt")
    new = os.path.join(folder, "renamed.txt")

    if os.path.exists(old):
        os.rename(old, new)
        print("\nFile renamed")

    # 6 Cleanup
    print("\nCleaning...")
    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))

    os.rmdir(folder)
    print("Cleanup completed")


file_manager()
