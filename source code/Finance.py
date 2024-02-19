from tkinter import *
from tkinter import ttk
from feedbackdatabase import create_table, save_feedback

# Create the main window
root = Tk()
root.title('Feedback System')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Create a frame inside the window
frame = Frame(root, width=850, height=470, bg="lightblue")
frame.place(x=40, y=20)

# Create a heading label
heading = Label(frame, text='FEEDBACK SYSTEM', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=310, y=5)

# Labels for input fields
Label_name = Label(frame, text="Name of the Faculty", width=45, fg='black', border=0, bg="white",font=('Microsoft YaHei UI Light', 11))
Label_name.place(x=20, y=80)
Label_satisfaction = Label(frame, text="How satisfied are you with the faculty's teaching style?", width=45, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light', 11))
Label_satisfaction.place(x=20, y=140)
Label_clear_explanations = Label(frame, text="Did the faculty provide clear explanations?", width=45, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light', 11))
Label_clear_explanations.place(x=20, y=200)
Label_engagement = Label(frame, text="How well did the faculty engage with students?", width=45, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light', 11))
Label_engagement.place(x=20, y=260)
Label_organization = Label(frame, text="Rate the overall organization of the course materials.", width=45, fg='black',border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
Label_organization.place(x=20, y=320)
Label_comments = Label(frame, text="Do you have any additional comments or suggestions?", width=45, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light', 11))
Label_comments.place(x=20, y=380)

# Combobox for faculty selection
style = ttk.Style()
style.configure("TCombobox", foreground='black', font=('Microsoft YaHei UI Light', 11))

def block_key_event(event):
    return "break"

entry_faculty = ttk.Combobox(frame, values=['Poonam Dugar', 'Tanya Jain', 'Prateek Jain','Hetal Jhaveri',
                                            'Vaibhav Kadia','Narendra Kushwaha','Vinodh Madhavan','Parag Patel',
                                            'Binny Rawat','Kinshuk Saurabh','Saumil Shah','Nimit Thaker',
                                            'Vibha Tripathi'],width=50, style="TCombobox")
entry_faculty.place(x=500, y=80)
entry_faculty.bind("<Key>", block_key_event)

# Radio buttons for satisfaction level
var = IntVar()

Entry_satisfaction = Radiobutton(root, text="1", variable=var, value=1)
Entry_satisfaction.place(x=538, y=158)
Entry_satisfaction = Radiobutton(root, text="2", variable=var, value=2)
Entry_satisfaction.place(x=600, y=158)
Entry_satisfaction = Radiobutton(root, text="3", variable=var, value=3)
Entry_satisfaction.place(x=662, y=158)
Entry_satisfaction = Radiobutton(root, text="4", variable=var, value=4)
Entry_satisfaction.place(x=724, y=158)
Entry_satisfaction = Radiobutton(root, text="5", variable=var, value=5)
Entry_satisfaction.place(x=786, y=158)

# Entry fields for other feedback parameters
Entry_clear_explanations = Entry(frame, width=40, fg='black', border=0, bg="white",font=('Microsoft YaHei UI Light', 11))
Entry_clear_explanations.place(x=500, y=200)
Entry_engagement = Entry(frame, width=40, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
Entry_engagement.place(x=500, y=260)

# Radio buttons for organization rating
var1 = IntVar()

Entry_organization = Radiobutton(root, text="1", variable=var1, value=1)
Entry_organization.place(x=538, y=340)
Entry_organization = Radiobutton(root, text="2", variable=var1, value=2)
Entry_organization.place(x=600, y=340)
Entry_organization = Radiobutton(root, text="3", variable=var1, value=3)
Entry_organization.place(x=662, y=340)
Entry_organization = Radiobutton(root, text="4", variable=var1, value=4)
Entry_organization.place(x=724, y=340)
Entry_organization = Radiobutton(root, text="5", variable=var1, value=5)
Entry_organization.place(x=786, y=340)

# Entry fields for other feedback parameters
Entry_comments = Entry(frame, width=40, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
Entry_comments.place(x=500, y=380)

# Function to handle the save feedback button click event
def save_feedback_handler():
    faculty_name = entry_faculty.get()
    satisfaction = var.get()
    clear_explanations = Entry_clear_explanations.get()
    engagement = Entry_engagement.get()
    organization = var1.get()
    comments = Entry_comments.get()

    save_feedback(faculty_name, satisfaction, clear_explanations, engagement, organization, comments)

    # Clearing the input fields
    entry_faculty.set('')
    Entry_satisfaction.deselect()
    Entry_clear_explanations.delete(0, END)
    Entry_engagement.delete(0, END)
    Entry_organization.deselect()
    Entry_comments.delete(0, END)
    
# Save feedback button
save_button = Button(frame, width=20, pady=7, text='Save Feedback', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 11, 'bold'), command=save_feedback_handler)
save_button.place(x=250, y=430)

# Exit button
exit_button = Button(frame, width=20, pady=7, text='exit', bg='#57a1f8', fg='white', border=0,font=('Microsoft YaHei UI Light', 11, 'bold'), command=root.destroy)
exit_button.place(x=500, y=430)

# Start the main event loop
root.mainloop()
