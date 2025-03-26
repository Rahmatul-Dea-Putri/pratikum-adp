#Menginput banyak pendaftar
n = int(input("Masukan jumlah pendaftar = "))

#Menginput data data yang dibutuhkan
for i in range (1,n+1):
    print(f"Data Pendaftar {i}")
    nama = input("Nama = ")
    matkul = input("Mata Kuliah yang Diminati = ")
    p = 0 
    while p <= 0:
        wawancara = float(input("Penilaian Wawancara (rentang nilai 1-100) = ")) 
        if 0 <= wawancara <= 100:
            p+=1
        else:
            print("Inputkan ulang nilai anda")
    q = 0
    while q <= 0:
        tulis = float(input("Penilaian Test Tulis (rentang nilai 1-100) = "))
        if 0 <= tulis <= 100:
            q+=1
        else:
            print("Inputkan ulang nilai anda")
    r = 0
    while r <= 0:
        mengajar = float(input("Penilaian Mengajar (rentang nilai 1-100) = "))
        if 0 <= mengajar <= 100:
            r+=1
        else:
            print("Inputkan ulang nilai anda")

    #Tentukan Nilai dan Prediket Pendaftar
    nilai = 0
    nilai += (wawancara + tulis + mengajar) / 3
    print("Rata rata nilai pendaftar = ",nilai)
    if nilai > 80 :
        print("Prediket : LULUS")
    else : 
        print("Prediket : TIDAK LULUS")
    print(" ")
            