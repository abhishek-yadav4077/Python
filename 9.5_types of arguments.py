"""
Variable length arguments - *args
    - a function which allows n number of arguments to be passed

#*args -> allows variable length positional arguments (0 to n)
def add(*args):
    # print(args, type(args))
    return sum(args)

result = add(10, 20, 4, 1, 2, 3, 9) #the value gets stored in the argument args as a tuple
print(result)

#star agrs *args exhaust all the positional arguments
"""

def student_details(s_id, s_name, *s_marks):
    if len(s_marks) == 0:
        print(f"{s_name} with id {s_id} was absent!")
    else:
        percent = sum(s_marks)/len(s_marks)
        print(f"{s_name} with id {s_id} secured {round(percent, 2)}%")

student_details(101, "John", 87.0, 69.5, 81.5, 74.0)
student_details(102, "Carol", 91.0, 49.5, 91.5, 84.0, 86.5)
student_details(103, "Mark", 81.5, 83.5, 79.0)
student_details(104, "Alice" )



