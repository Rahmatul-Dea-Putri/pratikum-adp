# Menampilkan Daftar Nama Barang dan Harga Barang 
barang = {
    "Es Krim": 50000,
    "Cokelat": 100000,
    "Sandal": 50000,
    "Baju": 60000,
    "Beras" : 70000,
    "Seafood": 65000,
    "Ciki Ciki": 75000,
    "Body Scrub": 80000,
    "Obat": 55000,
    "Susu": 85000,
    "Alat Tulis": 100000,
    "Mainan": 100000,
}

# Menampilkan Daftar Barang
print("==============================DAFTAR BARANG================================")
for perlengkapan, harga in barang.items():
    print(f"{perlengkapan:12} Rp {harga:}")

print("\nUntuk pembelian kurang dari 1.000.000, tidak mendapatkan diskon") 
print("Untuk pembelian 1.000.000 - 1.500.000, memperoleh diskon 10%")
print("Untuk pembelian lebih dari 1.500.000, memperoleh diskon 15%")
print("===========================================================================")

# Tagihan Pembayaran
nama_barang = input("Nama barang: ")
kuantitas = int(input("Kuantitas: "))
harga_satuan = barang[nama_barang]
harga_total = kuantitas * harga_satuan

# Menghitung Jumlah Diskon
diskon = 0
if harga_total > 1500000:
    diskon = harga_total * 15 / 100
elif 1000000 <= harga_total <= 1500000:
    diskon = harga_total * 10 / 100
else : #harga total < 1000000
    diskon = 0

# Menghitung total pembayaran setelah mendapatkan diskon
total_bayar = harga_total - diskon

# Tampilan Output
print("\n|===============================|")
print("|     : DAFTAR PEMBELIAN :      |")
print("|===============================|")
print("Nama Barang:", nama_barang)    
print("---------------------------------")
print("Kuantitas:", kuantitas)
print("---------------------------------")
print("Harga Satuan: Rp", harga_satuan)
print("---------------------------------")
print("Harga Total: Rp", harga_total)
print("---------------------------------")
print("Potongan Harga: Rp", diskon)
print("---------------------------------")
print("Total Bayar: Rp", total_bayar)
print("---------------------------------")