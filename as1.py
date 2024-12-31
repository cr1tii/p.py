import sqlite3

# إنشاء قاعدة البيانات أو الاتصال بها
def create_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT
    )
    ''')
    conn.commit()
    conn.close()

# إضافة ملاحظة جديدة
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    if title and content:
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        print("Note added successfully!")
    else:
        print("Both title and content are required!")

# عرض جميع الملاحظات
def show_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()

    if notes:
        print("\n--- Notes ---")
        for note in notes:
            print(f"ID: {note[0]}\nTitle: {note[1]}\nContent: {note[2]}\n")
    else:
        print("No notes available.")

# حذف ملاحظة
def delete_note():
    note_id = input("Enter note ID to delete: ")
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    print(f"Note with ID {note_id} deleted.")

# القائمة الرئيسية
def main():
    create_db()
    while True:
        print("\nSimple Notes Application")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            show_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
