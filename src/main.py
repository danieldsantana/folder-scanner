import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import sys


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".idea",
    ".vscode",
}


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


def build_tree(folder_path, include_files=False):
    root_path = Path(folder_path)

    # Use a fallback name for filesystem roots such as C:\.
    root_name = root_path.name or str(root_path)

    lines = [root_name]

    def add_directory(directory, prefix=""):
        try:
            entries = []

            for entry in directory.iterdir():
                if entry.is_symlink():
                    continue

                if entry.is_dir():
                    if entry.name not in IGNORED_DIRECTORIES:
                        entries.append(entry)

                elif include_files and entry.is_file():
                    entries.append(entry)

        except PermissionError:
            lines.append(prefix + "└── [Access denied]")
            return

        entries.sort(key=lambda path: (path.is_file(), path.name.lower()))

        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1

            if is_last:
                connector = "└── "
            else:
                connector = "├── "

            name = entry.name

            if entry.is_dir():
                name += "/"

            lines.append(prefix + connector + name)

            if entry.is_dir():
                if is_last:
                    new_prefix = prefix + "    "
                else:
                    new_prefix = prefix + "│   "

                add_directory(entry, new_prefix)

    add_directory(root_path)

    return lines


def save_tree(lines, folder_path):
    script_directory = Path(__file__).resolve().parent
    output_folder = script_directory.parent / "output"
    output_folder.mkdir(exist_ok=True)

    folder_name = Path(folder_path).name or Path(folder_path).anchor
    output_file = output_folder / f"{folder_name}_tree.txt"

    counter = 1

    while output_file.exists():
        output_file = output_folder / f"{folder_name}_tree_{counter}.txt"
        counter += 1

    output_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"\nTree saved to: {output_file}")


def scan_folders(folder_path):
    lines = build_tree(folder_path, include_files=False)

    for line in lines:
        print(line)

    save_tree(lines, folder_path)


def scan_folders_and_files(folder_path):
    lines = build_tree(folder_path, include_files=True)

    for line in lines:
        print(line)

    save_tree(lines, folder_path)


def exit_program():
    print("Exiting program")
    sys.exit()


print("Folder Scanner")
print("Select a folder to scan...")

tk_root = tk.Tk()
tk_root.withdraw()

folder_path = filedialog.askdirectory(title="Select a folder")

if not folder_path:
    exit_program()

print(f"Selected folder: {folder_path}")

scan_type = choose_scan_type()

if scan_type == "1":
    scan_folders(folder_path)

elif scan_type == "2":
    scan_folders_and_files(folder_path)

elif scan_type == "3":
    exit_program()