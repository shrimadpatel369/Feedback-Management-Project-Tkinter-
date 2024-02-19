import sqlite3

# Create a database to store student and faculty credentials
def create_tables():
    conn = sqlite3.connect('credential.db')
    c = conn.cursor()

    # Create student table
    c.execute('''CREATE TABLE student(Name text, type text, username text, password text);''')
    conn.commit()

    # Insert sample student data
    c.execute("INSERT INTO student VALUES('shrimad','student','shrimad','patel')")
    conn.commit()

    # Create faculty table
    c.execute('''CREATE TABLE faculty(Name text, type text, username text, password text);''')
    conn.commit()

    # Insert sample faculty data
    c.execute("INSERT INTO faculty VALUES('Neel Chapagain','faculty','Neel Chapagain','123456')")
    conn.commit()
    conn.close()

create_tables()
