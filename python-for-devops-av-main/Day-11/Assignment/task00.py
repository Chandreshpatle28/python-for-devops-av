# # Define a dictionary named 'student_info' containing information about a student
# student_info = {
#     "name": "Chandresh",  # Key: "name", Value: "Chandresh" (Student's name)
#     "age": "12",          # Key: "age", Value: "12" (Student's age)
#     "class": "X"          # Key: "class", Value: "X" (Student's class)
# }

# # Print the value associated with the "name" key from the 'student_info' dictionary
# print(student_info["name"])  # Output: Chandresh


# Define a list named 'student_info' containing dictionaries with information about students
student_info = [
    {
        "name": "Chandresh",  # Key: "name", Value: "Chandresh" (Student's name)
        "age": "12",          # Key: "age", Value: "12" (Student's age)
        "class": "X"          # Key: "class", Value: "X" (Student's class)
    },
    {
        "name": "Harish",     # Key: "name", Value: "Harish" (Student's name)
        "age": "32",          # Key: "age", Value: "32" (Student's age)
        "class": "XII"        # Key: "class", Value: "XII" (Student's class)
    },
    {
        "name": "Anshika",    # Key: "name", Value: "Anshika" (Student's name)
        "age": "8",           # Key: "age", Value: "8" (Student's age)
        "class": "III"        # Key: "class", Value: "III" (Student's class)
    }
]

# Print the information for each student in the 'student_info' list
print(student_info[1]["class"])
# for student in student_info:
#     print("Name:", student["name"])
#     print("Age:", student["age"])
#     print("Class:", student["class"])
#     print("\n")
