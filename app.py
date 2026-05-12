from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def home():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    conn.close()

    return render_template('index.html', notes=notes)

# Save note
@app.route('/add', methods=['POST'])
def add_note():
    data = request.form['note']

    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (content) VALUES (?)", (data,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Note added successfully"})

if __name__ == '__main__':
    app.run(debug=True)