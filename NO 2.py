import tkinter as tk
from tkinter import messagebox

def luas_segi_empat(sisi):
    return sisi ** 2

def keliling_segi_empat(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c

def luas_lingkaran(radius):
    return 3.14159 * radius ** 2

def keliling_lingkaran(radius):
    return 2 * 3.14159 * radius

def hitung():
    pilihan = menu_var.get()
    try:
        if pilihan == "Segi Empat":
            sisi = float(input_1_entry.get())
            luas = luas_segi_empat(sisi)
            keliling = keliling_segi_empat(sisi)
            hasil_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")
        
        elif pilihan == "Persegi Panjang":
            panjang = float(input_1_entry.get())
            lebar = float(input_2_entry.get())
            luas = luas_persegi_panjang(panjang, lebar)
            keliling = keliling_persegi_panjang(panjang, lebar)
            hasil_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")
        
        elif pilihan == "Segitiga":
            alas = float(input_1_entry.get())
            tinggi = float(input_2_entry.get())
            sisi_3 = float(input_3_entry.get())
            luas = luas_segitiga(alas, tinggi)
            keliling = keliling_segitiga(alas, tinggi, sisi_3)
            hasil_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")
        
        elif pilihan == "Lingkaran":
            radius = float(input_1_entry.get())
            luas = luas_lingkaran(radius)
            keliling = keliling_lingkaran(radius)
            hasil_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")
        
        else:
            messagebox.showerror("Error", "Pilih bangun datar")
            return

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid")

def update_input_fields():
    pilihan = menu_var.get()
    if pilihan == "Segi Empat":
        label_1.config(text="Sisi:")
        label_2.grid_remove()
        input_2_entry.grid_remove()
        label_3.grid_remove()
        input_3_entry.grid_remove()
    elif pilihan == "Persegi Panjang":
        label_1.config(text="Panjang:")
        label_2.config(text="Lebar:")
        label_2.grid()
        input_2_entry.grid()
        label_3.grid_remove()
        input_3_entry.grid_remove()
    elif pilihan == "Segitiga":
        label_1.config(text="Alas:")
        label_2.config(text="Tinggi:")
        label_3.config(text="Sisi 3:")
        label_2.grid()
        input_2_entry.grid()
        label_3.grid()
        input_3_entry.grid()
    elif pilihan == "Lingkaran":
        label_1.config(text="Radius:")
        label_2.grid_remove()
        input_2_entry.grid_remove()
        label_3.grid_remove()
        input_3_entry.grid_remove()
    else:
        label_1.config(text="Input 1:")
        label_2.config(text="Input 2 (jika ada):")
        label_3.config(text="Input 3 (jika ada):")
        label_2.grid()
        input_2_entry.grid()
        label_3.grid()
        input_3_entry.grid()

root = tk.Tk()
root.title("Perhitungan Bangun Datar")

root.configure(bg="#f0f0f0")
font_style = ("Helvetica", 12)

menu_var = tk.StringVar()
menu_var.trace('w', lambda *args: update_input_fields())

tk.Label(root, text="Pilih Bangun Datar", bg="#f0f0f0", font=font_style).grid(row=0, column=0, padx=10, pady=10)
tk.OptionMenu(root, menu_var, "Segi Empat", "Persegi Panjang", "Segitiga", "Lingkaran").grid(row=0, column=1, padx=10, pady=10)

label_1 = tk.Label(root, text="Input 1", bg="#f0f0f0", font=font_style)
label_1.grid(row=1, column=0, padx=10, pady=5)
input_1_entry = tk.Entry(root, font=font_style)
input_1_entry.grid(row=1, column=1, padx=10, pady=5)

label_2 = tk.Label(root, text="Input 2 (jika ada)", bg="#f0f0f0", font=font_style)
label_2.grid(row=2, column=0, padx=10, pady=5)
input_2_entry = tk.Entry(root, font=font_style)
input_2_entry.grid(row=2, column=1, padx=10, pady=5)

label_3 = tk.Label(root, text="Input 3 (jika ada)", bg="#f0f0f0", font=font_style)
label_3.grid(row=3, column=0, padx=10, pady=5)
input_3_entry = tk.Entry(root, font=font_style)
input_3_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=font_style).grid(row=4, column=1, padx=10, pady=10)

hasil_label = tk.Label(root, text="", bg="#f0f0f0", font=font_style)
hasil_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
