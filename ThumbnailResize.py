from tkinter import Tk, Label, Toplevel
from PIL import Image, ImageTk

def show_full_image(image_path):
    # Open the full-resolution image
    filedir = "/home/egoodwin/src/data/"
    full_image = Image.open(filedir + "AlphaFlight-078-00.jpg")

    # Create a new window for displaying the full-resolution image
    window = Toplevel()
    window.title("Full page")

    # Display the full-resolution image
    full_image_tk = ImageTk.PhotoImage(full_image)
    label = Label(window, image=full_image_tk)
    label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = full_image_tk

def show_thumbnail(image_path):
    # Open the thumbnail image
    thumbnail = Image.open(image_path)
    thumbnail.thumbnail((300, 300))  # Resize the thumbnail to fit in the window

    # Create the main window
    root = Tk()
    root.title("Thumbnail Image")

    # Display the thumbnail image
    thumbnail_tk = ImageTk.PhotoImage(thumbnail)
    label = Label(root, image=thumbnail_tk)
    label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = thumbnail_tk

    # Function to handle double-click event
    def double_click(event):
        show_full_image(image_path)

    # Bind double-click event to the label
    label.bind("<Double-Button-1>", double_click)

    # Start the main event loop
    root.mainloop()

# Usage example

img_file = "/home/egoodwin/src/data/AlphaFlight-078-00.jpg"
show_thumbnail(img_file)
