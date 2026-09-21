"""
Variable length keyword arguments -> **kwargs
    - used to take 0 or more variable length keyword arguments
    - kwargs - stores stuffs in form of dictionary
    - it should be the last argument in the function definition
        def student_details(**s_marks, s_name, s_id): ERROR
    - *args comes first then **args(should be the last argument)
        def student_details(s_id, s_name, *extra, **s_marks):

#**kwargs
def func(**kwargs):
    print(kwargs, type(kwargs)) #output -> {'x': 10, 'y': 20}, dictionary

func(x=10, y=20)
func() #empty dictionary
"""

def student_details(s_id, s_name, *extra, **s_marks):
    if len(s_marks) == 0:
        print(f"{s_name} with id {s_id} was absent!")
    else:
        percent = sum(s_marks.values())/len(s_marks)
        print(f"{s_name} with id {s_id} secured {round(percent, 2)}%")
    print(f"{s_name} does {extra}")

student_details(101, "John", 'football', sub1 = 87.0, sub2 = 69.5, sub3 = 81.5, sub4 = 74.0)
student_details(102, "Carol", sub1 = 91.0, sub2 = 49.5, sub3 = 91.5, sub4 = 84.0, sub5 = 86.5)
student_details(103, "Mark", sub1 = 81.5, sub2 = 83.5, sub3 = 79.0)
student_details(104, "Alice" )

