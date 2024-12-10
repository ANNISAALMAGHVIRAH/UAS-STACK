class UndoRedo:
    def __init__(self): self.undo, self.redo = [], []
    def add(self, action): self.undo.append(action); self.redo.append(action)
    def undo_action(self): print("Undo berhasil." if self.undo else "Tidak ada yang bisa di-undo.")
    def redo_action(self): print("Redo berhasil." if self.redo else "Tidak ada yang bisa di-redo.")
    def show(self): print(f"Undo: {self.undo or 'Kosong'}, Redo: {self.redo or 'Kosong'}")

ur = UndoRedo()
while True:
    pilihan = input("\n1. Tambahkan aksi | 2. Undo | 3. Redo | 4. Lihat stack undo dan redo | 5. Keluar: ")
    
    if pilihan == '1':
        aksi = input("Pilih aksi (a. Office Word, b. Chrome, c. Visual studio code): ")
        if aksi == 'a': ("Jalankan Office Word")
        elif aksi == 'b': ("Buka Google Chrome")
        elif aksi == 'c': ("Jalankan VSCode")
        else:
            print("Pilihan tidak valid.")
    
    elif pilihan == '2': ur.undo_action()
    elif pilihan == '3': ur.redo_action()
    elif pilihan == '4': ur.show()
    elif pilihan == '5': break
    else: 
        print("Pilihan tidak valid.")
