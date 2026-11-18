import os

files = os.listdir("clutter folder")
i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"clutter folder/{file}", f"clutter folder/{i}.png")
        i = i+1