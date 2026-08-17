print("----STUDENT DATABASE")
student={}
student["Name"]=input("Enter Student Name:")
student["Roll Number"]=input("Enter Roll Number:")
student["Age"]=int(input("Enter Age:"))
student["Branch"]=input("Enter Branch:")
student["CGPA"]=float(input("Enter CGPA:"))
print("/n======STUDENT DETAILS======")
for key,value in student.items():
    print(key,":",value)
    choice = input("\nDo you want to update CGPA? (yes/no): ")

if choice.lower() == "yes":
    student["CGPA"] = float(input("Enter New CGPA: "))
    print("\nCGPA Updated Successfully!")

print("\nUpdated Student Details")

for key, value in student.items():
    print(key, ":", value)