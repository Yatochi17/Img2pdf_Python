import tkinter as tk
from tkinter import filedialog
import os

class ImgToPDFConv:

    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()