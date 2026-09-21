#x mode -> create a file, if the file already existswe cannot re-create the same file
file_handler = open("file_10_2.txt", 'xt')

#write(content) - writing into a file
file_handler.write("This file is created using the 'x' mode in Python.\n")
file_handler.write("Next line.")

#closing the file
file_handler.close()
