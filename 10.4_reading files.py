#read() -> reads the contents of the file. if we open a file in text mode, it reads as string
"""
file_handler = open("practice_10_1.txt", 'rt')
content = file_handler.read()
file_handler.close()
print(content)
print(type(content))

# content = file_handler.read(10) #-> it will read only 1st 10 characters


#readline() -> also reads the content of the file, but it reads single line including /n at a time
file_handler = open("practice_10_1.txt", 'rt')
line1 = file_handler.readline()
line2 = file_handler.readline()
line3 = file_handler.readline()

line4 = file_handler.readline() #empty string -> file has reached end of file (EOF)
line5 = file_handler.readline()

file_handler.close()
print(f"Line 1: {line1}")
print(f"Line 2: {line2}")
print(f"Line 3: {line3}")

print(f"Line 4: {line4}") #empty string
print(f"Line 5: {line5}") #empty string
"""


#readlines() - reads all the line together
file_handler = open("practice_10_1.txt", 'rt')
lines = file_handler.readlines()
file_handler.close()

print(f"Lines: {lines}")
print(type(lines))

for line in lines:
    print(line.rstrip('\n'))
