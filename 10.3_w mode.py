#w mode -> open the file for writing. if file exist then Overwrites the file

file_handler = open("file2_10_3.txt", "wt")
file_handler.write("This file is overwritten using w mode in Python.\n")
file_handler.write("Have a nice day!")
file_handler.close()

#if the file doesn't exist, then the w mode will create a new file and even write to it
#but x mode -> if file doesn't exist then create new file, if exist then error

