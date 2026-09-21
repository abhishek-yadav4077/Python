"""
os.path.exists()
    - the exist function is the part of the os module
    - it's a straight forward of checking if a file exists or not
    - we can do the same thing with directory as well

pathlib.Path.exists()


import os

# file_name = "practice_10_1.txt" #one way, if file present in current directory
file_name = "C:/Users/Tarkeshwar/PycharmProjects/my_project/practice_10_1.txt" #another way, to use absolute path ->  give front slash everywhere, if file not present in current directory

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exists.")
"""


from pathlib import Path

file_name = Path("C:/Users/Tarkeshwar/PycharmProjects/my_project/practice_10_1.txt")

if file_name.exists:
    print("File exists. Cannot create a file")
else:
    print("File does not exists. Creating it!")
    fh = open(file_name, 'xt')
    fh.write("Some content")
    fh.close()