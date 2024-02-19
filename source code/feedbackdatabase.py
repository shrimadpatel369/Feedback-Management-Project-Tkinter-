import sqlite3

# Create a database to store feedback
def create_table():
    try:
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()

        # Create feedback table
        c.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                faculty_name TEXT
                satisfaction TEXT,
                clear_explanations TEXT,
                engagement TEXT,
                organization TEXT,
                comments TEXT
            );
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

# Save feedback to the database
def save_feedback(faculty_name, satisfaction, clear_explanations, engagement, organization, comments):
    try:
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()

        c.execute('''
            INSERT INTO feedback (faculty_name, satisfaction, clear_explanations, engagement, organization, comments)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (faculty_name, satisfaction, clear_explanations, engagement, organization, comments))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error saving feedback: {e}")
    finally:
        conn.close()

# Get feedback from the database
def get_data():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT * FROM feedback')
    fetched_data = c.fetchall()
    conn.close()
    return fetched_data


