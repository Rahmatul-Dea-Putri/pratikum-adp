
pakai = int(input("Jumlah pemakaian (dalam kwh): "))

print("  -- GOLONGAN TARIF -- ")
print("=====================================================================================")
print("Golongan 1: Rp 1500/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 2000/kwh")
print("Golongan 2: Rp 2500/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 3000/kwh")
print("Golongan 3: Rp 4000/kwh untuk 100 kwh pertama, selanjtnya dikenakan   Rp 5000/kwh")
print("Golongan 4: Rp 5000/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 7000/kwh")
print("=====================================================================================")

golongan = int(input("Golongan listrik (1-4): "))
def gol (golongan):
    if golongan == 1:
        print("Golongan listrik anda:", golongan)
        if pakai > 100:
            kwh = pakai-100
            total = (1500*100)+(kwh*2000)
            print("Total biaya yang harus dibayar Rp", total)
        else:
            biaya = pakai*1500
            print("Total yang harus dibayar Rp", biaya)
    elif golongan == 2:
        print("Golongan listrik anda:", golongan)
        if pakai > 100:
            kwh = pakai-100
            bayar = (2500*100)+(kwh*3000)
            print("Total biaya yang harus dibayar Rp", bayar)
        else:
            biaya = pakai*2500
            print("Total biaya yang harus dibayar Rp", biaya)
    elif golongan == 4:
        print("Golongan listrik anda:", golongan)
        if pakai > 100:
            kwh = pakai-100
            jumlah= (5000*100)+(kwh*7000)
            print("Total biaya yang harus dibayar Rp", jumlah)
        else:
            biaya = pakai*5000
            print("Total biaya yang harus dibayar Rp", biaya)
    else:
        print("Golongan listrik anda:", golongan)
        if pakai >100:
            kwh = pakai-100
            Total_biaya = (4000*100)+(kwh*5000)
            print("Total biaya yang harus dibayar Rp", Total_biaya)
        else :
            biaya = pakai*4000
            print("Total biaya yang harus dibayar Rp", biaya)
gol(golongan) 