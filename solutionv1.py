"""
V1 GÖREV LİSTESİ (TASK LIST)[cite: 40, 45]:
1. 'init' komutunda dosya varlık kontrolü ekle ve 'Already initialized' mesajı döndür.
2. Veri saklama konumunu '.minidiary/diary.txt' olarak daha düzenli hale getir.
3. Hata mesajlarını kullanıcıya daha spesifik bilgi verecek şekilde güncelle.

V0 -> V1 DEĞİŞİKLİK ÖZETİ[cite: 46]:
- 'init' komutu artık mevcut sistemin üzerine yazmıyor, koruma sağlıyor[cite: 65].
- Veri dosyası '.minidiary/diary.txt' klasör içi yapısına taşındı[cite: 70].
- Boş giriş ve geçersiz ID kontrolleri için hata yönetimi mantığı güçlendirildi [cite: 71-75].
"""

import os
import sys
from datetime import datetime

# V1'de güncellenen dosya yolu [cite: 70]
STORAGE_DIR = ".minidiary"
DATA_FILE = os.path.join(STORAGE_DIR, "diary.txt")

def init():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    
    if os.path.exists(DATA_FILE):
        print("Already initialized.") [cite: 65]
        return
        
    with open(DATA_FILE, "w") as f:
        pass
    print("System initialized.")

def login(username):
    print(f"User {username} logged in.") [cite: 66]

def add(title):
    if not title.strip():
        print("Error: Entry title cannot be empty. Please enter valid text.") [cite: 73]
        return

    entries = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            entries = f.readlines()
    
    new_id = str(len(entries) + 1).zfill(3)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(DATA_FILE, "a") as f:
        f.write(f"{new_id} | {timestamp} | {title}\n")
    print(f"Added entry #{new_id}: {title}") [cite: 67]

def list_entries():
    if not os.path.exists(DATA_FILE):
        print("No entries found. Please run 'init' first.")
        return
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No entries found.") [cite: 68]
        else:
            for line in lines:
                print(line.strip())

def read_entry(entry_id):
    if not os.path.exists(DATA_FILE):
        print("Error: Diary entry file cannot be found.") [cite: 74]
        return
    found = False
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith(entry_id):
                print(f"Reading entry #{line.strip()}") [cite: 69]
                found = True
                break
    if not found:
        print(f"Error: Entry ID {entry_id} does not exist in the records.") [cite: 72]

def delete_entry(entry_id):
    if not os.path.exists(DATA_FILE):
        print("Error: File not found.")
        return
    lines = []
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
    
    new_lines = [l for l in lines if not l.startswith(entry_id)]
    
    if len(new_lines) < len(lines):
        with open(DATA_FILE, "w") as f:
            f.writelines(new_lines)
        print(f"Deleted entry #{entry_id}.") [cite: 70]
    else:
        print(f"Error: No matching entry found for ID {entry_id}.")

def main():
    if len(sys.argv) < 2:
        print("Error: Invalid Menu Input. No command provided.") [cite: 71]
        return
    cmd = sys.argv[1]
    if cmd == "init": init()
    elif cmd == "login" and len(sys.argv) > 2: login(sys.argv[2])
    elif cmd == "add" and len(sys.argv) > 2: add(sys.argv[2])
    elif cmd == "list": list_entries()
    elif cmd == "read" and len(sys.argv) > 2: read_entry(sys.argv[2])
    elif cmd == "delete" and len(sys.argv) > 2: delete_entry(sys.argv[2])
    else: print("Error: Command not recognized.")

if __name__ == "__main__":
    main()
