import tkinter as tk
from tkinter import messagebox

data_barang = {}

def tambah_barang():
    nama = nama_barang_entry.get().strip()
    harga = harga_barang_entry.get().strip()
    stok = stok_barang_entry.get().strip()
    
    if not nama:
        messagebox.showerror("Error", "Nama barang tidak boleh kosong.")
        return
    
    if not harga.isdigit() or not stok.isdigit():
        messagebox.showerror("Error", "Harga dan stok harus berupa angka.")
        return
    
    data_barang[nama] = {"harga": int(harga), "stok": int(stok)}
    messagebox.showinfo("Berhasil", f"Barang '{nama}' ditambahkan.")
    clear_entries()
    tampil_barang()

def tampil_barang():
    output = "Data Barang:\n"
    for nama, info in data_barang.items():
        output += f"{nama}: Harga - Rp. {info['harga']}, Stok - {info['stok']}\n"
    data_barang_label.config(text=output)

def hapus_barang():
    nama = nama_barang_entry.get().strip()
    if nama in data_barang:
        del data_barang[nama]
        messagebox.showinfo("Berhasil", f"Barang '{nama}' dihapus.")
        tampil_barang()
    else:
        messagebox.showerror("Error", f"Barang '{nama}' tidak ditemukan.")
    clear_entries()

def cari_barang():
    nama = nama_barang_entry.get().strip()
    if nama in data_barang:
        info = data_barang[nama]
        data_barang_label.config(text=f"Detail Barang:\n{nama}: Harga - Rp. {info['harga']}, Stok - {info['stok']}")
    else:
        messagebox.showerror("Error", f"Barang '{nama}' tidak ditemukan.")
    clear_entries()

def beli_barang():
    nama = nama_barang_entry.get().strip()
    jumlah = jumlah_barang_entry.get().strip()
    
    if not jumlah.isdigit():
        messagebox.showerror("Error", "Jumlah harus berupa angka.")
        return

    if nama in data_barang:
        jumlah = int(jumlah)
        stok = data_barang[nama]["stok"]
        if jumlah <= stok:
            total_harga = jumlah * data_barang[nama]["harga"]
            data_barang[nama]["stok"] -= jumlah
            messagebox.showinfo("Total Harga", f"Total harga: Rp. {total_harga}")
            tampil_barang()
        else:
            messagebox.showerror("Error", "Stok tidak mencukupi.")
    else:
        messagebox.showerror("Error", "Barang tidak ditemukan.")
    clear_entries()

def clear_entries():
    nama_barang_entry.delete(0, tk.END)
    harga_barang_entry.delete(0, tk.END)
    stok_barang_entry.delete(0, tk.END)
    jumlah_barang_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Manajemen Barang Hotel Sejuk Asri")
root.configure(bg="#ff6347")

label_style = {"font": ("Arial", 12, "bold"), "bg": "#ff6347", "fg": "white"}
entry_style = {"font": ("Arial", 12), "bg": "#ffe4e1", "fg": "black"}

tk.Label(root, text="Nama Barang", **label_style).grid(row=0, column=0, padx=10, pady=5, sticky="w")
nama_barang_entry = tk.Entry(root, **entry_style)
nama_barang_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Harga Barang", **label_style).grid(row=1, column=0, padx=10, pady=5, sticky="w")
harga_barang_entry = tk.Entry(root, **entry_style)
harga_barang_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Stok Barang", **label_style).grid(row=2, column=0, padx=10, pady=5, sticky="w")
stok_barang_entry = tk.Entry(root, **entry_style)
stok_barang_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Tambah Barang", command=tambah_barang, font=("Arial", 12, "bold"), bg="#ff4500", fg="white").grid(row=3, column=1, pady=10)

tk.Button(root, text="Tampil Barang", command=tampil_barang, font=("Arial", 12, "bold"), bg="#ff4500", fg="white").grid(row=4, column=1, pady=10)
data_barang_label = tk.Label(root, text="", justify=tk.LEFT, **label_style)
data_barang_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Hapus Barang", command=hapus_barang, font=("Arial", 12, "bold"), bg="#ff4500", fg="white").grid(row=6, column=1, pady=10)
tk.Button(root, text="Cari Barang", command=cari_barang, font=("Arial", 12, "bold"), bg="#ff4500", fg="white").grid(row=7, column=1, pady=10)

tk.Label(root, text="Jumlah Barang", **label_style).grid(row=8, column=0, padx=10, pady=5, sticky="w")
jumlah_barang_entry = tk.Entry(root, **entry_style)
jumlah_barang_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Button(root, text="Beli Barang", command=beli_barang, font=("Arial", 12, "bold"), bg="#ff4500", fg="white").grid(row=9, column=1, pady=10)

root.mainloop()
