## Student Management System
This Python program is designed to manage student records using basic CRUD (Create, Read, Update, Delete) operations. 

The following fields are required for each student record:

- `student_id`: a 7-digit string or character
- `name`: first name of the student
- `family_name`: last name of the student
- `admission_year`: a 4-digit integer representing the year the student joined the university
- `field`: an integer representing the field of study, with the following options:

1. computer
2. civil
3. agriculture
4. electrical
5. mechanic


The user can add, remove, search, and update student records using a command-line interface. The program stores the student records in a file named data.txt.

To add a new student, the user is prompted to enter the required fields. If the entered student_id already exists in the file, an error message is displayed.

To remove a student, the user is prompted to enter the student_id of the student to be removed. If the student_id is found, the corresponding record is deleted from the database. If not, an error message is displayed.

To search for a student, the user is prompted to enter the student_id of the student to be searched. If the student_id is found, the corresponding record is displayed. If not, an error message is displayed.

To update a student record, the user is prompted to enter the student_id of the student to be edited. 

If the student_id is found, the corresponding record is displayed along with a menu of fields that can be edited.

The user can select a field to edit and enter the new value. The updated record is then stored in the database.
