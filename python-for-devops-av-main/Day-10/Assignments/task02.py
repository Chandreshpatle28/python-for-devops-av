# Import the os module for interacting with the operating system
import os
# Prompt the user to enter a list of folder paths separated by spaces
folders = input("Enter a list of folder paths separated by spaces: ").split()
# Iterate through each folder path provided by the user
for folder in folders:
    try:
        files = os.listdir(folder)   # Get the list of files in the current folder
        # Print the folder path to indicate the following list of files belongs to this folder
        print("Listing files for the folder: " + folder)

     # Handle the case where the specified folder is not found
    except FileNotFoundError:
        print("Error: Folder not found - " + folder)
    # Handle the case where there's a permission issue accessing the folder
    except PermissionError:
        print("Error: Permission denied - " + folder)

    print("\n")  # Adding a line break for better readability
    
    # Continue to the next iteration of the loop, even if an exception occurred
    continue     
# Iterate through each file in the current folder and print its name
for file in files:
        print(file)