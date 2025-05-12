import tkinter as tk
from datetime import datetime
import random

# === Global Variables ===
previous_keystroke_time = None


def check_idle():
    global previous_keystroke_time
    if previous_keystroke_time:
        gap = (datetime.now() - previous_keystroke_time).total_seconds()
        if gap > 5:
            print("Idle for too long. Clearing text...")
            text.delete("1.0", tk.END)
            label_result.config(text="")
            previous_keystroke_time = None  # Reset
        elif 3 <gap <5 :
            label_result.config(text="You have stopped typing.Text will clear in 1 second....")

    root.after(1000, check_idle)  # Check again in 1 second

# === First Key Detection ===
def on_keypress(event):
    global previous_keystroke_time
    previous_keystroke_time = datetime.now()


# === UI Setup ===
root = tk.Tk()
root.title("Dangerous typing")
root.geometry("720x420")
root.configure(bg="#f7f7f7")

# === Fonts and Styles ===
font_title = ("Helvetica", 12, "bold")
font_text = ("Consolas", 11)
font_result = ("Arial", 10)

# header label
header = tk.Label(root, text="Dangerous typing ", font=("Helvetica", 14, "bold"),
                  bg="#f7f7f7", fg="#2c3e50")
header.pack(pady=10)

# === Text Input ===
text = tk.Text(root, height=20, width=100, font=font_text, bd=2, relief="groove")
text.pack(pady=5)
text.bind("<Key>", on_keypress)

# === Result Label ===
label_result = tk.Label(root, text="", wraplength=480, justify="left",
                        font=font_result, bg="#f7f7f7", fg="#444")
label_result.pack(pady=10)



# === Result Label ===
label_result = tk.Label(root, text="", wraplength=480, justify="left",
                        font=font_result, bg="#f7f7f7", fg="#444")
label_result.pack(pady=10)



# Start the idle-check loop
root.after(1000, check_idle)
root.mainloop()