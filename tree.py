# Import 'listdir' from the 'os' module to get a list of files and directories in a given path
from os import listdir

# 'isfile' checks if a path points to a file
# 'join' combines directory and file names into a full path
from os.path import isfile, join

# Define a function called 'printnames' that takes a directory path as input
def printnames(dir):
    # Loop through all entries (files and folders) in the directory, sorted alphabetically
    for file in sorted(listdir(dir)):
        # Construct the full path of the current entry
        fullpath = join(dir, file)
        
        # Check if this full path is a file
        if isfile(fullpath):
            # If it's a file, print its name
            print(file)
        else:
            # If it's a directory, recursively call 'printnames' on that directory
            printnames(fullpath)

# Start the function with the root directory "C:/Users/sahir/Pictures/Scans"
# This will print all file names in that folder and its subfolders
printnames("C:/Users/sahir/Pictures/Scans")
