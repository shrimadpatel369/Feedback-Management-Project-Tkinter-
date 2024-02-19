from tkinter import *
from subprocess import call

# Create the main window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Create a frame inside the window
frame = Frame(root, width=850, height=380, bg="lightblue")
frame.place(x=40, y=50)

# Create a heading label
heading = Label(frame, text='FEEDBACK SYSTEM', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=310, y=5)

# Function to open the faculty feedback form
def open(old_root):
    old_root.destroy()
    call(["python", "F:/AU/SEM 3/CSE 100/Project - final/feedback/gict faculty.py"])

# Button to open the faculty feedback form and exit the current window
b1 = Button(frame, text='faculty', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 15), command=lambda: open(root))
b1.place(x=120, y=180)

b2 = Button(frame, text='Exit', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 15), command=root.destroy)
b2.place(x=480, y=180)

# Start the main event loop
root.mainloop()