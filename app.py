from flask import Flask, request, jsonify

import sqlite3

app = Flask(__name__)

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

@app.route('/')
def index():
    create_table()  # Create the "contact" table if it doesn't exist
    contacts = get_all_contacts()
    return jsonify(contacts)

@app.route('/insert', methods=['POST'])
def insert_contact():
    data = request.get_json()
    email = data['email']
    name = data['name']
    age = data['age']
    
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO contact (email, name, age) VALUES (?, ?, ?)
    ''', (email, name, age))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Contact inserted successfully"})

@app.route('/update/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.get_json()
    email = data['email']
    name = data['name']
    age = data['age']
    
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE contact
        SET email=?, name=?, age=?
        WHERE id=?
    ''', (email, name, age, id))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Contact updated successfully"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM contact WHERE id=?', (id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Contact deleted successfully"})

# Function to retrieve all contacts
def get_all_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contact')
    contacts = cursor.fetchall()
    
    conn.close()
    return [{"id": c[0], "email": c[1], "name": c[2], "age": c[3]} for c in contacts]

if __name__ == "__main__":
    app.run(debug=True)
