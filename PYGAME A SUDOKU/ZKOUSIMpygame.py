import pygame

# inicializace pygame
pygame.init()

# vytvoření obrazovky
sirka = 1200
vyska = 700
obrazovka = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("SUDOKU")

# definice barev
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
alabaster = (237, 234, 222)
baby_blue = (137, 207, 240)
baby_purple = (170, 145, 217)
baby_pink = (235, 194, 194)

# barva pozadí
obrazovka.fill(white)

# tvary
# čtverec, obdélník
pygame.draw.rect(obrazovka, alabaster, (35, 35, 1130, 630))
pygame.draw.rect(obrazovka, baby_purple, (35, 50, 1130, 73))
pygame.draw.rect(obrazovka, baby_pink, (sirka - 355, 200, 273, 418))
pygame.draw.rect(obrazovka, baby_blue, (50, 138, 512, 512))

# čára
pygame.draw.line(obrazovka, baby_purple, (800,100), (800, (vyska - 36)), 5 )

# vložení obrázku
fotka_na_ISIC = pygame.image.load("img/IMG_6428.JPG")
fotka_na_ISIC_rect = fotka_na_ISIC.get_rect()
fotka_na_ISIC_rect.topleft = (sirka - 340, 215)

# custom font a pak text
custom_font_nadpis = pygame.font.Font("venv/cour.ttf", 64)
nadpis = custom_font_nadpis.render("SUDOKU", True, black, baby_purple)
nadpis_rect = nadpis.get_rect()
nadpis_rect.midtop = (sirka/2, 50)
custom_font_student = pygame.font.Font("venv/cour.ttf", 32)
student = custom_font_student.render("zápočtový program", True, black, alabaster)
student_rect = student.get_rect()
student_rect.topleft = (sirka - 380, 146)
prostor_vymezeny_na_sudoku = custom_font_student.render("prostor vymezený na sudoku", True, black, white)
prostor_vymezeny_na_sudoku_rect = prostor_vymezeny_na_sudoku.get_rect()
prostor_vymezeny_na_sudoku_rect.topleft = (60, 400)
custom_font_jmeno = pygame.font.Font("venv/cour.ttf", 23)
jmeno = custom_font_jmeno.render("Viktorie Pavelková", True, black, baby_pink)
jmeno_rect = jmeno.get_rect()
jmeno_rect.center = (sirka - 220, 560)
skola_a_rok = custom_font_jmeno.render("MFF, 2022", True, black, baby_pink)
skola_a_rok_rect = skola_a_rok.get_rect()
skola_a_rok_rect.center = (sirka - 220, 590)

# hudba v pozadí
hudba_v_pozadi = pygame.mixer.Sound("media/01 www.fesliyanstudios.com.mp3")

# hlasitost hudby v pozadí
hudba_v_pozadi.set_volume(0.08)

# přehrát hudbu v pozadí
hudba_v_pozadi.play()
#pygame.mixer.music.stop()

"""# ČEKÁNÍ"""
#pygame.time.delay(5000)

# hrací čas
#hraci_cas = pygame.time.Clock()
#current_time = 0


# hlavní herní cyklus
pokracujeme = True
while pokracujeme:
    for akce in pygame.event.get():
        print(akce)
        if akce.type == pygame.QUIT:
            pokracujeme = False
    
    # přidání obrázku
    obrazovka.blit(fotka_na_ISIC, fotka_na_ISIC_rect)

    # přidání textu
    obrazovka.blit(nadpis, nadpis_rect)
    obrazovka.blit(student, student_rect)
    obrazovka.blit(jmeno, jmeno_rect)
    obrazovka.blit(skola_a_rok, skola_a_rok_rect)
    obrazovka.blit(prostor_vymezeny_na_sudoku, prostor_vymezeny_na_sudoku_rect)

    # refresh obrazovky
    pygame.display.update()


# ukončení pygame
pygame.quit()