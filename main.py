import tkinter as tk
from datetime import datetime
import random

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






root.mainloop()