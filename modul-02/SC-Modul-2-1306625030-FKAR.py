print("Mencari Bilangan Faktor")
print("Nama : Firaz Khiar Al Rasyid")
print("NIM : 1306625030")
print()
while True:
    bilangan = int(input("Masukkan Bilangan Sembarang <100 (masukkan 0 untuk selesai) = "))
    
    if bilangan == 0:
        break
    
    if bilangan >= 100:
        print("Error")
        break
    
    faktor = []
    for i in range(1,bilangan+1):
        if bilangan % i == 0:
            faktor.append(i)
            
    print(f"Bilangan {bilangan} Faktornya = {faktor}")

print("Selesai")