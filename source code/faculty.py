from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
import feedbackdatabase
import sqlite3

# Create the main window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Create a frame inside the window
frame = Frame(root, width=850, height=430, bg="lightblue")
frame.place(x=40, y=50)

# Place the logo in the frame
img = PhotoImage(file='F:/AU/SEM 3/CSE 100/project/logo.png')
Label(frame, image=img, bg='white').place(x=120, y=120)

# Create a heading label
heading = Label(frame, text='Sign in', fg='#57a1f8', bg='lightblue', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=600, y=50)

# Create the username entry fields
def enter(e):
    user.delete(0, 'end')

def leave(e):
    name = user.get()
    if name == '':
        password.insert(0, 'username')
    
user = Entry(frame, width=35, fg='black', border=0, bg="lightblue", font=('Microsoft YaHei UI Light', 11))
user.place(x=500, y=150)
user.insert(0, 'Username')
user.bind('<FocusIn>', enter)
user.bind('<FocusOut>', leave)

Frame(frame, width=290, height=2, bg='black').place(x=500, y=170)

# Create the password entry fields
def enter(e):
    password.delete(0, 'end')

def leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'password')

password = Entry(frame, width=25, fg='black', border=0, bg="lightblue", font=('Microsoft YaHei UI Light', 11))
password.place(x=500, y=220)
password.insert(0, 'Password')
password.bind('<FocusIn>', enter)
password.bind('<FocusOut>', leave)

Frame(frame, width=295, height=2, bg='black').place(x=500, y=240)


global username_entered

# Function to sign in
def sign_in(old_root):
    conn = sqlite3.connect('credential.db')
    c = conn.cursor()

    username = user.get()
    password_value = password.get()

    print("Entered username:", username)
    print("Entered password:", password_value)
    
    c.execute("SELECT * FROM faculty WHERE username=? AND password=?", (username, password_value))
    result = c.fetchone()

    if result:
        global username_entered
        username_entered = username

        for widget in frame.winfo_children():
            widget.destroy()
        part3()
            
    else:
        messagebox.showerror("Error", "Invalid username or password")

    conn.close()

# Function to sign up
def sign_up():
    for widget in frame.winfo_children():
            widget.destroy()
    part2()

# Button to sign in and sign up    
Button(frame, width=25, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=lambda:sign_in(root)).place(x=550, y=280)
signuptext = Label(frame, text="Don't have an account?", fg='black', bg='lightblue', font=('Microsoft YaHei UI Light', 11))
signuptext.place(x=480, y=350)
signup = Button(frame, width=20, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0,command=lambda: sign_up())
signup.place(x=650, y=350)

