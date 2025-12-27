from tkinter import *

root = Tk()
root.title("Inches to centimeters converter")
root.geometry("450x350")
root.config(bg="#FFF6CC") 


title = Label(
    root,
    text="Inches --> Centimeters",
    font=("Comic Sans MS", 18, "bold"),
    bg="#4C97FF",
    fg="white",
    padx=20,
    pady=10
)
title.pack()

# Frame (Scratch block style)
frame = Frame(root, bg="#96CCFF", width=360, height=180)
frame.pack(pady=10)

# Labels
lbl1 = Label(
    frame,
    text="Inches 📏",
    font=("Comic Sans MS", 12, "bold"),
    bg="#FFD500",
    fg="black",
    width=14
)

lbl2 = Label(
    frame,
    text="Centimeters 📐",
    font=("Comic Sans MS", 12, "bold"),
    bg="#FFD500",
    fg="black",
    width=14
)

lbl1.place(x=30, y=30)
lbl2.place(x=30, y=90)

# Entry widgets
inch_entry = Entry(frame, font=("Comic Sans MS", 12), width=15, bd=3)
cm_entry = Entry(frame, font=("Comic Sans MS", 12), width=15, bd=3)

inch_entry.place(x=190, y=30)
cm_entry.place(x=190, y=90)

# Convert function
def convert():
    cm_entry.delete(0, END)
    try:
        inches = float(inch_entry.get())
        cm = inches * 2.54
        cm_entry.insert(0, round(cm, 2))
    except:
        cm_entry.insert(0, "Oops!")

# Button (Scratch green)
btn = Button(
    root,
    text="Convert 🟢",
    font=("Comic Sans MS", 14, "bold"),
    bg="#00C853",
    fg="white",
    activebackground="#00E676",
    width=16,
    bd=0
)
btn.config(command=convert)
btn.pack(pady=15)

root.mainloop()
