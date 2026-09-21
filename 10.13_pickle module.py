"""
- when lists, tuple, set, dictionaries are stored in datatype memory/files, they need to be
converted into sequence of bytes, which the computer can understand, this process is called
serialization

- when we want to access these data structures back from this file that we have stored, these sequence of byte must be
converted into original datatype, this process is called de-serialization

#why can't we simply save in text file and read it back?
"""
import pickle
students = {'student1': {'roll':101, 'name':'John', 'percent':78.5},
           'student2': {'roll':102, 'name':'Carol', 'percent':91.5},
           'student3': {'roll':103, 'name':'Alice', 'percent':71.0}}

print(students)
print(type(students))
'''
with open("student_info_10.13_2.txt", "wt") as fh:
    # fh.write(students) error
    fh.write(str(students))


with open("student_info_10.13_2.txt", "rt") as fh:
    content = fh.read()

print(type(content))
# output = dict(content) error
# print(output)
#after converting the dictionaries into text file, the dictionaries cannot be accessed back

'''

#what to do? -----> use pickle module
#Serialization
with open("students_10_13_2.bin", "bw") as fh:
    for student in range(len(students)):
        pickle.dump(students[student], fh)

#De-serialization
with open("students_10_13_2.bin", "rb") as fh:
    data1 = pickle.load(fh)
    print(data1, type(data1))
    data2 = pickle.load(fh)
    print(data2, type(data2))
    data3 = pickle.load(fh)
    print(data3, type(data3))

    # data4 = pickle.load(fh)   ERROR
    # print(data4, type(data4))








