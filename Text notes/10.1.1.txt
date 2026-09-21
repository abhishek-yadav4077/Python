"""
- datas are stored in files and need to be handled efficiently

In python, files are classified/handled in 2 ways
    1.Text files
        - stores datas in form of text characters
          e.g. name of employee/client
    2.Binary files
        - stores data in form of bytes(group of 8 bits)
        e.g. image files, files, video files

Operations performed on files
    - read, edit, create, open, close, add, delete, overwrite etc.

(i) firstly, we need to open a file in python -> open()
    syntax -> open(file_name, mode_to_open)
    - Modes: read -> r, create -> x, write -> w, append -> a, work with text file -> t, work with binary files -> b.
    rt are default modes

(ii) close the file -> close()
    syntax -> file_object.close()
"""

#opening a file -> open()
file_handler = open("practice_10_1.txt", "rt")
print(file_handler)
#Read operation

#closing a file -> close()
file_handler.close()
print(file_handler)
#after closing a file, we cannot perform any operation on them
#we can close it multiple times
file_handler.close()
file_handler.close()
file_handler.close()
file_handler.close()





