#input will run in the runtime where the CLI arguments and Environmental variables execute in compilation

import os

folders = input("Please provide the list of folders name with spaces in between: ").split() #Please provide the list of folders name with spaces in between: /opt /etc /bin

for folder in folders:
    files = os.listdir(folder)
    print("===Listing files for the folder-> " + folder)

    for file in files:
        print(file)
    
                  
"""
---------OUTPUT--------
Please provide the list of folders name with spaces in between: /opt /tm
===Listing files for the folder-> /opt
conda
containerd
python
tmp
oryx
dotnet
Traceback (most recent call last):
  File "/workspaces/Python/input.py", line 8, in <module>
    files = os.listdir(folder)
FileNotFoundError: [Errno 2] No such file or directory: '/tm'
"""