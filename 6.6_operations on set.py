student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics", "CS"}
student3 = {"Sanskrit", "Maths", "CS"}
print(student1, type(student1))
print(student2, type(student2))
print(student3, type(student3))

#Intersection - common subjects of student1 and student2
common_subjects = student1.intersection(student2, student3)
print(common_subjects)
common_subjects = student1 & student2 & student3 #another way
print(common_subjects)


#with no output - we got an empty set -> representation -> set()


#Union - all subjects of student1 and student2, thats why concatenation does not work
all_subjects = student1.union(student2, student3)
print(all_subjects)
all_subjects = student1 | student2 | student3 #another way
print(all_subjects)


#difference - difference of sets
days_of_week = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}
weekdays = days_of_week.difference(weekends)
print(weekdays)
weekdays = days_of_week - weekends #another way
print(weekdays)



