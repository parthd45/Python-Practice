students = []

def add_student():
    name = input("Enter student name: ")
    marks = []
    for subject in ["Math", "Science", "English"]:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }
    students.append(student)
    print(f"\n{name}'s record added successfully!\n")


def show_all_students():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n---------- STUDENT REPORT ----------")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("------------------------------------")


def search_student():
    name = input("Enter name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found:")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Total: {student['total']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            return
    print("\nStudent not found.\n")


def delete_student():
    name = input("Enter name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"\n{name}'s record deleted.\n")
            return
    print("\nStudent not found.\n")


while True:
    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. Show all students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Please try again.")