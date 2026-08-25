# ===== EXPENSE TRACKER =====

expense_names = []
expense_amounts = []

print("===== WELCOME TO EXPENSE TRACKER =====")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Remove Expense")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ===== ADD EXPENSE =====
    if choice == "1":
        name = input("Enter Expense Name: ")
        amount = float(input("Enter Amount: "))

        expense_names.append(name)
        expense_amounts.append(amount)

        print("Expense added successfully!")

    # ===== VIEW EXPENSES =====
    elif choice == "2":
        if len(expense_names) == 0:
            print("No expenses found!")
        else:
            print("\n===== EXPENSE LIST =====")
            for i in range(len(expense_names)):
                print(f"{i+1}. {expense_names[i]} - ₹{expense_amounts[i]}")

    # ===== TOTAL EXPENSE =====
    elif choice == "3":
        total = sum(expense_amounts)
        print("Total Expense: ₹", total)

    # ===== REMOVE EXPENSE =====
    elif choice == "4":
        name = input("Enter Expense Name to Remove: ")

        if name in expense_names:
            index = expense_names.index(name)

            expense_names.pop(index)
            expense_amounts.pop(index)

            print("Expense removed successfully!")
        else:
            print("Expense not found!")

    # ===== EXIT =====
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    # ===== INVALID OPTION =====
    else:
        print("Invalid choice! Please try again.")