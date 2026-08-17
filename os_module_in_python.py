import os

# Get the current working directory

#print(os.getcwd()) 

# ------------------------------------------
# List all files and directories in the current working directory

#print(os.listdir()) 

# print(os.path.isfile("KBC_Game.py")) 
# print(os.path.exists("path")) 

#-------------------------------------------------

if os.path.exists("test.txt"):
    print("File mil gayi!")
else:
    print("File nahi mili.")