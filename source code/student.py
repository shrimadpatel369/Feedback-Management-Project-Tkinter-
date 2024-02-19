from tkinter import *
from tkinter import messagebox
from subprocess import call
import sqlite3

# Create the main window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# place the logo in the window
img = PhotoImage(file='F:/AU/SEM 3/CSE 100/project/logo.png')
Label(root, image=img, bg='white').place(x=120, y=120)

# Create a frame inside the window
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

# Create a heading label
heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Create the username entry fields
def enter(e):
    user.delete(0, 'end')

def leave(e):
    name = user.get()
    if name == '':
        password.insert(0, 'username')
    

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', enter)
user.bind('<FocusOut>', leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Create the password entry fields
def enter(e):
    password.delete(0, 'end')

def leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'password')

password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', enter)
password.bind('<FocusOut>', leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Function to sign in
def sign_in(old_root):
    conn = sqlite3.connect('credential.db')
    c = conn.cursor()

    username = user.get()
    password_value = password.get()

    print("Entered username:", username)
    print("Entered password:", password_value)

    c.execute("SELECT * FROM student WHERE username=? AND password=?", (username, password_value))
    result = c.fetchone()

    if result:
        old_root.destroy()
        call(["python", "department.py"])
    else:
        messagebox.showerror("Error", "Invalid username or password")

    conn.close()

# Function to sign up
def sign_up():
    for widget in frame.winfo_children():
            widget.destroy()
    part2()

# Create the sign in and sign up buttons
Button(frame, width=20, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=lambda: sign_in(root)).place(x=100, y=204)
signuptext = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 11))
signuptext.place(x=20, y=250)
signup = Button(frame, width=20, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0,command=lambda: sign_up())
signup.place(x=200, y=250)

# Function to sign up
def part2():
    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # Create the username entry fields
    def enter(e):
        user.delete(0, 'end')

    def leave(e):
        name = user.get()
        if name == '':
            password.insert(0, 'username')
    
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', enter)
    user.bind('<FocusOut>', leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Create the password entry fields
    def enter(e):
        password.delete(0, 'end')

    def leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'password')

    password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', enter)
    password.bind('<FocusOut>', leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
    
    # Create the confirm password entry fields
    def enter(e):
        passconfirm.delete(0, 'end')
    
    def leave(e):
        name = passconfirm.get()
        if name == '':
            passconfirm.insert(0, 'Confirm Password')
    
    passconfirm = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    passconfirm.place(x=30, y=220)
    passconfirm.insert(0, 'Confirm Password')
    passconfirm.bind('<FocusIn>', enter)
    passconfirm.bind('<FocusOut>', leave)
    
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
    
    # Function to sign up
    def sign_up():
        username = user.get()
        password_value = password.get()
        confirm_password_value = passconfirm.get()
        
        print("Entered username:", username)
        print("Entered password:", password_value)
        print("Entered confirm password:", confirm_password_value)

        if password_value != confirm_password_value:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            conn = sqlite3.connect('credential.db')
            c = conn.cursor()
            
            c.execute("SELECT * FROM student WHERE username=?", (username,))
            result = c.fetchone()
            if result:
                messagebox.showerror("Error", "Username already exists")
            else:
                c.execute("INSERT INTO student (username, password) VALUES (?, ?)", (username, password_value))
                conn.commit()
                messagebox.showinfo("Success", "Account created successfully")
                
            conn.close()
    
    Button(frame, width=20, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=lambda: sign_up()).place(x=100, y=270)

# Start the main event loop
root.mainloop()
