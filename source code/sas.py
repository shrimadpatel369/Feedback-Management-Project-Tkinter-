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

# Function to open the biology and life science feedback form
def open(old_root):
    old_root.destroy()
    call(["python", "biology.py"])

# Function to open the humanities and language feedback form
def open1(old_root):
    old_root.destroy()
    call(["python", "humanities.py"])

# Function to open the mathematical and physical science feedback form
def open2(old_root):
    old_root.destroy()
    call(["python", "mathemathics.py"])

# Function to open the performing and visual arts feedback form
def open3(old_root):
    old_root.destroy()
    call(["python","pva.py"])

# Function to open the social science feedback form
def open4(old_root):
    old_root.destroy()
    call(["python", "social science.py"])

# create buttons to open the feedback forms   
b1 = Button(frame, text='Biology and life science', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open(root))
b1.place(x=20, y=100)

b2 = Button(frame, text='Humanitites and language', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open1(root))
b2.place(x=320, y=100)

b3 = Button(frame, text='Mathematical&Physical science', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open2(root))
b3.place(x=600, y=100)

b4 = Button(frame, text='Performing and visual arts', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open3(root))
b4.place(x=20, y=170)

b5 = Button(frame, text='social sciences', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open4(root))
b5.place(x=320, y=170)

b6 = Button(frame, text='Exit', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=root.destroy)
b6.place(x=600, y=170)

# Start the main event loop
root.mainloop()