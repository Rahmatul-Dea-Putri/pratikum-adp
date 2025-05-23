while True:
    m = int(input('Jumlah persamaan (2 atau 3): '))
    n = int(input('Jumlah variabel (1,2, atau 3) : '))

    if m > n:
        print('\nJumlah persamaan > Jumlah variabel, maka SPL tidak memiliki solusi.\n')
    elif m < n:
        print('\nJumlah persamaan < Jumlah variabel, maka SPL memiliki banyak solusi.\n')
    else:
        break

matriks = []
for i in range(m):
    baris = []
    print(f'\nKoefisien untuk persamaan ke-{i+1}')
    for j in range(n):
        elemen = float(input(f'Koefisien x{j+1} = '))
        baris.append(elemen)
    konstanta = float(input('Nilai konstanta = '))
    baris.append(konstanta)
    matriks.append(baris)

print('Matriks awal :')
for baris in matriks:
    print(baris)

berhasil = True
for i in range(m):
    if matriks[i][i] == 0:
        print(f'\nElemen diagonal pada baris {i+1} adalah nol, maka pembagian tidak bisa dilakukan.')
        berhasil = False
        break
    
    pembagi = matriks[i][i]
    for j in range(n+1):
        matriks[i][j] = matriks[i][j]/pembagi
    for k in range(m):
        if k != i:
            faktor = matriks[k][i]
            for j in range(n +1):
                matriks[k][j] = matriks[k][j]-faktor*matriks[i][j]
        
if berhasil:
    print('\nMatriks setelah eliminasi gauss :')
    for baris in matriks:
        print(baris)
    print('\Solusi :')
    for i in range(n):
        print(f'x{i+1} = {matriks[i][n]}')
else:
    print('Karena pembagian tidak bisa dilakukan, maka solusi SPL ini tidak ada.')




