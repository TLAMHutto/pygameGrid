# hot_reload.py

import os
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command, debounce_time=1.0):
        self.command = command
        self.debounce_time = debounce_time
        self.last_modified_time = {}
        self.last_reload_time = time.time()
    
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            current_time = time.time()
            last_modified = self.last_modified_time.get(event.src_path, 0)
            if current_time - last_modified > self.debounce_time:
                self.last_modified_time[event.src_path] = current_time
                if current_time - self.last_reload_time > self.debounce_time:
                    self.last_reload_time = current_time
                    print(f"Change detected in {event.src_path}. Restarting...")
                    subprocess.run(self.command, shell=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: python hot_reload.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    path = os.getcwd()  # Monitor current directory
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)  # Sleep to keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
