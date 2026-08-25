#======NOTES APP=====
notes=[]
while True:
   print("1.Add Note:")
   print("2.View Notes:")
   print("3.Delete Note:") 
   print("4.Exit:")
   choice=int(input("Enter the choice(1-4):"))
   if choice==1:
        note = input("Enter your note: ")
        notes.append(note)
        print("Note added successfully!") 
   elif choice==2:
        print(notes)
   elif choice==3:
        note=input("Enter the note to delete:")
        if note in notes:
            notes.remove(note)
            print("Note deleted successfully!") 
   elif choice==4:
     print("Thank you for using the Notes App!")
     break
   else:
    print("Invalid choice!")