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

# Function to open the cultural and heritage feedback form
def open(old_root):
    old_root.destroy()
    call(["python", "cultural.py"])

# Function to open the communication feedback form
def open1(old_root):
    old_root.destroy()
    call(["python", "communication.py"])

# Function to open the economics and public policy feedback form
def open2(old_root):
    old_root.destroy()
    call(["python", "economics.py"])

# Function to open the entrepreneurship feedback form
def open3(old_root):
    old_root.destroy()
    call(["python", "Entrepreneurship.py"])

# Function to open the environment and sustainability feedback form
def open4(old_root):
    old_root.destroy()
    call(["python", "Environment.py"])

# Function to open the finance and accounts feedback form
def open5(old_root):
    old_root.destroy()
    call(["python", "Finance.py"])

# Function to open the management and organisation feedback form
def open6(old_root):
    old_root.destroy()
    call(["python", "Management.py"])

# Function to open the marketing feedback form
def open7(old_root):
    old_root.destroy()
    call(["python", "Marketing.py"])

# Function to open the technology and decision science feedback form
def open8(old_root):
    old_root.destroy()
    call(["python", "Technology.py"])  

# Create buttons for each feedback form
b1 = Button(frame, text='Cultural and heritage', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open(root))
b1.place(x=20, y=100)

b2 = Button(frame, text='Communication', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open1(root))
b2.place(x=320, y=100)

b3 = Button(frame, text='Economics and Public policy', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open2(root))
b3.place(x=600, y=100)

b4 = Button(frame, text='Entrepreneurship', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open3(root))
b4.place(x=20, y=170)

b5 = Button(frame, text='Environment and sustainability', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open4(root))
b5.place(x=320, y=170)

b6 = Button(frame, text='Finance and Accounts', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open5(root))
b6.place(x=600, y=170)

b7 = Button(frame, text='Management and Organisation', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open6(root))
b7.place(x=20, y=240)

b8 = Button(frame, text='Marketing', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open7(root))
b8.place(x=320, y=240)

b9 = Button(frame, text='Technology&decision science', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=lambda: open8(root))
b9.place(x=600, y=240)

b10 = Button(frame, text='Exit', width=25, fg='black', border=0, bg="tan", font=('Microsoft YaHei UI Light', 12), command=root.destroy)
b10.place(x=20, y=310)

# Start the main event loop
root.mainloop()