import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

SETTINGS_FILE = "settings.json"

# Default categories
DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".ipynb"],
    "Executables": [".exe", ".msi", ".apk", ".bat", ".sh"],
    "Others": []
}


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_CATEGORIES.copy()


def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(FILE_CATEGORIES, f, indent=4)


# Load categories
FILE_CATEGORIES = load_settings()


class FileOrganizer:
    def __init__(self, folder, log_callback=None):
        self.folder = folder
        self.log_callback = log_callback

    def organize_files(self):
        if not os.path.exists(self.folder):
            return 0

        files_moved = 0
        for filename in os.listdir(self.folder):
            file_path = os.path.join(self.folder, filename)

            if os.path.isdir(file_path):
                continue

            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    self.move_file(file_path, category, filename)
                    files_moved += 1
                    moved = True
                    break

            if not moved:
                self.move_file(file_path, "Others", filename)
                files_moved += 1

        return files_moved

    def move_file(self, src, category, filename):
        category_folder = os.path.join(self.folder, category)
        os.makedirs(category_folder, exist_ok=True)

        dest = os.path.join(category_folder, filename)

        if os.path.exists(dest):
            base, ext = os.path.splitext(filename)
            i = 1
            while os.path.exists(dest):
                dest = os.path.join(category_folder, f"{base}_{i}{ext}")
                i += 1

        shutil.move(src, dest)

        if self.log_callback:
            self.log_callback(filename, category)


# Watchdog handler
class WatcherHandler(FileSystemEventHandler):
    def __init__(self, organizer):
        super().__init__()
        self.organizer = organizer

    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)
            self.organizer.organize_files()


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.folder_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.observer = None
        self.auto_mode = False

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="📂 File Organizer", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        frm = tk.Frame(self.root)
        frm.pack(pady=10)

        tk.Label(frm, text="Folder:").pack(side=tk.LEFT, padx=5)
        self.folder_entry = tk.Entry(frm, textvariable=self.folder_path, width=40, state="readonly")
        self.folder_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Browse", command=self.browse_folder).pack(side=tk.LEFT, padx=5)

        self.organize_btn = tk.Button(self.root, text="Organize Now", command=self.organize_now,
                                      bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.organize_btn.pack(pady=10)

        self.auto_btn = tk.Button(self.root, text="Start Auto Mode", command=self.toggle_auto_mode,
                                  bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.auto_btn.pack(pady=5)

        self.settings_btn = tk.Button(self.root, text="⚙ Settings", command=self.open_settings,
                                      bg="#9C27B0", fg="white", font=("Arial", 12, "bold"))
        self.settings_btn.pack(pady=5)

        self.log_tree = ttk.Treeview(self.root, columns=("File", "Category"), show="headings", height=12)
        self.log_tree.heading("File", text="File")
        self.log_tree.heading("Category", text="Category")
        self.log_tree.column("File", width=320)
        self.log_tree.column("Category", width=180)
        self.log_tree.pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def log_file(self, filename, category):
        self.log_tree.insert("", tk.END, values=(filename, category))

    def organize_now(self):
        organizer = FileOrganizer(self.folder_path.get(), log_callback=self.log_file)
        self.log_tree.delete(*self.log_tree.get_children())
        count = organizer.organize_files()
        messagebox.showinfo("Done", f"✅ {count} files organized successfully!")

    def toggle_auto_mode(self):
        if not self.auto_mode:
            self.start_auto_mode()
        else:
            self.stop_auto_mode()

    def start_auto_mode(self):
        folder = self.folder_path.get()
        if not os.path.exists(folder):
            messagebox.showerror("Error", "Folder does not exist.")
            return

        organizer = FileOrganizer(folder, log_callback=self.log_file)
        event_handler = WatcherHandler(organizer)
        self.observer = Observer()
        self.observer.schedule(event_handler, folder, recursive=False)
        self.observer_thread = threading.Thread(target=self.observer.start, daemon=True)
        self.observer_thread.start()

        self.auto_mode = True
        self.auto_btn.config(text="Stop Auto Mode", bg="#f44336")

    def stop_auto_mode(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()

        self.auto_mode = False
        self.auto_btn.config(text="Start Auto Mode", bg="#2196F3")

    def open_settings(self):
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings - File Categories")
        settings_win.geometry("500x400")

        tree = ttk.Treeview(settings_win, columns=("Category", "Extensions"), show="headings", height=12)
        tree.heading("Category", text="Category")
        tree.heading("Extensions", text="Extensions")
        tree.column("Category", width=150)
        tree.column("Extensions", width=300)
        tree.pack(pady=10)

        def refresh_tree():
            tree.delete(*tree.get_children())
            for cat, exts in FILE_CATEGORIES.items():
                tree.insert("", tk.END, values=(cat, ", ".join(exts)))

        def add_category():
            cat = simpledialog.askstring("New Category", "Enter category name:", parent=settings_win)
            if cat and cat not in FILE_CATEGORIES:
                FILE_CATEGORIES[cat] = []
                save_settings()
                refresh_tree()

        def delete_category():
            selected = tree.selection()
            if not selected:
                return
            cat = tree.item(selected[0])["values"][0]
            if cat in FILE_CATEGORIES and cat != "Others":
                del FILE_CATEGORIES[cat]
                save_settings()
                refresh_tree()

        def add_extension():
            selected = tree.selection()
            if not selected:
                return
            cat = tree.item(selected[0])["values"][0]
            ext = simpledialog.askstring("Add Extension", "Enter file extension (e.g. .xyz):", parent=settings_win)
            if ext and not ext.startswith("."):
                ext = "." + ext
            if ext and cat in FILE_CATEGORIES:
                if ext not in FILE_CATEGORIES[cat]:
                    FILE_CATEGORIES[cat].append(ext.lower())
                save_settings()
                refresh_tree()

        def remove_extension():
            selected = tree.selection()
            if not selected:
                return
            cat = tree.item(selected[0])["values"][0]
            exts = FILE_CATEGORIES.get(cat, [])
            if not exts:
                return
            ext = simpledialog.askstring("Remove Extension", f"Enter extension to remove from {cat}:", parent=settings_win)
            if ext and ext in exts:
                FILE_CATEGORIES[cat].remove(ext)
                save_settings()
                refresh_tree()

        btn_frame = tk.Frame(settings_win)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Category", command=add_category, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete Category", command=delete_category, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Add Extension", command=add_extension, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Remove Extension", command=remove_extension, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)

        refresh_tree()


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
