import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from rembg import remove
from PIL import Image
import os

def upload_file():
    """Prompt the user to select an image file and process it."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        process_image(file_path)

def drop(event):
    """Handle the drag and drop event."""
    file_path = event.data
    if file_path:
        process_image(file_path.strip('{}'))

def process_image(file_path):
    """Process the image by removing its background and saving it."""
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if output_dir:
        output_file_name = simpledialog.askstring("Input", "Enter the output file name (without extension):")
        if output_file_name:
            output_path = os.path.join(output_dir, f"{output_file_name}.png")
            input_image = Image.open(file_path)
            output_image = remove(input_image)
            output_image.save(output_path)
            messagebox.showinfo("Success", f"Image saved to {output_path}")
            ask_another_image()

def ask_another_image():
    """Ask the user if they want to upload another image or exit."""
    response = messagebox.askyesno("Continue", "Do you want to upload another image?")
    if response:
        upload_file()
    else:
        root.quit()

# Create the main window
root = TkinterDnD.Tk()
root.title("Image Background Remover")
root.geometry("400x200")

# Create a label and buttons for file upload
tk.Label(root, text="Drag and drop an image or use the button below to upload:", wraplength=350).pack(pady=10)
tk.Button(root, text="Upload Image", command=upload_file).pack(pady=10)

# Enable dragging and dropping files
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Run the application
root.mainloop()
