#Exceptional handling means instead of terminating the program, for a known error(exeption), we should give proper error message without breaking the execution.

import os

folders = input("Please provide the list of folders name with spaces in between: ").split() #Please provide the list of folders name with spaces in between: /opt /etc /bin

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this folder does not exist: " + folder)
        continue
    except PermissionError:
        print("No access to this folder: " + folder)
        break
    print("===Listing files for the folder-> " + folder)

    for file in files:
        print(file)


"""
---------OUTPUT--------
Please provide the list of folders name with spaces in between: /tm /opt
Please provide a valid folder name, looks like this folder does not exist: /tm
===Listing files for the folder-> /opt
conda
containerd
python
tmp
oryx
dotnet
"""