file_handler = open("practice_10_1.txt", 'rt')
content = file_handler.read()
file_handler.close()

print(content)

"""
What if want to read a file which is not exists ? -> ERROR
What if we opened a file in read mode and try to write something ? -> ERROR
What if we opened a file in write/append/x mode and try to read something ? -> ERROR

- if we opened a file in write mode and try to read something -> we will surely get a error but the file content gets deleted

"""