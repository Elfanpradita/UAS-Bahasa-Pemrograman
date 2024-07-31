import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung biaya sewa dan total bayar
def hitung():
    try:
        kode_kamar = kode_kamar_var.get().upper()
        lama_sewa = int(lama_sewa_entry.get())
        uang_bayar = float(uang_bayar_entry.get())
        
        harga_sewa = 0
        nama_kamar = ""
        
        if kode_kamar == 'M':
            harga_sewa = 650000
            nama_kamar = "Melati"
        elif kode_kamar == 'S':
            harga_sewa = 550000
            nama_kamar = "Sakura"
        elif kode_kamar == 'L':
            harga_sewa = 400000
            nama_kamar = "Lily"
        elif kode_kamar == 'A':
            harga_sewa = 350000
            nama_kamar = "Anggrek"
        else:
            messagebox.showerror("Error", "Kode kamar tidak valid")
            return

        jumlah_bayar = harga_sewa * lama_sewa
        
        ppn = 0
        if lama_sewa > 5:
            ppn = 0.10 * jumlah_bayar
        elif lama_sewa > 3:
            ppn = 0.05 * jumlah_bayar

        total_bayar = jumlah_bayar - ppn
        uang_kembali = uang_bayar - total_bayar

        # Output hasil perhitungan
        receipt_text = (
            f"Bukti Kwitansi Pembayaran\n"
            f"=========================\n"
            f"Nama Petugas: {nama_petugas_entry.get()}\n"
            f"Nama Customer: {nama_customer_entry.get()}\n"
            f"Tanggal Check-in: {tanggal_checkin_entry.get()}\n"
            f"Nama Kamar: {nama_kamar}\n"
            f"Harga Sewa/malam: Rp. {harga_sewa:,.2f}\n"
            f"Lama Sewa: {lama_sewa} malam\n"
            f"Diskon: Rp. {ppn:,.2f}\n"
            f"Jumlah Bayar: Rp. {jumlah_bayar:,.2f}\n"
            f"Total Bayar: Rp. {total_bayar:,.2f}\n"
            f"Uang Bayar: Rp. {uang_bayar:,.2f}\n"
            f"Uang Kembali: Rp. {uang_kembali:,.2f}\n"
        )
        
        hasil_label.config(text=receipt_text)

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid")

# Setup GUI
root = tk.Tk()
root.title("Hotel Sejuk Asri - Pembayaran")
root.geometry("400x600")
root.configure(bg="#FFA500")  # Set the background color to orange

# Styling elements
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 10)
entry_font = ("Arial", 10)
btn_font = ("Arial", 10, "bold")
result_font = ("Arial", 10, "bold")
color_bg = "#FFA500"  # Orange background color
color_fg = "black"

# Input Frame
input_frame = tk.Frame(root, bg=color_bg, pady=10)
input_frame.pack(fill="both", expand=True)

tk.Label(input_frame, text="Hotel Sejuk Asri", font=title_font, bg=color_bg, fg=color_fg).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(input_frame, text="Nama Petugas:", font=label_font, bg=color_bg, fg=color_fg).grid(row=1, column=0, sticky='w')
nama_petugas_entry = tk.Entry(input_frame, font=entry_font)
nama_petugas_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Nama Customer:", font=label_font, bg=color_bg, fg=color_fg).grid(row=2, column=0, sticky='w')
nama_customer_entry = tk.Entry(input_frame, font=entry_font)
nama_customer_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Tanggal Check-in (DD-MM-YYYY):", font=label_font, bg=color_bg, fg=color_fg).grid(row=3, column=0, sticky='w')
tanggal_checkin_entry = tk.Entry(input_frame, font=entry_font)
tanggal_checkin_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Kode Kamar [M/S/L/A]:", font=label_font, bg=color_bg, fg=color_fg).grid(row=4, column=0, sticky='w')
kode_kamar_var = tk.StringVar()
kode_kamar_entry = tk.Entry(input_frame, textvariable=kode_kamar_var, font=entry_font)
kode_kamar_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Lama Sewa (hari):", font=label_font, bg=color_bg, fg=color_fg).grid(row=5, column=0, sticky='w')
lama_sewa_entry = tk.Entry(input_frame, font=entry_font)
lama_sewa_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Uang Bayar (Rp):", font=label_font, bg=color_bg, fg=color_fg).grid(row=6, column=0, sticky='w')
uang_bayar_entry = tk.Entry(input_frame, font=entry_font)
uang_bayar_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Button(input_frame, text="Hitung Pembayaran", font=btn_font, command=hitung, bg="#4CAF50", fg="white").grid(row=7, column=0, columnspan=2, pady=10)

# Output Frame
output_frame = tk.Frame(root, bg=color_bg)
output_frame.pack(fill="both", expand=True)

hasil_label = tk.Label(output_frame, text="", font=result_font, bg=color_bg, fg=color_fg, justify="left")
hasil_label.pack(padx=10, pady=10, fill="both", expand=True)

# Control buttons
control_frame = tk.Frame(root, bg=color_bg)
control_frame.pack(fill="both", expand=True)

tk.Button(control_frame, text="Clear", font=btn_font, command=lambda: hasil_label.config(text=""), bg="#F44336", fg="white").pack(side="left", padx=10, pady=5)
tk.Button(control_frame, text="Pause", font=btn_font, bg="#FFC107", fg="white").pack(side="right", padx=10, pady=5)

root.mainloop()
