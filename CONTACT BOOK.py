import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        for contact in found_contacts:
            print(contact)

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            if address:
                self.contacts[index].address = address
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
        else:
            print("Invalid index.")

def display_menu():
    print("\nContact Manager Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            index = int(input("Enter contact number to update: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(index, name, phone, email, address)
        elif choice == '5':
            index = int(input("Enter contact number to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
