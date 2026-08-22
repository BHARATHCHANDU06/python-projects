students=[]
print("\n ===STUDENT ATTENDAMCE SYSTEM===")
for i in range(5):
    name=input(f"Enter Student{i+1} Name:")
    students.append(name)
print("\nToday's Attendance")
for index,student in enumerate(students,start=1):
    print(index,student)
print("\n Total Students:",len(students))