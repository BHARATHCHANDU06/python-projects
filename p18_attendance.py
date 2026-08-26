students = []
while True:
 print("1.Add Student:")
 print("2.Mark present:")
 print("3.View Attendance")
 print("4.Exit")
 choice=int(input("Enter your choice:(1-4):"))
 if choice==1:
     student=input("Enter the student's name:") 
     if student in students:
         print("Student is already added.")
     else:
         students.append(student)
         print("Student added successfully.")
 elif choice==2:
     student=input("Enter the student's name:")
     if student in students:
         print("Student is already marked present.")
     else:
         students.append(student)
         print("Student marked present.")
 elif choice==3:
     print("Attendance List:",students)
 elif choice==4:
     print("Exiting the program.")
     break
 else:
     print("Invalid choice! Please enter a valid option (1-4).")