# contact_book.py
# Simple Contact Book

# Store contacts as a list of dictionaries
contacts = []

def add_contact():
    """Add a new contact"""
    print("\n--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    # Create contact dictionary
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added!")

def search_contact():
    """Search for a contact by name"""
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ")
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    
    print("Contact not found!")

def delete_contact():
    """Delete a contact by name"""
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ")
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted!")
            return
    
    print("Contact not found!")

def view_all():
    """Display all contacts"""
    print("\n--- All Contacts ---")
    
    if not contacts:
        print("No contacts yet!")
        return
    
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")

# Main menu loop
while True:
    print("\n" + "="*30)
    print("CONTACT BOOK")
    print("="*30)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All")
    print("5. Exit")
    print("="*30)
    
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    
    input("\nPress Enter to continue...")

    

