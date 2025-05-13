nomor_pelanggan = []
nama_pelanggan = []
total_belanja = []
while True:
    print("Menu Utama")
    print("   ")
    print("   1. Tambah Data")
    print("   2. hapus Data")
    print("   3. Cetak Data")
    print("   4. Keluar")
    print("   ")
    n = int(input("Pilih Menu: "))
    print("   ")

    if n == 1:
        print("Tambah Data Pelanggan")
        nomor = input("Masukkan Nomor: ")
        nama = input("Masukkan Nama Anda: ")
        total = float(input("Masukkan Total Belanja: "))

        nomor_pelanggan.append(nomor)
        nama_pelanggan.append(nama)
        total_belanja.append(total)
        print("Data Berhasil Ditambah")
        print("   ")
    elif n == 2:
        print("Hapus Data Pelanggan")
        x = int(input("Masukkan Index Nomor Pelanggan Yang Ingin Dihapus: ")) 
        nomor_pelanggan.pop(x)
        nama_pelanggan.pop(x)
        total_belanja.pop(x)
        print("Data Berhasil Dihapus")
    elif n == 3:
        print("Data Pelanggan")
        if len(nomor_pelanggan)> 0:
            print("Index     No Pelanggan     Nama Pelanggan     Total Belanja")
            for i in range (len(nomor_pelanggan)):
                print(f'{i} {nomor_pelanggan[i]:>10} {nama_pelanggan[i]:>20}   {total_belanja[i]:>15}')
        else:  
            print("Data Kosong, Silahkan Tambahkan Data Anda")
    elif n == 4:
        print("Terimakasih Telah Menggunakan Program Ini")
        break
