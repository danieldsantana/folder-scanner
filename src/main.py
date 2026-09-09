import tkinter as tk
from tkinter import filedialog

def choose_scan_type():
    print("\nWhat do you want to scan?")
    print("1. Folders")
    print("2. Files")
    print("3. Folders and files")
    print("4. Exit")

    while True:
        option = input("Select an option: ")

        if option in ("1", "2", "3", "4"):
            return option

        print("Invalid option. Please choose 1, 2, 3 or 4.")

print("Folder Scanner")
print("Select a folder to scan...")

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title="Select a folder")

print(f"Selected folder: {folder_path}")

scan_type = choose_scan_type()
print(f"Selected scan type: {scan_type}")