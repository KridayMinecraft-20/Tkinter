from tkinter import *

root = Tk()

root.geometry("300x400")
root.title("Multiply Two Numbers")

lbl = Label(text="Enter Two Numbers", fg="white", bg="#25EFC7", height=1, width=300)

num1_lbl = Label(text="First Number:", bg="#69E928")
num1_entry = Entry()

num2_lbl = Label(text="Second Number:", bg="#69E928")
num2_entry = Entry()

def multiply():
    try:
        n1 = float(num1_entry.get())
        n2 = float(num2_entry.get())
        product = n1 * n2

        text_box.delete("1.0", END)     # Clear previous output
        text_box.insert(END, f"Product = {product}")
    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Please enter valid numbers!")

text_box = Text(height=3)

btn = Button(text="Multiply", command=multiply, height=1, bg="#a22e00", fg="white")

lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
