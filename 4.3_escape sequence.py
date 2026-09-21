"""
What are escape sequence/ characters?
- used when we need to include certain special characters in a string which we cannot otherwise include/ directly typed
\n - new/ next line
\t - tab
\\ - backlash
\' - a single quote inside a single-quoted string
\"
"""

#\n
print("Hello everyone.\nHow are you?")

#\t
print("John 20")
print("John\t20")

#\\ - inserts a single backslash
#print("new\old") -> still works but there is a warning
print("yes\\no")

#\'
print('This is Python\'s class')
print("This is Python's class")

#\"
print("He says, \"we are learning python\"")
