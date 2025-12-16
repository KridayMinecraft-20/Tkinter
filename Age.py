# Import Tkinter and datetime
from tkinter import *
from datetime import date

# Create window screen
root = Tk()
root.title('Age Calculator App')
root.geometry('420x450')

# Create a frame
frame = Frame(master=root, height=260, width=380, bg="#FFD1DC")

# Labels
lbl1 = Label(frame, text="Full Name 🧑", bg="#B0E0E6", fg="#04905D", width=15)
lbl2 = Label(frame, text="Birth Year 📅", bg="#B0E0E6", fg="#04905D", width=15)
lbl3 = Label(frame, text="Birth Month 📆", bg="#B0E0E6", fg="#04905D", width=15)
lbl4 = Label(frame, text="Birth Day 📌", bg="#B0E0E6", fg="#04905D", width=15)

# Entry widgets
name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
day_entry = Entry(frame)

# Function to calculate age
def calculate_age():
    textbox.delete("1.0", END)

    name = name_entry.get()
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())

    today = date.today()
    birth_date = date(year, month, day)

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    message = (
        f"Hello {name} 😄\n\n"
        f"Your Date of Birth: {day}/{month}/{year}\n"
        f"Your Age is: {age} years 🎉"
    )

    textbox.insert(END, message)

# Textbox
textbox = Text(bg="#D0F0C0", fg="#A1A1E7", height=7, width=45)

# Button
btn = Button(
    text="Calculate Age ✅",
    command=calculate_age,
    bg="#FFDFD3",
    fg="#3A4909",
    width=18
)

# Arrange widgets
frame.place(x=20, y=10)

lbl1.place(x=20, y=20)
name_entry.place(x=180, y=20)

lbl2.place(x=20, y=70)
year_entry.place(x=180, y=70)

lbl3.place(x=20, y=120)
month_entry.place(x=180, y=120)

lbl4.place(x=20, y=170)
day_entry.place(x=180, y=170)

btn.place(x=140, y=280)
textbox.place(x=20, y=330)

root.mainloop()
