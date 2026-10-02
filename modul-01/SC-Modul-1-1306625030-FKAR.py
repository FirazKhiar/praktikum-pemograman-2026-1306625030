print("Tabel Konversi Suhu")
print("Nama : Firaz Khiar Al Rasyid")
print("NIM : 1306625030")
print()
#input
suhu_awal = int(input("Masukkan Suhu Awal = "))
suhu_akhir = int(input("Masukkan Suhu Akhir = "))
selang = int(input("Masukkan Selang = "))

print("Tabel Konversi Suhu")
print("=" * 42)
print("|| NO || Celcius|| Reamur || Fahrenheit ||")
print("=" * 42)

no = 1

for celcius in range(suhu_awal,suhu_akhir + 1, selang):
    reamur = 4/5 * celcius
    fahrenheit = 9/5 * celcius + 32
    
    print(f"|| {no:2} || {celcius:4} || {reamur:8.2f} || {fahrenheit:10.2f} ||")
    
    no = no + 1

print("=" * 42)
print("selesai")
