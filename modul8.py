while True :
    print(" ~~ MENU UTAMA ~~ ")
    print("1. Lihat Catatan yang Tersedia")
    print("2. Buat Catatan Baru")
    print("3. Exit/Keluar")
    print(" ")
    n = int(input("Pilih menu anda : "))
    print(" ")

    if n == 1: 
        f = open("sederhana.txt", "r")
        line = f.readlines()
        f.close()
        data = []
        baris = 0
        while baris < len(line)-1:
            judul = ""
            isi = ""
            for i in line[baris]:
                if i != "\n":
                    judul += i
            for k in line[baris + 1]:
                if k != "\n":
                    isi += k
            data.append([judul , isi])
            baris += 2
            if len(data) == 0 :
                print("DATA BELUM ADA")
            else:
                print("Judul catatan yang ada: ")
                for j in data:
                    print("-" + j[0])
                baca = input("Masukkan judul yg akan dibaca: ")
                for j in data:
                    if baca == j[0]:
                        print(j[1])
                        break
                else:
                        print("DATA TIDAK ADA")
    elif n == 2 :
        judul = input("JUDUL : ")
        isi = input("ISI : ")
        f = open("sederhana.txt", "a")
        f.write(judul + '\n')
        f.write (isi + '\n')
        print("Data sudah disimpan")
    elif n == 3 :
        f.close()
        break
