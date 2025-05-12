import tkinter as tk
from datetime import datetime
import random

# === Global Variables ===
previous_keystroke_time = None
# completion_time = None
# duration = None

# # === Reset Function ===
# def reset():
#     global first_keystroke_time, completion_time, duration
#     previous_keystroke_time = None
#     text.delete("1.0", tk.END)
#     label_result.config(text="Start typing again. End with '/' to finish.")

# === First Key Detection ===
def on_keypress(event):
    global previous_keystroke_time
    current_keystroke_time= datetime.now()
    if previous_keystroke_time is not None:
        gap= (current_keystroke_time-previous_keystroke_time).total_seconds()
        print(f"The gap between two characters was {gap}")

    else:
        print(f"First key '{event.char}' pressed at {current_keystroke_time}")

    previous_keystroke_time = current_keystroke_time



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




root.mainloop()