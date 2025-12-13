# Import Tkinter
from tkinter import *  

# Create window screen
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame 
frame = Frame(master=root, height=200, width=360, bg='#AEC6CF')

#add widgets
#add labels

lbl1 = Label(frame, text="Full Name🧑", bg="#ffd1dc", fg="#06A168", width=12)
lbl2 = Label(frame, text="Email ID📞", bg="#ffd1dc", fg="#048354", width=12)
lbl3 = Label(frame, text="Your Password📷", bg="#ffd1dc", fg="#04905D", width=12)

#Use entry widgets to get answers from the user
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

#Function to display message
def display():
    name = name_entry.get()
    email = email_entry.get()
    greet = "Hey " + name + " 😄"
    message = "\nYou have registared an account with the email id of " + email + " Congrats!🎉"
    textbox.insert(END, greet)
    textbox.insert(END, message)

#Textbox creation :-)
textbox = Text(bg="#FDFD96", fg="#9500FF")

#Button creation :-)
btn = Button(text="Create Account✅", command=display, bg="#FF746C", fg="#FFDFD3")

#arrange widgets
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()