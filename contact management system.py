# Simple Contact Manager

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} | {contact['phone']} | {contact['email']}")
        print()

def edit_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("Enter new name: ")
            contacts[index]["phone"] = input("Enter new phone: ")
            contacts[index]["email"] = input("Enter new email: ")
            print("Contact updated!\n")
        else:
            print("Invalid contact number.\n")
    except:
        print("Please enter a number.\n")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact: {removed['name']}\n")
        else:
            print("Invalid contact number.\n")
    except:
        print("Please enter a number.\n")

def main():
    while True:
        print("Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
