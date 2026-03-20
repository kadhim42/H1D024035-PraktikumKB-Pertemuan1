import random
import time

# Struktur data
riwayat = []

# Library random
target = random.randint(1, 100)

print("GAME TEBAK ANGKA")
print("Tebak angka dari 1 sampai 100")

while True:
    tebak = int(input("Masukkan tebakan: "))
    riwayat.append(tebak)

    # Struktur kontrol
    if tebak == target:
        print("Benar!")
        break
    elif tebak < target:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")

print("\nWaktu selesai:", time.ctime())
print("Jumlah percobaan:", len(riwayat))
print("Riwayat tebakan:", riwayat)