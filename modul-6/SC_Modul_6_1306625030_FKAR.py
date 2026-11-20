import pygame
import sys

pygame.init()

LEBAR, TINGGI = 800, 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Simulasi Jatuh Bebas & Pantulan")
jam = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

PUTIH = (255, 255, 255)
HITAM = (20, 20, 20)
BIRU_LANGIT = (135, 206, 235)
COKLAT_TANAH = (139, 90, 43)
MERAH = (220, 50, 50)

g = 9.8             
e = 0.8             
SKALA = 50          
RADIUS = 20         
TANAH_Y = 480       
BATAS_BERHENTI = 0.5  


H_AWAL = 8.0        
x = LEBAR // 2      
h = H_AWAL          
v = 0.0             
jumlah_pantulan = 0
berhenti = False

def reset(tinggi, posisi_x):
    """Mengembalikan bola ke kondisi awal."""
    global h, v, x, jumlah_pantulan, berhenti
    h = tinggi
    v = 0.0
    x = posisi_x
    jumlah_pantulan = 0
    berhenti = False

berjalan = True
while berjalan:
    dt = jam.tick(60) / 1000.0

    for kejadian in pygame.event.get():
        if kejadian.type == pygame.QUIT:
            berjalan = False
        elif kejadian.type == pygame.MOUSEBUTTONDOWN:
            mx, my = kejadian.pos
            tinggi_klik = (TANAH_Y - RADIUS - my) / SKALA   
            tinggi_klik = max(tinggi_klik, 0.5)
            reset(tinggi_klik, mx)
        elif kejadian.type == pygame.KEYDOWN:
            if kejadian.key == pygame.K_ESCAPE:
                berjalan = False
            elif kejadian.key == pygame.K_SPACE:
                reset(H_AWAL, LEBAR // 2)
            elif kejadian.key == pygame.K_RIGHT:
                g = round(g + 1.0, 1)
            elif kejadian.key == pygame.K_LEFT:
                g = max(1.0, round(g - 1.0, 1))


    if not berhenti:
        v = v - g * dt          
        h = h + v * dt          

        if h <= 0:              
            h = 0
            v = -e * v          
            jumlah_pantulan += 1
            if v < BATAS_BERHENTI:   
                v = 0
                berhenti = True
    layar.fill(BIRU_LANGIT)
    pygame.draw.rect(layar, COKLAT_TANAH, (0, TANAH_Y, LEBAR, TINGGI - TANAH_Y))

    y_layar = TANAH_Y - h * SKALA - RADIUS   
    pygame.draw.circle(layar, MERAH, (int(x), int(y_layar)), RADIUS)
    pygame.draw.circle(layar, HITAM, (int(x), int(y_layar)), RADIUS, 2)

    teks = [
        f"Ketinggian : {h:6.2f} m",
        f"Kecepatan  : {v:6.2f} m/s",
        f"Gravitasi g: {g:.1f} m/s^2",
        f"Pantulan   : {jumlah_pantulan}",
        "Klik = jatuhkan | SPASI = reset",
    ]
    for i, baris in enumerate(teks):
        layar.blit(font.render(baris, True, HITAM), (10, 10 + i * 24))

    pygame.display.flip()
pygame.quit()
sys.exit()