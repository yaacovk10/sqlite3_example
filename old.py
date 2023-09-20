import sqlite3

# Function to create the "contact" table
def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

# Function to insert a new contact
def insert_contact(email, name, age):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO contact (email, name, age) VALUES (?, ?, ?)
    ''', (email, name, age))
    
    conn.commit()
    conn.close()

# Function to retrieve all contacts
def get_all_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contact')
    contacts = cursor.fetchall()
    
    conn.close()
    return contacts

# Function to update a contact by ID
def update_contact(contact_id, email, name, age):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE contact
        SET email=?, name=?, age=?
        WHERE id=?
    ''', (email, name, age, contact_id))
    
    conn.commit()
    conn.close()

# Function to delete a contact by ID
def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM contact WHERE id=?', (contact_id,))
    
    conn.commit()
    conn.close()

# Function to display the menu and handle user input
def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Insert a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Get all contacts")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            email = input("Enter email: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            insert_contact(email, name, age)
            print("Contact inserted successfully.")
        elif choice == '2':
            contact_id = input("Enter contact ID to update: ")
            email = input("Enter new email: ")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            update_contact(contact_id, email, name, age)
            print("Contact updated successfully.")
        elif choice == '3':
            contact_id = input("Enter contact ID to delete: ")
            delete_contact(contact_id)
            print("Contact deleted successfully.")
        elif choice == '4':
            contacts = get_all_contacts()
            print("\nAll Contacts:")
            for contact in contacts:
                print(contact)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_table()
    main_menu()

