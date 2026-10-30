import os
files = os.listdir('Clutter Folder')
i = 1
for file in files:
    if file.endswith('.jpg'):
        print(file)
        os.rename(f"Clutter Folder/{file}", f"Clutter Folder/pic_{i}.jpg")
        i = i+1