"""
the 'with' statement
    - simplifies resource management by automatically handling the set-up and clean up task
    - it ensures that the resources are properly release even though there are errors in the code
    - it make the code clean

#we have to manually close the file
fh = open("practice_10_1.txt", 'rt')
content = fh.read()
fh.close()
print(content)

#using with statement
with open("practice_10_1.txt", 'rt') as fh:
    content = fh.read()

print(content)

#I have not close the file, file gets automatically closed
"""


with open("practice_10_6.txt", 'xt') as fh:
    fh.write("file creation.\n")
    fh.write("Bye")
