from tkinter import *
from subprocess import call

# Create the main window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Place the logo on the window
img = PhotoImage(file='F:/AU/SEM 3/CSE 100/project/logo.png')
Label(root, image=img, bg='white').place(x=120, y=120)

# Create a frame inside the window
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

# Create a heading label
heading = Label(frame, text='FEEDBACK SYSTEM', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=50, y=5)

# Function to open the faculty section window and destroy the current window
def open1(old_root):
    old_root.destroy() 
    call(["python", "faculty.py"])

# Function to open the student section window and destroy the current window
def open2(old_root):
    old_root.destroy() 
    call(["python", "student.py"])
 
# Create buttons to open faculty and student sections  
faculty = Button(frame, text='Faculty', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 11), command=lambda: open1(root))
faculty.place(x=80, y=90)

student = Button(frame, text='Student', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 11), command=lambda: open2(root))
student.place(x=80, y=170)

# Start the main event loop
root.mainloop()





