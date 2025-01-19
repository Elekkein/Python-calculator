import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#f0f0f0")

# Entry widget to display the current equation
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", bg="#ffffff", fg="#333333")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Colors for buttons
button_colors = {
    "C": "#ff6666",
    "=": "#66b3ff",
    "+": "#ffd966",
    "-": "#ffd966",
    "*": "#ffd966",
    "/": "#ffd966",
}

def get_button_color(text):
    return button_colors.get(text, "#e6e6e6")

# Create and place buttons in the window
for (text, row, col) in buttons:
    button = tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 18),
        bg=get_button_color(text),
        fg="#333333",
        activebackground="#d9d9d9",
        command=lambda t=text: on_click(t)
    )
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
