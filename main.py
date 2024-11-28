import tkinter as tk
from tkinter import filedialog
import os

class ImgToPDFConv:

    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text = "Image to PDF Converter", font = ("Times New Roman", 20, "bold"))
        title_label.pack(pady = 10)

        Select_Img_btn = tk.Button(self.root, text="Please Select any images", command = self.select_images))
        Select_Img_btn.pack(pady = (0, 10))

        self.selected_images_listbox.pack(pady =(0, 10), fill = tk.BOTH, expand = True)

        label = tk.Label(self.root, text = "Enter the name for the new PDF file: ")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width= 40, justify= 'center')
        pdf_name_entry.pack()

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    converter = ImgToPDFConv(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()