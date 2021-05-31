# Student-Record-App
An application to record students to files with various information

This application has two main functions:
- registering a student and writing information to file
- reading a student record from file

While registering a student; the application asks for student name, surname, ID and grade. A file named as given ID (e.g. 123456.txt) is created and all given information is written to that file. Furthermore, the letter grade is calculated based on the grade point provided in registration phase and written to related file. All these mean that a unique file is created for each student and these files carry student IDs as their names.

While reading a student record; the application asks for student ID and it reads related data from the file, then it displays all. 

## Usage:

Windows: `python student-record-app.py`<br>
Linux: `python3 student-record-app.py`
