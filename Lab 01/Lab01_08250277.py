# Inithalize an empty list and dictionary to store student data
students_list = []  # This list will hold the names os students.
students_dict = {} # This dictionary will store detailed information about each students.

# Input student details
name = input("Enter student name: ") # Prompts the user to enter the students name.
age = int(input("Enter student age: ")) # Prompts for the age and converts it to an integer.
grade = int(input("enter student grade: ")) # Prompts for the grade and converts it to integer.

# Add student to the list and dictionary
students_list.append(name) #Adds the students name to the list.
students_dict[name] = {"age": age, "grade": grade} # Adds the students details to the dictionary.

# Success message
print(f"student {name} has  been successfully added!") # Confirms that the student has been added.
print("current students list:", students_list) # Displays the current list of students.
print("detailed student records:", students_dict) # Displays the detailed records in the dictionary.

# Search for a student
search_name = input("Enter the name of the student you want to find: ") # Prompts the user to enter a name to search for.
if search_name in students_dict: # Checks if the name exists in dictionary.
   print(f"Found: {search_name}, age: {students_dict[search_name]["age"]}, grade: {students_dict[search_name]["grade"]}") # Prints the students details if found.
else:
    print("student not found in the records.") # Informs the user if the student is not found.

# Remove a student 
remove_name = input("Enter the name of the student to remove: ") # Prompts for the name to remove.
if remove_name in students_dict: # Checks if the name exixts.
    students_list.remove(remove_name) # Removes the students name from the list.
    del students_dict[remove_name] # Removes the students details from the dictionary.
    print(f"student {remove_name} has been successfilly removed!") # Confirms the removal.
else: 
    print("student not found in the record.") # Informs the user if the student is not found.

# Display updated student information
    print("updated list of student:",students_list) # Displays the updated list.
    print("updated student details:", students_dict) # Displays the updated detailed records.