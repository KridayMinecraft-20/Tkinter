import random
import tkinter as tk
from tkinter import messagebox


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "🤝 IT'S A TIE!! 🤝\nBoringgg... play again 🙄😴"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "🔥🎉 YOU WINNN!! 🎉🔥\nDat's how legends play 😎👑"
    else:
        return "🤖💀 MR. BOT WINS 💀🤖\nU got this, try again 🥺💪"


def play(user_choice):
    computer_choice = get_computer_choice()
    user_label.config(text=f"🧑 YOU = {user_choice.upper()} ✊📄✂️")
    bot_label.config(text=f"🤖 MR. BOT = {computer_choice.upper()} 🤖")
    result_label.config(text=determine_winner(user_choice, computer_choice))


root = tk.Tk()
root.title("🤖 Rock Paper Scissors — MR. BOT 🤖")
root.geometry("420x380")
root.resizable(False, False)

BG_COLOR = "#1E1E2E"
FG_COLOR = "#EAEAF0"
BTN_COLOR = "#6FA8DC"
BTN_ACTIVE = "#9FC5E8"

root.configure(bg=BG_COLOR)

title_label = tk.Label(
    root,
    text="🎮 WELCOME TO THE MIGHTIEST GAME 🎮\n"
         "✊📄✂️ ROCK • PAPER • SCISSORS ✂️📄✊\n"
         "🤖 (BTW my name is MR. BOT 🤖)",
    font=("Arial", 12, "bold"),
    justify="center",
    bg=BG_COLOR,
    fg=FG_COLOR
)
title_label.pack(pady=15)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

rock_btn = tk.Button(
    button_frame, text="✊ ROCK ✊", width=10,
    bg=BTN_COLOR, fg="black", activebackground=BTN_ACTIVE,
    command=lambda: play("rock")
)
paper_btn = tk.Button(
    button_frame, text="📄 PAPER 📄", width=10,
    bg=BTN_COLOR, fg="black", activebackground=BTN_ACTIVE,
    command=lambda: play("paper")
)
scissors_btn = tk.Button(
    button_frame, text="✂️ SCISSORS ✂️", width=10,
    bg=BTN_COLOR, fg="black", activebackground=BTN_ACTIVE,
    command=lambda: play("scissors")
)

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

user_label = tk.Label(
    root, text="🧑 YOU = ",
    font=("Arial", 11),
    bg=BG_COLOR, fg=FG_COLOR
)
user_label.pack(pady=5)

bot_label = tk.Label(
    root, text="🤖 MR. BOT = ",
    font=("Arial", 11),
    bg=BG_COLOR, fg=FG_COLOR
)
bot_label.pack(pady=5)

result_label = tk.Label(
    root, text="",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR, fg="#FFD966"
)
result_label.pack(pady=15)

exit_btn = tk.Button(
    root, text="🚪 EXIT 🚪",
    bg="#E06666", fg="white",
    activebackground="#F4CCCC",
    command=root.destroy
)
exit_btn.pack(pady=10)

root.mainloop()
