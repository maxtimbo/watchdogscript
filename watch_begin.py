import os, time, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

if os.path.isfile(f"{os.getcwd()}/conf.csv"):
    dirs = open(f"{os.getcwd()}/conf.csv").read().splitlines()
    source = dirs[0].replace("/", "\\")
    destination = dirs[1].replace("/", "\\")
    for x in dirs:
        if os.path.isdir(x):
            pass
        else:
            messagebox.showerror("Error", f"The directory {x} is invalid")
            exit()
else:
    messagebox.showerror("Error", "The configuration file does not exist.")
    exit()

print("We've made it passed the checks")
print(source, destination)
paused = False

def check_count(file):
    global count, paused
    if count == 5:
        paused = True
        time.sleep(3)
        shutil.move(file, destination)
        count = 0
        paused = False
    else:
        print("Not yet")

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        global count, paused
        if paused is True:
            return
        else:
            count += 1
            print(f"the file {event.src_path} has been created")

    def on_deleted(self, event):
        global count, paused
        if paused is True:
            return
        else:
            count += 1
            print(f"the file {event.src_path} has been deleted")

    def on_modified(self, event):
        global count, paused
        if paused is True:
            return
        else:
            count += 1
            print(f"{event.src_path} was modified {count}")
            file = event.src_path
            check_count(file)

    def on_moved(self, event):
        global count, paused
        if paused is True:
            return
        else:
            print(f"{event.src_path} was moved")

    # def check_count(self, file):
    #     global count
    #     if count == 5:
    #         shutil.move(file, destination)
    #         count = 0
    #     else:
    #         print("Not yet")

if __name__ == "__main__":
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=source, recursive=False)
    observer.start()
    count = 0
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
