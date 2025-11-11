import tkinter as tk
from tkinter import messagebox, filedialog

# --- Function to merge lists ---
def merge_lists():
    list1_input = entry1.get()
    list2_input = entry2.get()

    if not list1_input or not list2_input:
        messagebox.showwarning("Input Error", "Please enter both lists!")
        return

    # Convert comma-separated text into lists
    list1 = [item.strip() for item in list1_input.split(",") if item.strip()]
    list2 = [item.strip() for item in list2_input.split(",") if item.strip()]

    # Combine lists
    merged = list1 + list2

    # Normalize (make all lowercase for comparison)
    seen = set()
    final_list = []
    for item in merged:
        lower_item = item.lower()
        if lower_item not in seen:
            seen.add(lower_item)
            # Capitalize first letter for neatness
            final_list.append(item.capitalize())

    # Sort alphabetically (case-insensitive)
    final_list.sort(key=lambda x: x.lower())

    # Store for later saving
    global last_result
    last_result = final_list

    # Show merged, sorted list
    result_var.set(", ".join(final_list))


# --- Function to save merged list to file ---
def save_to_file():
    global last_result
    if not last_result:
        messagebox.showwarning("No Data", "Please merge the lists first before saving.")
        return

    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Merged List As"
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(last_result))
            messagebox.showinfo("Success", f"Merged list saved successfully to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")


# --- GUI Setup ---
root = tk.Tk()
root.title("List Merger")
root.geometry("400x430")
root.resizable(False, False)
root.configure(bg="#f3f3f3")

last_result = []  # holds the latest merged list

# --- Title ---
title = tk.Label(
    root,
    text="List Merger Program",
    font=("Arial", 18, "bold"),
    bg="#f3f3f3"
)
title.pack(pady=10)

# --- List 1 Input ---
lbl1 = tk.Label(root, text="Enter first list (comma-separated):", bg="#f3f3f3", font=("Arial", 12))
lbl1.pack()
entry1 = tk.Entry(root, font=("Arial", 12), width=40, bd=3, relief="sunken")
entry1.pack(pady=5)

# --- List 2 Input ---
lbl2 = tk.Label(root, text="Enter second list (comma-separated):", bg="#f3f3f3", font=("Arial", 12))
lbl2.pack()
entry2 = tk.Entry(root, font=("Arial", 12), width=40, bd=3, relief="sunken")
entry2.pack(pady=5)

# --- Buttons Frame ---
btn_frame = tk.Frame(root, bg="#f3f3f3")
btn_frame.pack(pady=10)

# --- Merge Button ---
btn_merge = tk.Button(
    btn_frame,
    text="Merge Lists",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    relief="raised",
    bd=3,
    command=merge_lists
)
btn_merge.pack(side="left", padx=5)

# --- Save Button ---
btn_save = tk.Button(
    btn_frame,
    text="Save to File",
    font=("Arial", 13, "bold"),
    bg="#2196F3",
    fg="white",
    relief="raised",
    bd=3,
    command=save_to_file
)
btn_save.pack(side="left", padx=5)

# --- Result Display ---
result_var = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result_var,
    wraplength=350,
    justify="left",
    bg="#e6ffe6",
    fg="#333",
    font=("Arial", 12),
    bd=2,
    relief="groove",
    padx=10,
    pady=10
)
result_label.pack(pady=10)

# --- Footer ---
footer = tk.Label(
    root,
    text="© Copyright Aime Wyatt",
    font=("Arial", 10, "italic"),
    fg="gray",
    bg="#f3f3f3"
)
footer.pack(side="bottom", fill="x", pady=5)

# --- Run App ---
root.mainloop()