# Function to sign up
def part2():
    img = PhotoImage(file='F:/AU/SEM 3/CSE 100/project/logo.png')
    Label(frame, image=img, bg='white').place(x=120, y=120)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='lightblue', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=600, y=50)

    # Create the username entry fields
    style = ttk.Style()
    style.configure("TCombobox", foreground='black', font=('Microsoft YaHei UI Light', 11))
    
    def block_key_event(event):
        return "break"
    
    user = ttk.Combobox(frame, values=['Ratna Ghosal', 'Ashutosh Kumar', 'Shomen Mukherjee','Bhuvan Pathak',
                                            'Balaji Prakash','Ashim Rai','Subhash Rajpurohit','Rama Ratnam',
                                            'Balachandran Ravindran', 'Souvik Gupta','Ritesh Shukla','Krishna Swamy',
                                            'Vivek Tanavde','Noopur Thakur','Preeti Manek', 'Sudhir Pandey', 'Saptam Patel', 
                                            'Chirag Trivedi','Tana Trivedi','Neel Chapagain', 'Aditya Kanth', 'Molly Kaushal', 'Ioannis Poulios',
                                            'Gaurav Bhattacharya', 'Aryan Chakraborty', 'Sugat Chaturvedi', 'A Damodaran',
                                            'Supratim Gupta','Samarth Gupta','Chakravarthi Rangarajan','Rahul Rao','Moumita Roy',
                                            'Rahul Singh','Abhinandan Sinha','Mita Suthar','Ishita Tripathi','Jeemol Unni',
                                            'Pallavi Vyas','Sonal Yadav','Fenil Shah','Minal Pathak', 'Samir Shah', 'Priyadarshi Shukla',
                                            'Poonam Dugar', 'Tanya Jain', 'Prateek Jain','Hetal Jhaveri',
                                            'Vaibhav Kadia','Narendra Kushwaha','Vinodh Madhavan','Parag Patel',
                                            'Binny Rawat','Kinshuk Saurabh','Saumil Shah','Nimit Thaker',
                                            'Vibha Tripathi','Shuja Ahmed', 'Jayendra Bhalodiya', 'Rupsa Bhowmick','Sanjay Chaudhary',
                                            'Sridhar Dalai','Bimal Das','Adarsh Ganesan','Arijit Ganguli',
                                            'Timothy Gonsalves', 'Sham Gurav','Mona Jani','Keyur Joshi',
                                            'Sunil Kale','Harmeet Kaur','Maryam Kaveshgar','Snigdha Khuntia',
                                            'Deepak Kunzru','Anurag Lakhlani','Vinod Mall','Mayuribala Mangrulkar',
                                            'Anamika Maurya','Mitaxi Mehta','Shefali Naik','Amit Nanavati',
                                            'Sanket Patel','Dhaval Patel','Kuntal Patel','Shashi Prabh',
                                            'Dharamashi Rabari','Akhand Rai','Ashok Ranade','Mehul S Raval',
                                            'Souvik Roy','Naresh Sharma','Aditi Singhal','Ramya Srinivasan','Mazad Zaveri',
                                            'Kunal Basu', 'Aditya Chaturvedi', 'Manomohini Dutta','Maya Jasanoff',
                                            'Murari Kumar','Apaar Kumar','Pallavi Narayan','Tejaswini Niranjana',
                                            'Aparajith Ramnath', 'Rahul Sarwate','Shishir Saxena','Charu Singh',
                                            'Joseph Weelden','Guillaume Wadia','Mayank Aggarwal', 'Amrita Bihani', 'Jatin Christie','Vedant Dev',
                                            'Samvet Kuril','Kunal Mankodi','Siddhartha Saxena','Ekta Sharma',
                                            'Ramadhar Singh','Atul Kumar', 'Bijal Mehta', 'Ravi Miglani','Prithwiraj Mukherjee',
                                            'Darshana Padia','Mahendra Rao','Zalak Shah','Sujo Thomas',
                                            'Samyaday Choudhury', 'Soumen Ghosh', 'Gaurav Goswami','Raghwinder Grewal',
                                            'Kaushik Jana','Jitesh Jhawar','Pankaj Joshi','Eshita Mazumdar',
                                            'Sutapa Mukherji', 'Ashwin Pande','Pravakar Paul','Raghavan Rangarajan',
                                            'Manjil Saikia','Alok Shukla','Susanta Tewari','Aditya Vaishya',
                                            'Aditi Deo', 'Rajesh Naidu', 'Tejaswini Niranjana','Ranu Roychoudhuri',
                                            'Lakshmi Sreeram','Safwan Amir', 'Sarthak Bagchi', 'Urmi Biswas','Mary Chacko',
                                            'Suchismita Das','Aditi Deo','Nithin George','Darshini Mahadevia',
                                            'Leya Mathew', 'Mona Mehta','Keita Omi','Shilpa Pandit',
                                            'Chakravarthi Rangarajan','Maya Ratnam','Nagireddy Reddy','Rucha Sarwate',
                                            'Divita Singh','Ramadhar Singh','Bhargav Adhvaryu', 'Dinesh Barot', 'Vivek Bhatt','Pankaj Chandra',
                                            'Loyimee Gogoi','Amarlal Kalro','Jinal Parikh','Abhinandan Sinha',
                                            'Devanath Tirupati','Bhaktida Trivedi'],width=50, style="TCombobox")
    
    user.place(x=500, y=150)
    user.bind("<Key>", block_key_event)

    # Create the password entry fields
    def enter(e):
        password.delete(0, 'end')

    def leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'password')

    password = Entry(frame, width=25, fg='black', border=0, bg="lightblue", font=('Microsoft YaHei UI Light', 11))
    password.place(x=500, y=200)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', enter)
    password.bind('<FocusOut>', leave)

    Frame(frame, width=295, height=2, bg='black').place(x=500, y=220)

    # Create the confirm password entry fields
    def enter(e):
        passconfirm.delete(0, 'end')
    
    def leave(e):
        name = passconfirm.get()
        if name == '':
            passconfirm.insert(0, 'Confirm Password')
    
    passconfirm = Entry(frame, width=25, fg='black', border=0, bg="lightblue", font=('Microsoft YaHei UI Light', 11))
    passconfirm.place(x=500, y=250)
    passconfirm.insert(0, 'Confirm Password')
    passconfirm.bind('<FocusIn>', enter)
    passconfirm.bind('<FocusOut>', leave)
    
    Frame(frame, width=295, height=2, bg='black').place(x=500, y=270)

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

            c.execute("SELECT * FROM faculty WHERE username=?", (username,))
            result = c.fetchone()

            if result:
                messagebox.showerror("Error", "Username already exists")
            else:
                c.execute("INSERT INTO faculty (username, password) VALUES (?, ?)", (username, password_value))
                conn.commit()
                messagebox.showinfo("Success", "Account created successfully")

            conn.close()

    Button(frame, width=20, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=lambda: sign_up()).place(x=500, y=300)

# Function to display the feedback
def part3():
    def on_listbox_select(event):
        pass
    
    heading = Label(frame, text='FEEDBACK SYSTEM', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
    heading.place(x=310, y=5)

    listbox = Listbox(frame, width=83, height=16, font=('Microsoft YaHei UI Light', 12, 'bold'))
    listbox.bind('<<ListboxSelect>>', on_listbox_select)
    listbox.place(x=12, y=60)
    
    # Function to get the data from the database
    def get_data():     
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute("SELECT * FROM feedback WHERE faculty_name=?", (username_entered,))
        results = c.fetchall()
    
        if results:
            for result in results:
                listbox.insert(END, result)
        else:
            print("Faculty not found in the database")

    get_data()
    
root.mainloop()

