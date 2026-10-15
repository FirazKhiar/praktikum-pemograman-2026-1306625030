import math
def mclaurin_sin(x, k):
    n = k - 1
    suku_sin = ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n + 1)
    return suku_sin
def mclaurin_cos(x, k):
    n = k - 1
    suku_cos = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
    return suku_cos
def main():
    while True:
        print("Program Sinus Cosinus")
        print("Nama : Firaz Khiar Al Rasyid")
        print("NIM : 1306625030")
        print()
        besar_sudut = float(input("Besar Sudut (derajat) = "))
        sudut_rad = math.radians(besar_sudut)
        tv_sin = math.sin(sudut_rad)
        print(f"True Value Sin {besar_sudut:.1f} = {tv_sin:.3f}")
        tv_cos = math.cos(sudut_rad)
        print(f"True Value Cos {besar_sudut:.1f} = {tv_cos:.3f}")
        print()
        print("=" * 65)
        print(f"{'Suku ke':<8} | {'AV Sin':<12} | {'ER Sin (%)':<10} | {'AV Cos':<12} | {'ER Cos (%)':<10}")
        print("=" * 65)
        suku_ke = 1
        av_sin = 0.0
        av_cos = 0.0 
        er_sin = 100.0
        er_cos = 100.0
        
        while (er_sin >= 5.0 or er_cos >= 5.0):
            av_sin += mclaurin_sin(sudut_rad, suku_ke)
            av_cos += mclaurin_cos(sudut_rad, suku_ke)
            er_sin = abs((tv_sin - av_sin) / tv_sin) * 100
            er_cos = abs((tv_cos - av_cos) / tv_cos) * 100
            print(f"{suku_ke:<8} | {av_sin:12.4f} | {er_sin:10.2f}   | {av_cos:12.4f} | {er_cos:10.2f}")
            suku_ke += 1
        print("=" * 65)
        print()
        ulang = input("Mau menghitung lagi (y/t)? = ").lower()
        if ulang != "y":
            break
if __name__ == "__main__":
    main()
print()
print("Selesai")