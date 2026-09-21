"""
We have the following dictionary containing details:

user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}

Delete the sensitive information from the dictionary present in a list
sensitive_info = ["password", "address"]
"""

user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}
sensitive_info = ["password", "address", "phone"]

# for key in user:
#     if key in sensitive_info:
#         user.pop(key)             runtime error -> we cannot change/pop in middle of the execution of for loop
#
# print(user)

for i in sensitive_info:
    if i in user:
        print(f"DELETED => Key: {i}, Value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")

print(user)

#what will happen if we try to delete a key "phone" which is not present ? -> key error

