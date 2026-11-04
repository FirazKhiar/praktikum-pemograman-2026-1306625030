Nilai = [85, 13, 99, 34, 71, 15, 82, 24, 64, 61, 67, 99, 50, 68, 25, 37, 32, 27, 14, 91,79, 15, 47, 48, 74, 88, 64, 53, 77, 50, 24, 91, 87, 55, 60, 75, 91, 22, 47, 63,
         81, 88, 26, 48, 69, 59, 84, 77, 28, 36, 59, 74, 89, 73, 91, 64, 55, 88, 90, 48,73, 97, 98, 40, 93, 50, 78, 60, 44, 77, 82, 51, 53, 65, 98, 59, 94, 91, 52, 44,
         65, 85, 72, 92, 49, 67, 58, 48, 62, 54, 89, 67, 58, 48, 85, 45, 77, 76, 81, 77]
print("Program Sorting")
print("Nama : Firaz Khiar Al Rasyid")
print("NIM  : 1306625030")
print("Data nilai awal :")
print(", ".join(str(x) for x in Nilai))
print()
data = Nilai.copy()
n = len(data)
sorting = True
while sorting:
    sorting = False
    i = 0
    while i < n - 1:
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            sorting = True
        i += 1
print("Data nilai terurut :", end=" ")
k = 0
while k < n:
    print(", ".join(f"{x:2d}" for x in data[k:k + 10]))
    k += 10
print("*selesai*")