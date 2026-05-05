# Student Record Management System

students = []
PASS_MARK = 50

# Function to add student records

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "id": student_id,
        "marks": marks
    }

    students.append(student)
    print("Student record added successfully!\n")


# Function to display all students

def display_students():
    if len(students) == 0:
        print("No student records available.\n")
    else:
        print("\nStudent Records")
        print("-----------------------")

        for student in students:
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Marks: {student['marks']}")

            if student['marks'] >= PASS_MARK:
                print("Status: Pass")
            else:
                print("Status: Fail")

            print("-----------------------")


# Function to search for a student

def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student['name'].lower() == search_name.lower():
            print("\nStudent Found")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Marks: {student['marks']}")
            found = True
            break

    if not found:
        print("Student not found.\n")


# Function to calculate average marks

        print("Invalid choice. Please try again.")
