#student result system
name=input("Enter your name:")
roll_number=int(input("Enter your roll number:"))
english_marks=int(input("Enter your English marks:"))
math_marks=int(input("Enter your Math marks:"))
science_marks=int(input("Enter your Science marks:"))
#======\nSTUDENT RESULT====
print("Student Name:",name)
print("Roll Number:",roll_number)
print("English Marks:",english_marks)
print("Math Marks:",math_marks)
print("Science Marks:",science_marks)
total_marks=english_marks+math_marks+science_marks
print("Total Marks:",total_marks)
average=total_marks/3
print(f"Average Marks:",round(average,2))
if average>=90:
    print("Grade:A+")
elif average>=75:
    print("Grade:A")
elif average>=60:
    print("Grade:B")
elif average>=35:
    print("Grade:C")
else:
    print("fail")