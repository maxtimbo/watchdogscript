import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import messagebox
import os

class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.folder_source_txt_var = tk.StringVar()
        self.folder_destination_txt_var = tk.StringVar()
        self.current_dir = os.getcwd()

        self.folder_view = ttk.Frame(parent)
        self.folder_view.grid(row=0, column=0)

        self.folder_source_label = ttk.Label(self.folder_view, text="Source Folder: ")
        self.folder_source_display = ttk.Entry(self.folder_view, width=36, textvariable=self.folder_source_txt_var)
        self.folder_source_select = ttk.Button(self.folder_view, width=26, text="Select Source", command=self.folder_source_select_on_click)

        self.folder_source_label.grid(row=0, column=0, padx=5, pady=5, sticky="ne")
        self.folder_source_display.grid(row=0, column=1, padx=5, pady=5, sticky="ne")
        self.folder_source_select.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

        self.folder_destination_label = ttk.Label(self.folder_view, text="Destination Folder: ")
        self.folder_destination_display = ttk.Entry(self.folder_view, width=36, textvariable=self.folder_destination_txt_var)
        self.folder_destination_button = ttk.Button(self.folder_view, width=26, text="Select Destination", command=self.folder_destination_select_on_click)

        self.folder_destination_label.grid(row=1, column=0, padx=5, pady=5, sticky="ne")
        self.folder_destination_display.grid(row=1, column=1, padx=5, pady=5, sticky="ne")
        self.folder_destination_button.grid(row=1, column=2, padx=5, pady=5, sticky="ne")

        self.done_button = ttk.Button(parent, text="Done", command=self.done_button_on_click)
        self.done_button.grid(row=1, column=0, padx=5, pady=5)
        self.get_current_dirs()

    def done_button_on_click(self):
        with open(f"{os.getcwd()}/conf.csv", "+w") as file:
            file.write(f"{self.folder_source_txt_var.get()}\n{self.folder_destination_txt_var.get()}")
        exit()

    def folder_source_select_on_click(self):
        folder_selection = tk.filedialog.askdirectory(title="Select Source Folder", initialdir=self.check_if_dir_exists(self.folder_source_txt_var))
        self.folder_source_txt_var.set(folder_selection)

    def folder_destination_select_on_click(self):
        folder_selection = tk.filedialog.askdirectory(title="Select Destination Folder", initialdir=self.check_if_dir_exists(self.folder_destination_txt_var))
        self.folder_destination_txt_var.set(folder_selection)

    def get_current_dirs(self):
        if os.path.isfile(f"{os.getcwd()}/conf.csv"):
            dirs = open(f"{os.getcwd()}/conf.csv").read().splitlines()
            displays = [self.folder_source_txt_var, self.folder_destination_txt_var]
            for x, y in zip(dirs, displays):
                y.set(x)

    def check_if_dir_exists(self, path):
        if path.get() != "":
            return path.get()
        else:
            return os.getcwd()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.wm_title("Watch Configuration")
    root.iconbitmap(default=f"{os.getcwd()}/icons/gear_32x32.ico")
    root.mainloop()
