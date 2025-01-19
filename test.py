import tkinter as tk

def on_mousewheel(event):
    text_widget.yview_scroll(-1 * int(event.delta / 120), "units")  # For Windows and macOS

root = tk.Tk()
root.title("Mouse Wheel Scrolling Example")

# Create a Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Text widget
text_widget = tk.Text(root, yscrollcommand=scrollbar.set, wrap="none")
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Attach the scrollbar to the Text widget
scrollbar.config(command=text_widget.yview)

# Bind the mouse wheel to scroll
root.bind("<MouseWheel>", on_mousewheel)  # Windows and macOS
root.bind("<Button-4>", on_mousewheel)    # Linux scroll up
root.bind("<Button-5>", on_mousewheel)    # Linux scroll down

# Populate the Text widget with sample text
for i in range(100):
    text_widget.insert(tk.END, f"This is line {i + 1}\n")

root.mainloop()
