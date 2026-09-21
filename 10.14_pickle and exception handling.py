import pickle
students = {'student1': {'roll':101, 'name':'John', 'percent':98.5},
            'student2': {'roll':102, 'name':'Carol', 'percent':81.5},
            'student3': {'roll':103, 'name':'Alice', 'percent':90.5}}


print(students)
print(type(students))

#Serialization
with open("students_10_14_2.bin", "bw") as fh:
    for student in students:
        pickle.dump(students[student], fh)
'''
#De-serialization
with open("students_10_14_2.bin", "rb") as fh:
    
    data1 = pickle.load(fh)
    print(data1, type(data1))
    data2 = pickle.load(fh)
    print(data2, type(data2))
    data3 = pickle.load(fh)
    print(data3, type(data3))
    

#what if we don't know how many data is present ?
    while True:
        try:
            data = pickle.load(fh)
            print(data, type(data))
        except EOFError:
            print("Done!")
            break
'''
##Print the names of the students as a list who secured 90 or more percent
student_list_90 = []
with open("students_10_14_2.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] >= 90:
                student_list_90.append(data['name'])
        except EOFError:
            print("Done!")
            break

print(f"List of student who secured 90 or more are: {student_list_90}")

