import pandas as pd
KOL_NAMA = "Mahasiswa"
KOL_LAIN = "Nilai Lain2"
KOL_UTS  = "Nilai  UTS"
KOL_UAS  = "Nilai  UAS"
df = pd.read_excel("DataNilai (2).xlsx")
nama = df[KOL_NAMA].tolist()
lain = df[KOL_LAIN].tolist()
uts  = df[KOL_UTS].tolist()
uas  = df[KOL_UAS].tolist()
jumlah_A = jumlah_Amin = jumlah_Bplus = jumlah_B = 0
jumlah_Bmin = jumlah_Cplus = jumlah_C = jumlah_TL = 0
print("Program Grading")
print("Nama : Firaz Khiar Al Rasyid")
print("NRM  : 1306625030")
print("_" * 39)
i = 0

while i < len(nama):
    na = 0.30 * lain[i] + 0.35 * uts[i] + 0.35 * uas[i]
    if na >= 86:
        grade = "A";  jumlah_A += 1
    elif na >= 81:
        grade = "A-"; jumlah_Amin += 1
    elif na >= 76:
        grade = "B+"; jumlah_Bplus += 1
    elif na >= 71:
        grade = "B";  jumlah_B += 1
    elif na >= 66:
        grade = "B-"; jumlah_Bmin += 1
    elif na >= 61:
        grade = "C+"; jumlah_Cplus += 1
    elif na >= 56:
        grade = "C";  jumlah_C += 1
    else:
        grade = "TL"; jumlah_TL += 1
    print(f"{i+1:<4}| {str(nama[i]):<14}| {na:>6.2f} | {grade:^6} |")
    i += 1
print("-" * 39)
print("Rekapitulasi :")
print(f"Grade A     = {jumlah_A}")
print(f"Grade A-    = {jumlah_Amin}")
print(f"Grade B+    = {jumlah_Bplus}")
print(f"Grade B     = {jumlah_B}")
print(f"Grade B-    = {jumlah_Bmin}")
print(f"Grade C+    = {jumlah_Cplus}")
print(f"Grade C     = {jumlah_C}")
print(f"Tidak Lulus = {jumlah_TL}")
print(f"Total Mahasiswa = {len(nama)}")
print("selesai")