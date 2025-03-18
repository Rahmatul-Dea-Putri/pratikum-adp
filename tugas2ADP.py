n = int(input("input nilai patisi n = "))

a = 1 #batas bawah
b = 3 #batas atas
delta_x = (b-a)/n 
luas_daerah = 0
for i in range (1,n+1) :
    x = a + i * delta_x
    fungsi = x**2 + 2*x
    luas_daerah += fungsi * delta_x
print("Luas daerah dari fungsi x**2 + 2*x dengan batas daerah x=1 dan x=3 dan jumlah partisi n = ", n ,"adalah", luas_daerah )