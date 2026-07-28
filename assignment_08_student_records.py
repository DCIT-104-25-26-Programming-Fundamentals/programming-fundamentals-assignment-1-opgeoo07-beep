# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
students = []
def add_student():
    name = input("Enter student's full name: ")
    student_id = input("Enter student ID: ")
    for student in students:
        if student["ID"] == student_id:
            print("A student with this ID already exists.")
            return

    scores = list(map(float, input("Enter scores separated by spaces: ").split()))

    students.append({
        "Name": name,
        "ID": student_id,
        "Scores": scores
    })

    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 50)
    for student in students:
        average = sum(student["Scores"]) / len(student["Scores"])
        print(f"Name   : {student['Name']}")
        print(f"ID     : {student['ID']}")
        print(f"Scores : {student['Scores']}")
        print(f"Average: {average:.2f}")
        print("-" * 50)

def search_student():
    student_id = input("Enter student ID to search: ")

    for student in students:
        if student["ID"] == student_id:
            average = sum(student["Scores"]) / len(student["Scores"])
            print("\nStudent Found")
            print(f"Name   : {student['Name']}")
            print(f"ID     : {student['ID']}")
            print(f"Scores : {student['Scores']}")
            print(f"Average: {average:.2f}")
            return

    print("Student not found.")

def update_scores():
    student_id = input("Enter student ID: ")

    for student in students:
        if student["ID"] == student_id:
            student["Scores"] = list(map(float,
                                         input("Enter new scores separated by spaces: ").split()))
            print("Scores updated successfully!")
            return

    print("Student not found.")
def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student not found.")
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Scores")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_scores()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
