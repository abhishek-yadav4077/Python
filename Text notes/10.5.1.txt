
"""
#a mode -> it appends/adds the end of the file
#file already exists
file_handler = open("file2_10_3.txt", 'at')
file_handler.write("\nThis content has been written using 'a' mode.\n")
file_handler.write("'a' mode is used to add new content at the end of the file.\n")
file_handler.write("Good bye!")
file_handler.close()
"""


#file do not exist ? - similar to w mode, but it doesn't overwrite any content, it adds the content at the end of the file
file_handler = open("file4_10_5.txt", 'at')
file_handler.write("This file has been created using 'a' mode.\n")
file_handler.write("'a' mode creates the file not already existing.\n")
file_handler.write("Good bye!")
file_handler.close()


