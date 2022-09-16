# Menghitung luas kubus dan volumme kubus===
print("Menghitung luas dan volume kubus")

r = int(input("Masukkan Nilai Rusuk = "))

Luaskubus = 6*r*r
Volumekubus = r*r*r

print("Luas kubus :", Luaskubus)
print("Volume kubus :", Volumekubus)

print('=' * 35)

# ===Menghitung luas balok dan volume balok===
print("Menghitung Luas dan Volume Balok")

panjang = int(input("Masukkan nilai panjang = "))
lebar = int(input("Masukkan niali lebar = "))
tinggi = int(input("Masukkan nilai tinggi = "))

luasbalok = 2*(panjang*lebar)+(panjang*tinggi)+(lebar*tinggi)
volumebalok = panjang*lebar*tinggi

print("Luas balok :", luasbalok)
print("Volume balok :",volumebalok)