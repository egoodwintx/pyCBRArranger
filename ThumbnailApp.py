import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ThumbnailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thumbnail Gallery")
        
        # Create a canvas
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        
        # List to store the images
        self.images = []
        
        # Create an index counter for logical sequence names
        self.index = 1
        
        # Allow dropping files onto the canvas
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_drop)
        
    def on_drag(self, event):
        # Get the current dragged image
        current_image = self.images[-1]
        self.canvas.coords(current_image, event.x, event.y)
        
    def on_drop(self, event):
        # Get the file path of the dropped image
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png")])
        
        # Check if a file was selected
        if file_path:
            # Open the image using PIL
            image = Image.open(file_path)
            
            # Resize the image to fit within the canvas
            if image.width > 200 or image.height > 200:
                image.thumbnail((200, 200))
            
            # Convert the image to Tkinter-compatible format
            tk_image = ImageTk.PhotoImage(image)
            
            # Create a label on the canvas with the image
            image_label = self.canvas.create_image(event.x, event.y, image=tk_image, anchor=tk.NW)
            
            # Store the image label in the list
            self.images.append(image_label)
            
            # Update the canvas
            self.canvas.update()
        
    def save_images(self):
        # Create a directory for the saved images
        directory = filedialog.askdirectory()
        if directory:
            for i, image_label in enumerate(self.images):
                # Get the original file extension
                file_extension = os.path.splitext(filedialog.askopenfilename())[1]
                
                # Generate the logical sequence name
                sequence_name = f"file{i+1:03}{file_extension}"
                
                # Get the image from the canvas
                image = self.canvas.itemcget(image_label, "image")
                
                # Save the image with the logical sequence name
                image.save(os.path.join(directory, sequence_name))
                
            # Display a message after saving
            messagebox.showinfo("Images Saved", "Images saved successfully!")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ThumbnailApp(root)
    
    # Create a button to save the images
    save_button = tk.Button(root, text="Save Images", command=app.save_images)
    save_button.pack()
    
    root.mainloop()
