import tkinter as tk
from tkinter import messagebox

# --- Functions ---
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            screen_var.set("")
    elif text == "C":
        screen_var.set("")
    elif text == "DEL":
        current = screen_var.get()
        screen_var.set(current[:-1])  # remove last character
    else:
        screen_var.set(screen_var.get() + text)


# --- Window Setup ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x420")
root.resizable(False, False)

# --- Input Field ---
screen_var = tk.StringVar()
screen = tk.Entry(
    root,
    textvar=screen_var,
    font=("Arial", 22),
    justify="right",
    bd=8,
    relief="sunken",
    bg="#f3f3f3"
)
screen.pack(fill="both", ipadx=8, ipady=10, pady=10)

# --- Buttons Layout ---
buttons = [
    ["C", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

frame = tk.Frame(root, bg="#ddd")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#ddd")
    row_frame.pack(pady=2)
    for text in row:
        btn = tk.Button(
            row_frame,
            text=text,
            font=("Arial", 18, "bold"),
            width=5,
            height=2,
            bg="#f0f0f0",
            relief="raised",
            bd=2
        )
        btn.pack(side="left", padx=3, pady=3)
        btn.bind("<Button-1>", click)

# --- Start App ---
root.mainloop()
