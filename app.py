import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import os

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")


        # Bind keyboard events
        self.root.bind_all('<Left>', self.prev_image)
        self.root.bind_all('<Right>', self.next_image)

        #button to load folder
        self.load_button = tk.Button(self.root, text="Browse Folder", command=self.load_folder)
        self.load_button.pack()

        # Initialize image list and index
        self.image_files = []
        self.current_image_index = 0

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_files = []
            for f in os.listdir(folder_path):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.raw', '.psd', '.eps', '.svg',
                                       '.exr', '.heif')):
                    self.image_files.append(os.path.join(folder_path, f))
            if self.image_files:
                self.current_image_index = 0
                self.display_image(self.image_files[self.current_image_index])

    def display_image(self, file_path):
        img = cv2.imread(file_path)
        if hasattr(self, "label"):
            self.label.pack_forget() 
        img = Image.fromarray(img)  
        i = ImageTk.PhotoImage(img)
        self.label = tk.Label(image=i)
        self.label.image = i
        self.label.pack()


    def prev_image(self, event=None):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.display_image(self.image_files[self.current_image_index])

    def next_image(self, event=None):
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.display_image(self.image_files[self.current_image_index])


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.focus_set()
    root.mainloop()
    cv2.destroyAllWindows()