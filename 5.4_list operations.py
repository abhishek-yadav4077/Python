"""
reverse()
    - it reverses the list, the elements/items of the list gets reversed
    - changes the list itself
sort()
    - sorts the list in ascending(default)/ descending order
count()
    - counts how many times a particular element is present in the list
Membership operations in list
    - in (whether a particular item is present inside list or not)
    - not in (reverse of in)

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)

days_of_week.reverse()
print(days_of_week)

nums = [4, 9, 0, 1, 2, 8]
print(nums)
nums.sort()
print("Sorted list:", nums)
nums.sort(reverse=True)
print(nums) #descending order


numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

language = ["Python", "Java", "C++", "Python"]
print(f"The list is: {language}")
item_to_count2 = input("Enter the language to be counted from the above list: ")
c2 = language.count(item_to_count2)
print(f"Occurrence of {item_to_count2} is {c2}")
"""

language = ["Python", "Java", "C++", "Python"]
print("Python" in language)
print("Javascript" in language)

print("Python" not in language)
print("Javascript" not in language)






