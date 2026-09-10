import tkinter as tk
from tkinter import filedialog


def choose_scan_type():
    print("\nWhat do you want to scan?")
    print("1. Only folders")
    print("2. Folders and files")
    print("3. Exit")

    while True:
        option = input("Select an option: ")

        if option in ("1", "2", "3"):
            return option

        print("Invalid option. Please choose 1, 2 or 3.")


def scan_folders(folder_path):
    print("scan_folders")


def scan_folders_and_files(folder_path):
    print("scan_folders_and_files")


def exit_program():
    print("Exiting program")
    exit()


print("Folder Scanner")
print("Select a folder to scan...")

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title="Select a folder")

print(f"Selected folder: {folder_path}")

scan_type = choose_scan_type()

if scan_type == "1":
    scan_folders(folder_path)

elif scan_type == "2":
    scan_folders_and_files(folder_path)

elif scan_type == "3":
    exit_program()