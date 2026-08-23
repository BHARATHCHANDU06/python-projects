# ===== INVENTORY MANAGEMENT SYSTEM =====

products = []

print("===== WELCOME TO INVENTORY MANAGEMENT SYSTEM =====")

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Count Products")
    print("6. Exit")

    choice = int(input("Enter Your Choice (1-6): "))

    # ===== ADD PRODUCT =====
    if choice == 1:
        product = input("Enter Product Name: ")

        if product in products:
            print(product, "already exists!")
        else:
            products.append(product)
            print(product, "added successfully!")

    # ===== VIEW PRODUCTS =====
    elif choice == 2:
        if len(products) == 0:
            print("Inventory is empty!")
        else:
            print("\n===== PRODUCT LIST =====")
            for i, product in enumerate(products, start=1):
                print(i, ".", product)

    # ===== REMOVE PRODUCT =====
    elif choice == 3:
        product = input("Enter Product Name to Remove: ")

        if product in products:
            products.remove(product)
            print(product, "removed successfully!")
        else:
            print("Product not found!")

    # ===== SEARCH PRODUCT =====
    elif choice == 4:
        product = input("Enter Product Name to Search: ")

        if product in products:
            print(product, "is available.")
        else:
            print(product, "is not available.")

    # ===== COUNT PRODUCTS =====
    elif choice == 5:
        print("Total Products:", len(products))

    # ===== EXIT =====
    elif choice == 6:
        print("Thank you for using Inventory Management System!")
        break

    # ===== INVALID CHOICE =====
    else:
        print("Please enter a valid option!")