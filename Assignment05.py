# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jocelyne, 7/30/2024, Modifying starter script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
import json
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)

try:
    # Extract the data from the file
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    # Print the data. If the columns aren't matching the FirstName, LastName, CourseName format, a KeyError exception will be thrown.
    print('Data:')
    for student in students:
        print(f'{student['FirstName']} {student['LastName']} is in {student['CourseName']}.')

# Key Error exception, such that  column names don't match FirstName, LastName, CourseName format.
except KeyError as e:
    print('There was an error reading the file in \'FirstName, LastName, CourseName\' format.')
    print(e, e.__doc__,'\n')
    print('Reassigning mapping keys within the json file...')
    # I will reassign the current json data to have FirstName, LastName, CourseName format.
    tempList = []  # make a new list, functions the same as students list
    # Iterate through each student in the current json data
    for student in students:
        keysList = list(student.keys())  # Gets the map keys for the current student, e.g. FirstName, LastName, CourseName
        print(keysList)
        # Redefine the current student to have the keys FirstName, LastName, CourseName. Uses the old keys to find the necessary entries
        student= {'FirstName':student[keysList[0]], 'LastName':student[keysList[1]], 'CourseName':student[keysList[2]]}
        tempList.append(student)  # Append the reassigned student data to tempList
        print(f'{student['FirstName']}, {student['LastName']}, {student['CourseName']}.')

    # Rewrite this new student list into the json file.
    file = open(FILE_NAME, "w")
    json.dump(tempList, file)
    file.close()
    print('Finished resetting keys to \'FirstName, LastName, CourseName\' format.')

    # Now, we can reread the json file to reset the students list to the corrected version
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    # Print data. It should print without error.
    print('Data:')
    for student in students:
        print(f'{student['FirstName']} {student['LastName']} is in {student['CourseName']}.')

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First Name may only contain letters.')
        except ValueError as e:
            print('User entered numbers inside the First Name field. Please try again.')
            break
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data: dict[str, str] = {'FirstName' : student_first_name, 'LastName' : student_last_name, 'CourseName' : course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
