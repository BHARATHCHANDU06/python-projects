contacts=[]
while True:
    print("1. Add contact")
    print("2. View contacts")   
    print("3.Search contact")
    print("4.Delete contact")
    print("5. Exit")
    choice = input("Enter your choice(1-5): ")
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts.append({'name': name, 'phone': phone})
        print("Contact added successfully!")
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")   
    elif choice == '3':
        search_name = input("Enter contact name to search: ")
        found_contacts = [contact for contact in contacts if contact['name'].lower() == search_name.lower()]
        if not found_contacts:
            print("Contact not found.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == '4':
        delete_name = input("Enter contact name to delete: ")
        contacts = [contact for contact in contacts if contact['name'].lower() != delete_name.lower()]
        print("Contact deleted successfully!")  
    elif choice == '5':
        print("Exiting the program.")
        break 
    else:
        print("Invalid choice. Please try again.")