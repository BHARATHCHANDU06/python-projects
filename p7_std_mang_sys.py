# --------------------------------------
# Student Management System
# --------------------------------------

students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":

        student = {}

        student["Name"] = input("Enter Name: ")
        student["Roll Number"] = input("Enter Roll Number: ")
        student["Branch"] = input("Enter Branch: ")
        student["CGPA"] = float(input("Enter CGPA: "))

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\n----- Student Records -----")

            for student in students:
                print("--------------------------")
                for key, value in student.items():
                    print(key, ":", value)

    elif choice == "3":

        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["Name"].lower() == search_name.lower():

                print("\nStudent Found")
                for key, value in student.items():
                    print(key, ":", value)

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":

        remove_name = input("Enter student name to remove: ")

        found = False

        for student in students:

            if student["Name"].lower() == remove_name.lower():

                students.remove(student)

                print("Student Removed Successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":

        print("Thank you!")
        break

    else:
        print("Invalid Choice!")