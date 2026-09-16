import os

# Get the current working directory

#print(os.getcwd()) 

# ------------------------------------------
# List all files and directories in the current working directory

#print(os.listdir()) 

# print(os.path.isfile("KBC_Game.py")) 
# print(os.path.exists("path")) 

#-------------------------------------------------

# if os.path.exists("test.txt"):
#     print("File mil gayi!")
# else:
#     print("File nahi mili.")

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")