import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Very Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Weak", fg="gold")
    elif length > 8 and length <= 10:
        result_label.config(text="Medium", fg="blue")
    elif length > 10 and length < 12:
        result_label.config(text="Strong", fg="green")
    else:  # length >= 12
        result_label.config(text="Very Strong", fg="dark green")


# Window
root = tk.Tk()
root.title("Password Checker")
root.geometry("350x220")
root.configure(bg="#F2F4FF")  # pastel lavender

# Title
title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 14, "bold"),
    bg="#F2F4FF",
    fg="#4A4A4A"
)
title.pack(pady=15)

# Entry
entry = tk.Entry(
    root,
    font=("Arial", 12),
    show="*",
    bg="#FFF1E6",   # pastel peach
    relief="flat"
)
entry.pack(pady=10, ipadx=10, ipady=5)

# Button
btn = tk.Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="#CDE7F0",   # pastel blue
    fg="#333333",
    relief="flat",
    font=("Arial", 11)
)
btn.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#F2F4FF"
)
result_label.pack(pady=10)

root.mainloop()
