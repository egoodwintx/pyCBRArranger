import tkinter as tk
from tkinter import messagebox, filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        messagebox.showinfo("Open File", f"Selected file: {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        messagebox.showinfo("Save File", f"Saved file: {filepath}")

def about():
    messagebox.showinfo("About", "This is a sample program.")

# Create the main window
window = tk.Tk()
window.title("Menu and Gallery Example")

# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create the Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Create the gallery canvas
canvas = tk.Canvas(window, width=500, height=400)
canvas.pack()

# Load thumbnail images
thumbnails = [
    "thumbnail1.jpg",
    "thumbnail2.jpg",
    "thumbnail3.jpg",
    "thumbnail4.jpg",
    "thumbnail5.jpg"
]

# Display the thumbnails in a grid
num_columns = 3
thumbnail_width = 100
thumbnail_height = 100
padding = 10

row = 0
column = 0

for thumbnail in thumbnails:
    image = tk.PhotoImage(file=thumbnail).subsample(2)
    canvas.create_image(
        column * (thumbnail_width + padding),
        row * (thumbnail_height + padding),
        anchor=tk.NW,
        image=image
    )
    
    column += 1
    if column == num_columns:
        column = 0
        row += 1

# Start the main event loop
window.mainloop()
