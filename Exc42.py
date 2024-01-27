# moving a file to any destination
import os

source = "C:\\Users\\serda\\dev\\test2.txt"
destination = "C:\\Users\\serda\\OneDrive\\Desktop\\test2.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source, destination)
        print(f"{source} was moved.")

except FileNotFoundError:
    print(f"{source}: There is no such file")
