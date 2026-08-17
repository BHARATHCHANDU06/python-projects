shopping_list=[]
print("Welcome to Shopping List Manager:")
while True:
    print("\n1.Add Item")
    print("2. Remove Item")
    print("3.view Shopping List")
    print("4.Exit")
    choice=input("Enter your choice(1-4):")
    if choice =="1":
        item=input("Enter item to add:")
        shopping_list.append(item)
        print(item,"added successfully!")
    elif choice=="2":
        item=input("Enter item to remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item,"removed successfully!")
        else:
            print("Item not found!")
    elif choice=="3":
        if len(shopping_list)==0:
             print("shopping list is empty!")
        else:
            print("\n Your Shopping List")
            for i in range(len(shopping_list)):
                print(i+1,".",shopping_list[i])
    elif choice=="4":
        print("Thonk you for using Shopping List Manager!")
        break
    else:
        print("Invalid choice! Please try again.")