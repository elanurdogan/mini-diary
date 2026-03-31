import os
import sys
from datetime import datetime

# Spec v0 Veri Yapısı [cite: 3, 10]
STORAGE_DIR = ".minidiary"
DATA_FILE = ".minidiary.dat" 

def init():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    with open(DATA_FILE, "w") as f:
        pass
    print("System initialized.") [cite: 4]

def login(username):
    print(f"User {username} logged in.") [cite: 5]

def add(title):
    if not title.strip():
        print("Error: Empty input validation failed.") [cite: 13]
        return

    count = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            count = len(f.readlines())
    
    new_id = str(count + 1).zfill(3)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(DATA_FILE, "a") as f:
        f.write(f"{new_id} | {timestamp} | {title}\n") [cite: 10]
    print(f"Added entry #{new_id}: {title}") [cite: 7]

def list_entries():
    if not os.path.exists(DATA_FILE):
        print("No entries found.") [cite: 8]
        return
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No entries found.")
        else:
            for line in lines:
                print(line.strip())

def read_entry(entry_id):
    if not os.path.exists(DATA_FILE):
        print("Error: File Not Found.") [cite: 14]
        return
    found = False
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith(entry_id):
                print(f"Reading entry #{line.strip()}") [cite: 9]
                found = True
                break
    if not found:
        print(f"Error: Entry ID {entry_id} not found.") [cite: 12]

def delete_entry(entry_id):
    if not os.path.exists(DATA_FILE):
        print("Error: File Not Found.")
        return
    lines = []
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
    
    new_lines = [l for l in lines if not l.startswith(entry_id)]
    
    if len(new_lines) < len(lines):
        with open(DATA_FILE, "w") as f:
            f.writelines(new_lines)
        print(f"Deleted entry #{entry_id}.") [cite: 10]
    else:
        print(f"Error: Entry ID {entry_id} not found.")

def main():
    if len(sys.argv) < 2:
        print("Error: Invalid Menu Input.") [cite: 11]
        return
    cmd = sys.argv[1]
    if cmd == "init": init()
    elif cmd == "login" and len(sys.argv) > 2: login(sys.argv[2])
    elif cmd == "add" and len(sys.argv) > 2: add(sys.argv[2])
    elif cmd == "list": list_entries()
    elif cmd == "read" and len(sys.argv) > 2: read_entry(sys.argv[2])
    elif cmd == "delete" and len(sys.argv) > 2: delete_entry(sys.argv[2])
    else: print("Error: Invalid command.")

if __name__ == "__main__":
    main()
