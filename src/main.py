import tkinter as tk
from tkinter import filedialog


print("Folder Scanner")
print("Select a folder to scan...")

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title="Select a folder")

print(f"Selected folder: {folder_path}")