import io
try:
    fh = open("file_10_10.txt", 'wt')
    # data = fh.read()
    data = fh.write("Hello")
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print(file_err)
except io.UnsupportedOperation:
    print("io error")
# else:
#     print("else block")
#     # print(data)
finally:
    print("finally block")
    fh.close()
"""
else
    - when there is no error/ exception in the try block, the flow enters an block called else 
finally
    - always executed irrespective of whether errors happens or not
    
- when there is an error, the flow goes to the else and then finally block, if
there is an error then the flow goes to the exceptions and then finally block

- fh.close() can be go the finally block, therefore finally block executed in both the cases therefore it's needed

- when we write a try, at least 1 except is required.  else and finally are optional

- else and finally sometimes cannot come together, either try-except with else or try-except with finally

- or all 4 of them try except else finally together -> that also fine
"""

