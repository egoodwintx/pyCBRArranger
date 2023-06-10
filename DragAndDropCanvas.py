import tkinter as tk
import tkinterdnd2 as tkdnd

filedir = "/home/egoodwin/src/data/"

# Create a list of image paths
image_paths = [
    filedir + "AlphaFlight-078-00.jpg",
    filedir + "AlphaFlight-078-01.jpg",
    filedir + "AlphaFlight-078-02.jpg"
]

def on_drop(event):
    # Get the dropped data (image path)
    path = event.data
    
    # Create an image on the canvas at the drop position
    canvas.create_image(event.x, event.y, image=tk.PhotoImage(file=path), anchor=tk.NW)
    canvas.update()
    
root = tk.Tk()

# Create a canvas with tkinterdnd2's DND_DROP target
canvas = tkdnd.DragSource(root, "image")
canvas.drop_target_register(tkdnd.DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)


# Add the canvas to the root window
canvas.pack()

# Load and display the thumbnail images on the canvas
for path in image_paths:
    img = tk.PhotoImage(file=path)
    canvas.create_image(10, 10, image=img, anchor=tk.NW)
    canvas.update()

root.mainloop()
