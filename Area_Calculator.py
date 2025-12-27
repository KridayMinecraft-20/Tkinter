from tkinter import *

def calculate_area():
    try:
        side = float(inputSide.get())
        area = side * side
        lblAns.config(text=str(area) + " cm²")
    except ValueError:
        lblAns.config(text="Invalid input!")

root = Tk()
root.title("Square's Area Calculator")
root.geometry("450x350")
root.config(bg="#02f4d4")

titleLBL = Label(
    root,
    text="Find the area of a square!",
    font=("Jokerman", 22),
    fg="#02f4d4",
    bg="#3f22c0"
)
titleLBL.pack(pady=15)

frame = Frame(root, bg="#FD8B00", width=400, height=230)
frame.pack(pady=15)
frame.place(relx=0.5, rely=0.55, anchor=CENTER)

lblSQUARE = Label(
    frame,
    bg="#FD8B00",
    fg="#02f4d4",
    text="Square's side in cm 📐🟦",
    font=("Kristen ITC", 12)
)
lblSQUARE.place(x=30, y=40)

inputSide = Entry(
    frame,
    font=("Comic Sans MS", 12),
    width=15,
    bg="#FEB75F",
    fg="#02f4d4",
    bd=3
)
inputSide.place(x=230, y=40)

btnCalc = Button(
    frame,
    text="Calculate Area ✨",
    font=("Comic Sans MS", 12),
    bg="#3f22c0",
    fg="white",
    command=calculate_area
)
btnCalc.place(x=120, y=90)

lblSquareArea = Label(
    frame,
    bg="#FD8B00",
    fg="#02f4d4",
    text="Square's area is:",
    font=("Kristen ITC", 12)
)
lblSquareArea.place(x=30, y=150)

lblAns = Label(
    frame,
    bg="#FEB75F",
    fg="#3f22c0",
    text="...",
    font=("Kristen ITC", 12),
    width=12,
    bd=3,
)
lblAns.place(x=230, y=150)

root.mainloop()
