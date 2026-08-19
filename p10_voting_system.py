#====VOTING SYSTEM====
name=input("Enter your name:")  
age=int(input("Enter the Age:"))
if age>=18:
    print("you are eligible to vote")
if age>=18:
    print("Please select your candidate from the following list:")
    print("1.Candidate A")
    print("2.Candidate B")
    print("3.Candidate C")
    choice=int(input("Enter your choice(1-3):"))
    if choice==1:
       print("vote recorded for Candidate A")
    elif choice==2:
       print("vote recorded for Candidate B")  
    elif choice==3:
       print("vote recorded for Candidate C")
    else:
         print("Invalid choice! Please select a valid candidate.")
    print("THANK YOU",name,"!Your vote has been recorded successfully.")   
else:
    print("sorry",name,"!You are not eligible to vote as you are under 18 years of age.")