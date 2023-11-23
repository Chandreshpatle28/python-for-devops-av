# Import the os module for interacting with the operating system
import os
# Prompt the user to enter a list of folder paths separated by spaces
folder = input("Enter a list of folder paths separated by spaces: ").split()

# List comprehension to create a list of files in each folder
for folder in folder:
    files = os.listdir(folder)
    # Printing the result of folder name
    print("listing files for the folder: " + folder)

    for file in files:
    # Printing the result
        print(file)