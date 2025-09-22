import os

# Specify the directory path (use '.' for current directory)
path = '/New folder'  

# Get the list of all files and directories
contents = os.listdir(path)

print(f"Contents of directory '{path}':")
for item in contents:
    print(item)
