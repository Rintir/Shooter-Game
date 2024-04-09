import random
import time
import pygame, sys, math
import os

pygame.init()

pygame.HWSURFACE
pygame.DOUBLEBUF
# VIZUÁLY

rozmery = pygame.display.Info()
W, H = rozmery.current_w, rozmery.current_h
# W, H = 1200,700
WIN = pygame.display.set_mode((W, H),
                              pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

pygame.HWSURFACE
pygame.DOUBLEBUF

print(rozmery)
# WIN = pygame.display.set_mode((0,0))
# pygame.display.toggle_fullscreen()
pygame.display.set_caption("Raketka")

# BARVY
BILA = (255, 255, 255)
SSBILA = "#f3f3f8"
SBILA = "#eaeaf5"
LIME = "#8EE662"
CERNA = "#000000"
MODRA = 0, 0, 255
# SSBILA = "#000000"
# ENGINE
FPS = 120
ROTACE = 0

zasobnik = 0
# time_boost = 1600

# TEXTÍKY
START_OKNO = pygame.Rect(W / 2 - 143, H / 2 - 30, 270, 80)
OBTIZNOST_OKNO = pygame.Rect(W / 2 - 126, H / 2 + 63, 240, 75)
OVLADANI_OKNO = pygame.Rect(W / 2 - 122, H / 2 + 147, 234, 75)
OPUSTIT_HRU_OKNO = pygame.Rect(W - 45, 10, 35, 35)
NASTAVENI_SMRTELNOSTI = pygame.Rect(W - 100, H - 85, 70, 80)

PROJSMRTELNOST = pygame.image.load(
    os.path.join('Assets', 'projsmrtelnost.png')).convert_alpha()
PROJSMRTELNOST_SKRT = pygame.image.load(
    os.path.join('Assets', 'projsmrtelnost_skrtnuta.png')).convert_alpha()
NAPOVEDA = pygame.image.load(
    os.path.join('Assets', 'Napoveda.png')).convert_alpha()
NAPOVEDA = pygame.transform.scale(NAPOVEDA, (W, H))
MEDAILE = pygame.image.load(
    os.path.join('Assets', 'Medaile.png')).convert_alpha()
NADPIS = pygame.image.load(
    os.path.join('Assets', 'Nadpis.png')).convert_alpha()
NADPIS = pygame.transform.scale(NADPIS, (1200, 675))
KRIZEK_HOVER = pygame.image.load(
    os.path.join('Assets', 'krizek.png')).convert_alpha()
KRIZEK = pygame.image.load(
    os.path.join('Assets', 'krizek_hover.png')).convert_alpha()

font = pygame.font.Font('freesansbold.ttf', 32)
font_malinky = pygame.font.Font('freesansbold.ttf', 34)
font_maly = pygame.font.Font('freesansbold.ttf', 36)
font_malostredni = pygame.font.Font('freesansbold.ttf', 39)
font_stredni = pygame.font.Font('freesansbold.ttf', 45)
font_velky = pygame.font.Font('freesansbold.ttf', 47)
font_menu_info = pygame.font.SysFont('calibri.ttf', 22)
font_zpet_menu = pygame.font.SysFont('comicsans.ttf', 33)
font_zpet_menu_vetsi = pygame.font.SysFont('comicsans.ttf', 34)

TEXT = font.render(f"Počet nábojů: {zasobnik}", True, CERNA)
# TEXTP = (1640,1010)
BOOSTP = (1500, 1010)

HRANICE = pygame.Rect(0, 0, W, H)

KURZOR = pygame.image.load(
    os.path.join('Assets', 'kurzor.png')).convert_alpha()

RAKETKA1 = pygame.image.load(
    os.path.join('Assets', 'raketka.png')).convert_alpha()
RAKETKA2 = pygame.image.load(
    os.path.join('Assets', 'raketka2.png')).convert_alpha()
RAKETKA3 = pygame.image.load(
    os.path.join('Assets', 'raketka3.png')).convert_alpha()
RAKETKA3 = pygame.image.load(
    os.path.join('Assets', 'raketka3.png')).convert_alpha()
RAKETKA4 = pygame.image.load(
    os.path.join('Assets', 'raketka4.png')).convert_alpha()

PROJ = pygame.image.load(os.path.join('Assets', 'proj.png')).convert_alpha()
HYPERPROJ = pygame.image.load(
    os.path.join('Assets', 'hyperproj.png')).convert_alpha()

# EXPLOZE
EXPLOZE1 = pygame.image.load(os.path.join('Assets', 'e1.png')).convert_alpha()
EXPLOZE2 = pygame.image.load(os.path.join('Assets', 'e2.png')).convert_alpha()
EXPLOZE3 = pygame.image.load(os.path.join('Assets', 'e3.png')).convert_alpha()
EXPLOZE4 = pygame.image.load(os.path.join('Assets', 'e4.png')).convert_alpha()
EXPLOZE5 = pygame.image.load(os.path.join('Assets', 'e5.png')).convert_alpha()
EXPLOZE6 = pygame.image.load(os.path.join('Assets', 'e6.png')).convert_alpha()
EXPLOZE7 = pygame.image.load(os.path.join('Assets', 'e7.png')).convert_alpha()

# EXPLOZE BIG
EXPLOZE1 = pygame.transform.scale(EXPLOZE1, (50, 50))
EXPLOZE2 = pygame.transform.scale(EXPLOZE2, (70, 70))
EXPLOZE3 = pygame.transform.scale(EXPLOZE3, (100, 100))
EXPLOZE4 = pygame.transform.scale(EXPLOZE4, (150, 150))
EXPLOZE5 = pygame.transform.scale(EXPLOZE5, (200, 200))
EXPLOZE6 = pygame.transform.scale(EXPLOZE6, (150, 150))
EXPLOZE7 = pygame.transform.scale(EXPLOZE7, (150, 150))

ENEMY1 = pygame.image.load(
    os.path.join('Assets', 'enemak.png')).convert_alpha()
ENEMY2 = pygame.image.load(
    os.path.join('Assets', 'enemak2.png')).convert_alpha()
ENEMY1_BIG = pygame.transform.scale(ENEMY1, (50, 50))


def custom_okno(X, Y, sirka, vyska):
    return pygame.Rect(X, Y, sirka, vyska)


def custom_font(velikost):
    return pygame.font.Font('freesansbold.ttf', velikost)


def text_maker(font, zneni_textu):
    return font.render(zneni_textu, True, CERNA)


def button_with_text(OKNO, kulatost_okna, text):
    pygame.draw.rect(WIN, CERNA, OKNO, 2, kulatost_okna)
    pozice_text = text.get_rect(center=OKNO.center)
    WIN.blit(text, pozice_text)


def rychlostovac(cas, pocatecni_cas):
    return (cas - pocatecni_cas) / 550000


def pozicovac_enemaku_chytry_beta(n1, n2, X, Y, enemy_rychlost):
    nt = math.atan2(X - n1,
                    Y - n2) * 180 / 3.141592653589793238462643383279502884197 + 270
    incn1 = math.cos(math.radians(nt))
    incn2 = -math.sin(math.radians(nt))
    n1 += incn1 * enemy_rychlost
    n2 += incn2 * enemy_rychlost
    return n1, n2


def pozicovac_enemaku(n1, n2, c1, c2, enemy_rychlost):
    nt = math.atan2(c1 - n1,
                    c2 - n2) * 180 / 3.141592653589793238462643383279502884197 + 270
    incn1 = math.cos(math.radians(nt))
    incn2 = -math.sin(math.radians(nt))
    n1 += incn1 * enemy_rychlost
    n2 += incn2 * enemy_rychlost
    return n1, n2;


def pozicovac_strel(c1, c2):
    start_posX, start_posY = pygame.mouse.get_pos()
    rotace_strely = math.atan2(start_posX - c1,
                               start_posY - c2) * 180 / math.pi + 270
    incp1 = math.cos(math.radians(rotace_strely))
    incp2 = -math.sin(math.radians(rotace_strely))
    p1, p2 = incp1 * 40 + c1, incp2 * 40 + c2
    return p1, p2, incp1, incp2, rotace_strely


def strilej(p1, p2, at):
    rotace = pygame.transform.rotate(PROJ, at)
    obraz = rotace.get_rect(center=(p1, p2))
    WIN.blit(rotace, obraz)
    return obraz


def hyperstrilej(p1, p2, at):
    rotace = pygame.transform.rotate(HYPERPROJ, at)
    obraz = rotace.get_rect(center=(p1, p2))
    WIN.blit(rotace, obraz)
    return obraz


def draw_window(barva, X, Y, tru, rt, c1, c2):
    # WIN.fill(barva)
    if tru == 1:
        raketka = pygame.transform.rotate(RAKETKA1, rt)
    elif tru == 3:
        raketka = pygame.transform.rotate(RAKETKA3, rt)
    elif tru == 4:
        raketka = pygame.transform.rotate(RAKETKA4, rt)
    else:
        raketka = pygame.transform.rotate(RAKETKA2, rt)
    pozice = raketka.get_rect(center=(c1, c2))
    WIN.blit(raketka, pozice)
    pygame.draw.rect(WIN, CERNA, HRANICE, 2)
    enemy = ENEMY1_BIG.get_rect(center=(550, 550))
    kurzor = KURZOR.get_rect(center=(X, Y))
    kurzor.center = (X, Y)
    WIN.blit(KURZOR, kurzor)
    return pozice


font_boost = pygame.font.Font("freesansbold.ttf", 25)


def draw_text(zasobnik, zasobnik_max, vyhral, prohral, level):
    WIN.blit(
        font.render(f"Počet nábojů: {zasobnik_max - zasobnik}", True, CERNA),
        (W - 280, H - 70))
    WIN.blit(font_zpet_menu_vetsi.render(f"LEVEL: {level}", True, CERNA),
             (W - 280, H - 40))
    WIN.blit(font_boost.render("ENERGIE:", True, CERNA), (17, H - 54))


def boost_timer(time_boost, BOOSTP):
    pygame.draw.rect(WIN, LIME, pygame.Rect(150, H - 53, time_boost, 22), 0)
    pygame.draw.rect(WIN, CERNA, pygame.Rect(150, H - 53, 185, 22), 3)


def animace_exploze(e1, e2, doba_vybuchu, exploze, cil):
    prvni = 1
    druhy = 3
    treti = 5
    ctvrty = 8
    paty = 12
    sesty = 14
    sedmy = 16
    # POZICE = EXPLOZE1.get_rect(center=(e1, e2))
    if prvni > doba_vybuchu >= 0:
        POZICE = EXPLOZE1.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE1, POZICE)
    elif druhy > doba_vybuchu >= prvni:
        POZICE = EXPLOZE2.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE2, POZICE)
    elif treti > doba_vybuchu >= druhy:
        POZICE = EXPLOZE3.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE3, POZICE)
    elif ctvrty > doba_vybuchu >= treti:
        POZICE = EXPLOZE4.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE4, POZICE)
    elif paty > doba_vybuchu >= ctvrty:
        POZICE = EXPLOZE5.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE5, POZICE)
    elif sesty > doba_vybuchu >= paty:
        POZICE = EXPLOZE6.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE6, POZICE)
    elif sedmy > doba_vybuchu >= sesty:
        POZICE = EXPLOZE7.get_rect(center=(e1, e2))
        WIN.blit(EXPLOZE7, POZICE)
    elif sedmy == doba_vybuchu:
        exploze = False
        POZICE_EXPLOZE = EXPLOZE1.get_rect(center=(0, -1000))
        return exploze, doba_vybuchu, POZICE_EXPLOZE
    doba_vybuchu += 1
    POZICE_EXPLOZE = POZICE
    return exploze, doba_vybuchu, POZICE_EXPLOZE


def animace_pohonu(vxa, vya):
    stop = 0.003
    slow = 0.05
    med = 0.9
    if vya * vxa <= stop:
        return 2
    elif med >= vxa * vya > slow:
        return 3
    elif slow > vxa * vya > stop:
        return 4
    else:
        return 1


def otacec(p1, p2, incp1, incp2, at):
    if p1 < 1 and p2 < 1:
        incp1 *= -1 + random.randrange(-10, 10) / 1000
        incp2 *= -1 + random.randrange(-10, 10) / 1000
        return incp1, incp2, at
    if p1 > W and p2 > H:
        incp1 *= -1 + random.randrange(-10, 10) / 1000
        incp2 *= -1 + random.randrange(-10, 10) / 1000
        return incp1, incp2, at
    if p1 < 1 and p2 > H:
        incp1 *= -1 + random.randrange(-10, 10) / 1000
        incp2 *= -1 + random.randrange(-10, 10) / 1000
        return incp1, incp2, at
    if p1 > W and p2 < 1:
        incp1 *= -1 + random.randrange(-10, 10) / 1000
        incp2 *= -1 + random.randrange(-10, 10) / 1000
        return incp1, incp2, at
    if p1 < 1 or p1 > W:
        incp1 = incp1 * (-1) + random.randrange(-10, 10) / 1000
        at = (180 - at)
        return incp1, incp2, at
    if p2 < 1 or p2 > H:
        incp2 = incp2 * (-1) + random.randrange(-10, 10) / 1000
        at = (-at)
        return incp1, incp2, at
    else:
        return incp1, incp2, at


def limit(num, minimum=-2, maximum=2):
    return min(max(num, maximum), minimum)


def clever_enemy(n1, n2):
    pozice = ENEMY2.get_rect(center=(n1, n2))
    WIN.blit(ENEMY2, pozice)
    return pozice


def basic_enemy(n1, n2):
    pozice = ENEMY1.get_rect(center=(n1, n2))
    WIN.blit(ENEMY1, pozice)
    return pozice


def tlusty_enemy(n1, n2, zivoty):
    pozice = ENEMY1_BIG.get_rect(center=(n1, n2))
    WIN.blit(ENEMY1_BIG, pozice)
    pygame.draw.rect(WIN, "#ff0000", pygame.Rect(n1 - 25, n2 - 40, 50, 8), 0)
    pygame.draw.rect(WIN, LIME,
                     pygame.Rect(n1 - 25, n2 - 40, 0 + zivoty * 17, 8), 0)
    return pozice


medailon = False
obtiznost = "tezka"


def main(medailon, obtiznost):  # rkt = pygame.Rect(200,200,50,50)
    # rkt.center = (50,50)F
    global kurzor
    smrtelnost_run = True
    explodovac = 1
    pozice_expl = ENEMY2.get_rect(center=(-20, -20))
    pozice = ENEMY2.get_rect(center=(W, H))
    zvyšovač = False
    volume = 0.0
    clock = pygame.time.Clock()
    doba_vybuchu = 0
    casovac = 0
    ano = True
    neblituj = True
    run = True
    exploze = False
    hyper = False
    stav_pohonu = 1
    timer = 0
    boost_tick = 3
    boost_cooldown = 1 / boost_tick * 3000
    n = 0
    m = 0
    k = 0
    l = 0
    treni = 0.7
    e1, e2 = -100, -100
    c1, c2 = pygame.mouse.get_pos()
    p1, p2 = 0, 0
    incp1, incp2 = 0, 0
    rychlost_rakety_x, rychlost_rakety_y = 0, 0
    start_posX, start_posY = 0, 0
    sps1, sps2 = 0, 0
    at = 0
    rychlost_p1 = 5
    rychlost_p2 = 5
    strileni = []
    zasobnik_max = 4
    zasobnik = 0
    zasobnik_displ = zasobnik
    smrtelnost = True
    boost = False
    vyhral = False
    prohral = False
    menu = True
    pause = False
    klikani_smrtelnost = True
    smrtelnost_ukazatel = PROJSMRTELNOST
    time_boost = 185
    level = 1
    BOOSTP = (1500, 1010)
    TEXTP = (1620, 1010)

    basic = [0, 3, 5, 7, 9, 11, 13, 15, 17, 11, 21]
    chytry = [0, 1, 2, 1, 3, 11, 5, 7, 10, 11, 21]
    tlusty = [0, 0, 0, 1, 2, 0, 4, 5, 5, 11, 21]

    LEVELY = [list(x) for x in zip(basic, chytry, tlusty)]
    NEPRATELE = []
    print(LEVELY)

    while run:
        WIN.fill(SSBILA)
        clock.tick(FPS)  # pzn.1
        pygame.mouse.set_visible(False)

        while menu == True:
            WIN.fill(SSBILA)
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        print(f"X,Y: {X, Y}")
                        sys.exit()

            X, Y = pygame.mouse.get_pos()
            kurzor = KURZOR.get_rect(center=(X, Y))

            if menu == True:
                # NADPIS
                nadpis = NADPIS.get_rect(center=(762, 193))
                WIN.blit(NADPIS, nadpis)

                # MEDAILE
                if medailon == True:
                    MEDAILE2 = pygame.transform.scale(MEDAILE, (100, 100))
                    medaile = MEDAILE2.get_rect(center=(40, 60))
                    WIN.blit(MEDAILE2, medaile)

                # PLAY BUTTON
                hrat = text_maker(font_stredni, "Hrát hru")
                button_with_text(START_OKNO, 10, hrat)
                if kurzor.colliderect(START_OKNO):
                    WIN.fill(SBILA, START_OKNO)
                    hrat = text_maker(custom_font(49), "Hrát hru")
                    button_with_text(START_OKNO, 12, hrat)
                    try:
                        if event.type == pygame.MOUSEBUTTONUP:
                            menu = False
                            c1, c2 = X, Y
                            pocatecni_cas = pygame.time.get_ticks()
                            continue
                    except:
                        pygame.event.peek()

                # Obtížnost
                obtiznost_text = font_maly.render("Obtížnost", True, CERNA)
                button_with_text(OBTIZNOST_OKNO, 10, obtiznost_text)
                try:
                    if kurzor.colliderect(OBTIZNOST_OKNO):
                        WIN.fill(SBILA, OBTIZNOST_OKNO)
                        obtiznost_text = font_malostredni.render("Obtížnost",
                                                                 True, CERNA)
                        button_with_text(OBTIZNOST_OKNO, 12, obtiznost_text)
                        if event.type == pygame.MOUSEBUTTONUP:
                            while run:
                                WIN.fill(SSBILA)
                                clock.tick(FPS)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        run = False
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            run = False
                                            sys.exit()

                                pauza = font_velky.render("Zvol si obtížnost",
                                                          True, CERNA)
                                pozice_pauza = pauza.get_rect(
                                    center=(W // 2 - 10, H // 2 - 150))
                                WIN.blit(pauza, pozice_pauza)
                                LEHKA_OKNO = pygame.draw.rect(WIN, CERNA, (
                                    W / 2 - 318, H - 450, 203, 65), 2, 15)
                                STREDNI_OKNO = pygame.draw.rect(WIN, CERNA, (
                                    W / 2 - 108, H - 450, 203, 65), 2, 15)
                                TEZKA_OKNO = pygame.draw.rect(WIN, CERNA, (
                                    W / 2 + 102, H - 450, 203, 65), 2, 15)

                                lehke_okno = font_zpet_menu.render("Lehká",
                                                                   True, CERNA)
                                pozice_lehke_okno = lehke_okno.get_rect(
                                    center=LEHKA_OKNO.center)
                                WIN.blit(lehke_okno, pozice_lehke_okno)

                                stredni_okno = font_zpet_menu.render("Střední",
                                                                     True,
                                                                     CERNA)
                                pozice_stredni_okno = stredni_okno.get_rect(
                                    center=STREDNI_OKNO.center)
                                WIN.blit(stredni_okno, pozice_stredni_okno)

                                tezke_okno = font_zpet_menu.render("Těžká",
                                                                   True, CERNA)
                                pozice_tezke_okno = tezke_okno.get_rect(
                                    center=TEZKA_OKNO.center)
                                WIN.blit(tezke_okno, pozice_tezke_okno)

                                # LEHKÁ OBTÍŽNOST
                                if kurzor.colliderect(LEHKA_OKNO):
                                    pozice_info = (W / 2 - 190, H - 327)
                                    WIN.fill(SBILA, LEHKA_OKNO)
                                    pygame.draw.rect(WIN, CERNA, LEHKA_OKNO, 2,
                                                     16)
                                    zpet_menu = font_zpet_menu_vetsi.render(
                                        "Lehká", True, CERNA)
                                    pozice_zpet_menu = zpet_menu.get_rect(
                                        center=LEHKA_OKNO.center)
                                    WIN.blit(zpet_menu, pozice_zpet_menu)
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        pause = True
                                        menu = False
                                        obtiznost = "lehka"
                                        main(medailon, obtiznost)

                                # STŘEDNÍ OBTÍŽNOST
                                if kurzor.colliderect(STREDNI_OKNO):
                                    pozice_info = (W / 2 - 190, H - 327)
                                    WIN.fill(SBILA, STREDNI_OKNO)
                                    pygame.draw.rect(WIN, CERNA, STREDNI_OKNO,
                                                     2, 16)
                                    zpet_menu = font_zpet_menu_vetsi.render(
                                        "Střední", True, CERNA)
                                    pozice_zpet_menu = zpet_menu.get_rect(
                                        center=STREDNI_OKNO.center)
                                    WIN.blit(zpet_menu, pozice_zpet_menu)
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        pause = True
                                        menu = False
                                        obtiznost = "stredni"
                                        main(medailon, obtiznost)

                                # TEZKA OBTIZNOST
                                if kurzor.colliderect(TEZKA_OKNO):
                                    pozice_info = (W / 2 - 190, H - 327)
                                    WIN.fill(SBILA, TEZKA_OKNO)
                                    pygame.draw.rect(WIN, CERNA, TEZKA_OKNO, 2,
                                                     16)
                                    zpet_menu = font_zpet_menu_vetsi.render(
                                        "Těžká", True, CERNA)
                                    pozice_zpet_menu = zpet_menu.get_rect(
                                        center=TEZKA_OKNO.center)
                                    WIN.blit(zpet_menu, pozice_zpet_menu)
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        pause = True
                                        menu = False
                                        obtiznost = "tezka"
                                        main(medailon, obtiznost)

                                X, Y = pygame.mouse.get_pos()
                                kurzor = KURZOR.get_rect(center=(X, Y))
                                WIN.blit(KURZOR, kurzor)
                                pygame.display.update()
                except:
                    pygame.event.peek()

                # KRIZEK
                krizek = KRIZEK.get_rect(center=OPUSTIT_HRU_OKNO.center)
                WIN.blit(KRIZEK, krizek)
                if kurzor.colliderect(OPUSTIT_HRU_OKNO):
                    krizek_hover = KRIZEK_HOVER.get_rect(
                        center=OPUSTIT_HRU_OKNO.center)
                    WIN.blit(KRIZEK_HOVER, krizek_hover)
                    quit_info = font_menu_info.render("Ukončit hru.", True,
                                                      CERNA)
                    WIN.blit(quit_info, (W - 145, 20))
                    if event.type == pygame.MOUSEBUTTONUP:
                        run = False
                        sys.exit()

                # NASTAVENI SMRTELNOSTI
                WIN.blit(smrtelnost_ukazatel, (W - 100, H - 95))
                if kurzor.colliderect(NASTAVENI_SMRTELNOSTI):
                    if smrtelnost_run == True:
                        smrtelnost_info = text_maker(font_menu_info,
                                                     "Vypni smrtelnost vůči projektilům")
                        smrtelnost_ukazatel = PROJSMRTELNOST
                    else:
                        smrtelnost_info = text_maker(font_menu_info,
                                                     "Zapni smrtelnost vůči projektilům")
                        smrtelnost_ukazatel = PROJSMRTELNOST_SKRT
                    WIN.blit(smrtelnost_info, (W - 345, H - 50))
                    if event.type == pygame.MOUSEBUTTONDOWN and klikani_smrtelnost == True:
                        klikani_smrtelnost = False
                        smrtelnost_run = not smrtelnost_run
                        smrtelnost = not smrtelnost
                    if event.type == pygame.MOUSEBUTTONUP:
                        klikani_smrtelnost = True

                # CONTROLS
                napoveda = font.render("Jak hrát?", True, CERNA)
                button_with_text(OVLADANI_OKNO, 10, napoveda)
                if kurzor.colliderect(OVLADANI_OKNO):
                    WIN.fill(SBILA, OVLADANI_OKNO)
                    napoveda = font_malinky.render("Jak hrát?", True, CERNA)
                    button_with_text(OVLADANI_OKNO, 12, napoveda)
                    # if event.type == pygame.MOUSEBUTTONUP:
                    WIN.blit(NAPOVEDA, (0, 0))
                    neblituj = True

            if neblituj == False:
                WIN.blit(KURZOR, kurzor)
            else:
                neblituj = False
            pygame.display.update()

        # PAUSE MENU
        grom = pygame.time.get_ticks()
        while pause == True:
            if volume > 0.07:
                volume -= 0.01
            WIN.fill(SSBILA)
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        sys.exit()
                    if event.key == pygame.K_p:
                        pocatecni_cas += pygame.time.get_ticks() - grom
                        zvyšovač = True
                        pause = not pause

                        # menu = True
                        pygame.display.update()
                        break

            X, Y = pygame.mouse.get_pos()
            kurzor = KURZOR.get_rect(center=(X, Y))

            # NASTAVENI SMRTELNOSTI
            WIN.blit(smrtelnost_ukazatel, (W - 100, H - 95))
            if kurzor.colliderect(NASTAVENI_SMRTELNOSTI):
                if smrtelnost_run == True:
                    smrtelnost_info = text_maker(font_menu_info,
                                                 "Vypni smrtelnost vůči projektilům")
                    smrtelnost_ukazatel = PROJSMRTELNOST
                else:
                    smrtelnost_info = text_maker(font_menu_info,
                                                 "Zapni smrtelnost vůči projektilům")
                    smrtelnost_ukazatel = PROJSMRTELNOST_SKRT
                WIN.blit(smrtelnost_info, (W - 345, H - 50))
                if event.type == pygame.MOUSEBUTTONDOWN and klikani_smrtelnost == True:
                    klikani_smrtelnost = False
                    smrtelnost_run = not smrtelnost_run
                    smrtelnost = not smrtelnost
                if event.type == pygame.MOUSEBUTTONUP:
                    klikani_smrtelnost = True

            zpet_menu_info = font_menu_info.render(
                "Návratem do menu přijdeš o svůj dosavadní postup.", True,
                CERNA)
            pauza = font_maly.render("Pauza", True, CERNA)
            pozice_pauza = pauza.get_rect(center=(W // 2 - 10, H // 2 - 20))
            WIN.blit(pauza, pozice_pauza)

            ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA,
                                              (W / 2 - 145, H - 400, 273, 65),
                                              2, 15)
            zpet_menu = font_zpet_menu.render("Zpět do hlavního menu", True,
                                              CERNA)
            pozice_zpet_menu = zpet_menu.get_rect(center=ZPET_MENU_OKNO.center)
            WIN.blit(zpet_menu, pozice_zpet_menu)

            # KRIZEK PAUSE MENU
            krizek = KRIZEK.get_rect(center=OPUSTIT_HRU_OKNO.center)
            WIN.blit(KRIZEK, krizek)
            if kurzor.colliderect(OPUSTIT_HRU_OKNO):
                krizek_hover = KRIZEK_HOVER.get_rect(
                    center=OPUSTIT_HRU_OKNO.center)
                WIN.blit(KRIZEK_HOVER, krizek_hover)
                pauza_info = font_menu_info.render("Pauzu lze také přerušit",
                                                   True, CERNA)
                pauza_info2 = font_menu_info.render(
                    "opětovným stisknutím \"P\"", True, CERNA)
                WIN.blit(pauza_info, (W - 245, 16))
                WIN.blit(pauza_info2, (W - 245, 36))

            # # KONEC PAUZY
            # if event.type == pygame.KEYDOWN and pause == True:
            #     if event.key == pygame.K_p:
            #         pause = False
            #         menu = False

            # ZPATKY DO MENU
            if kurzor.colliderect(ZPET_MENU_OKNO):
                pozice_info = (W / 2 - 190, H - 327)
                WIN.blit(zpet_menu_info, pozice_info)
                WIN.fill(SBILA, ZPET_MENU_OKNO)
                pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2, 16)
                zpet_menu = font_zpet_menu_vetsi.render(
                    "Zpět do hlavního menu", True, CERNA)
                pozice_zpet_menu = zpet_menu.get_rect(
                    center=ZPET_MENU_OKNO.center)
                WIN.blit(zpet_menu, pozice_zpet_menu)
                if event.type == pygame.MOUSEBUTTONUP:
                    pause = True
                    menu = False
                    level = 0
                    pygame.display.update()
                    main(medailon, obtiznost)

            WIN.blit(KURZOR, kurzor)
            pygame.display.update()

        # MENU
        grom = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    sys.exit()
                if event.key == pygame.K_SPACE and (
                        pygame.time.get_ticks() - timer) > boost_cooldown:
                    boost = True
                    timer = pygame.time.get_ticks()
                    time_boost = 0
                if event.key == pygame.K_p:
                    pocatecni_cas += pygame.time.get_ticks() - grom
                    pause = True
                    # menu = False
            if event.type == pygame.MOUSEBUTTONUP:
                # cp1,cp2 = p1,p2
                if event.button == 3:
                    if (pygame.time.get_ticks() - timer) > boost_cooldown:
                        start_posX, start_posY = pygame.mouse.get_pos()
                        at = math.atan2(start_posX - c1,
                                        start_posY - c2) * 180 / 3.141592653589793238462643383279502884197 + 270
                        incp1 = math.cos(math.radians(at))
                        incp2 = -math.sin(math.radians(at))
                        p1, p2 = incp1 * 40 + c1, incp2 * 40 + c2
                        boost = False
                        vystrelena = False
                        timer = pygame.time.get_ticks()
                        time_boost = 0
                        hyper = True
                    else:
                        break

                if event.button == 1:
                    p1, p2, incp1, incp2, at = pozicovac_strel(c1, c2)
                    hyper = False
                    vystrelena = True
                if zasobnik < zasobnik_max:
                    vystrelena = True
                    strileni.insert(zasobnik, [p1, p2, incp1, incp2, at, hyper,
                                               vystrelena])
                    zasobnik += 1
                    zasobnik_displ = zasobnik_max - zasobnik
                    hyper = False
                if zasobnik == zasobnik_max:
                    zasobnik_displ = "max"

        if time_boost < 184:
            time_boost += boost_tick

        X, Y = pygame.mouse.get_pos()

        zrychleni_rakety_x = (X - c1) / 200
        zrychleni_rakety_y = (Y - c2) / 200
        rt = math.atan2(X - c1,
                        Y - c2) * 180 / 3.141592653589793238462643383279502884197 + 270

        #if abs(zrychleni_rakety_x) > 2.5:
        #    treni = 1.75 / abs(zrychleni_rakety_x)

        rychlost_rakety_x += zrychleni_rakety_x
        rychlost_rakety_y += zrychleni_rakety_y

        rychlost_rakety_x *= treni
        rychlost_rakety_y *= treni

        vxa = abs(zrychleni_rakety_x)
        vya = abs(zrychleni_rakety_y)

        stav_pohonu = animace_pohonu(vxa, vya)

        if boost == True:
            rychlost_rakety_x += math.cos(math.radians(rt)) * 40
            rychlost_rakety_y += -math.sin(math.radians(rt)) * 40
            stav_pohonu = 1
        boost = False
        c1 += rychlost_rakety_x
        c2 += rychlost_rakety_y
        P1, P2, INCP1, INCP2, AT = 0, 1, 2, 3, 4

        rotovana_raketa = pygame.transform.rotate(RAKETKA2, rt)
        raketka = rotovana_raketa.get_rect(center=(c1, c2))
        for enemak in NEPRATELE:
            N1 = enemak[1]
            N2 = enemak[2]
            enemak_rect = ENEMY1.get_rect(center=(N1, N2))
            if enemak_rect.colliderect(raketka):
                while run:
                    WIN.fill(SSBILA)
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                run = False
                                sys.exit()

                    pauza = font_maly.render("Prohrál jsi", True, CERNA)
                    pozice_pauza = pauza.get_rect(
                        center=(W // 2 - 10, H // 2 - 20))
                    WIN.blit(pauza, pozice_pauza)

                    ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA, (
                        W / 2 - 145, H - 400, 273, 65), 2, 15)
                    zpet_menu = font_zpet_menu.render("Zpět do hlavního menu",
                                                      True, CERNA)
                    pozice_zpet_menu = zpet_menu.get_rect(
                        center=ZPET_MENU_OKNO.center)
                    WIN.blit(zpet_menu, pozice_zpet_menu)
                    if kurzor.colliderect(ZPET_MENU_OKNO):
                        pozice_info = (W / 2 - 190, H - 327)
                        WIN.fill(SBILA, ZPET_MENU_OKNO)
                        pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2, 16)
                        zpet_menu = font_zpet_menu_vetsi.render(
                            "Zpět do hlavního menu", True, CERNA)
                        pozice_zpet_menu = zpet_menu.get_rect(
                            center=ZPET_MENU_OKNO.center)
                        WIN.blit(zpet_menu, pozice_zpet_menu)
                        if event.type == pygame.MOUSEBUTTONUP:
                            pause = True
                            menu = False
                            level = 0
                            pygame.display.update()
                            # pygame.mixer.music.unload()
                            main(medailon, obtiznost)

                    X, Y = pygame.mouse.get_pos()
                    kurzor = KURZOR.get_rect(center=(X, Y))
                    WIN.blit(KURZOR, kurzor)
                    pygame.display.update()

        for strela in strileni:
            strela[INCP1], strela[INCP2], strela[AT] = otacec(strela[P1],
                                                              strela[P2],
                                                              strela[INCP1],
                                                              strela[INCP2],
                                                              strela[AT])
            strela[P1] += strela[INCP1] * rychlost_p1 * 1.2
            strela[P2] += strela[INCP2] * rychlost_p2 * 1.2
            obraz = PROJ.get_rect(center=(strela[P1], strela[P2]))
            if obraz.colliderect(raketka) == False:
                strela[6] = False
            if strela[5] == False:
                strilej(strela[P1], strela[P2], strela[AT])
                if obraz.colliderect(raketka) == True and strela[6] == False:
                    if smrtelnost == True:
                        while run:
                            WIN.fill(SSBILA)
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        run = False
                                        sys.exit()

                            pauza = font_maly.render("Střelil jsi se!", True,
                                                     CERNA)
                            pozice_pauza = pauza.get_rect(
                                center=(W // 2 - 10, H // 2 - 20))
                            WIN.blit(pauza, pozice_pauza)

                            ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA, (
                                W / 2 - 145, H - 400, 273, 65), 2, 15)
                            zpet_menu = font_zpet_menu.render(
                                "Zpět do hlavního menu", True, CERNA)
                            pozice_zpet_menu = zpet_menu.get_rect(
                                center=ZPET_MENU_OKNO.center)
                            WIN.blit(zpet_menu, pozice_zpet_menu)
                            if kurzor.colliderect(ZPET_MENU_OKNO):
                                pozice_info = (W / 2 - 190, H - 327)
                                WIN.fill(SBILA, ZPET_MENU_OKNO)
                                pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2,
                                                 16)
                                zpet_menu = font_zpet_menu_vetsi.render(
                                    "Zpět do hlavního menu", True, CERNA)
                                pozice_zpet_menu = zpet_menu.get_rect(
                                    center=ZPET_MENU_OKNO.center)
                                WIN.blit(zpet_menu, pozice_zpet_menu)
                                if event.type == pygame.MOUSEBUTTONUP:
                                    pause = True
                                    menu = False
                                    level = 0
                                    pygame.display.update()
                                    # pygame.mixer.music.unload()
                                    main(medailon, obtiznost)

                            X, Y = pygame.mouse.get_pos()
                            kurzor = KURZOR.get_rect(center=(X, Y))
                            WIN.blit(KURZOR, kurzor)
                            pygame.display.update()
                for enemak in NEPRATELE:
                    N1 = enemak[1]
                    N2 = enemak[2]
                    enemak_big_rect = ENEMY1_BIG.get_rect(center=(N1, N2))
                    enemak_rect = ENEMY1.get_rect(center=(N1, N2))

                    # PROJ KOLIZE S ENEMAKY
                    if obraz.colliderect(
                            enemak_rect) == True and NEPRATELE != []:
                        if strela in strileni:
                            strileni.remove(strela)
                            zasobnik -= 1
                            zasobnik_displ = zasobnik
                            if enemak[0] != "tlusty":
                                NEPRATELE.remove(enemak)
                            else:
                                enemak[3] -= 1
                                if enemak[3] == 0:
                                    NEPRATELE.remove(enemak)

            else:
                hyperstrilej(strela[P1], strela[P2], strela[AT])
                if obraz.colliderect(raketka) == True and strela[6] == False:
                    exploze = True
                    cil = raketka
                    strileni.remove(strela)
                    e1, e2 = strela[P1], strela[P2]
                    doba_vybuchu = 0
                    zasobnik -= 1
                    zasobnik_displ = zasobnik
                    if smrtelnost == True:

                        while run:
                            WIN.fill(SSBILA)
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        run = False
                                        sys.exit()

                            pauza = font_maly.render("Střelil jsi se!", True,
                                                     CERNA)
                            pozice_pauza = pauza.get_rect(
                                center=(W // 2 - 10, H // 2 - 20))
                            WIN.blit(pauza, pozice_pauza)

                            ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA, (
                                W / 2 - 145, H - 400, 273, 65), 2, 15)
                            zpet_menu = font_zpet_menu.render(
                                "Zpět do hlavního menu", True, CERNA)
                            pozice_zpet_menu = zpet_menu.get_rect(
                                center=ZPET_MENU_OKNO.center)
                            WIN.blit(zpet_menu, pozice_zpet_menu)
                            if kurzor.colliderect(ZPET_MENU_OKNO):
                                pozice_info = (W / 2 - 190, H - 327)
                                WIN.fill(SBILA, ZPET_MENU_OKNO)
                                pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2,
                                                 16)
                                zpet_menu = font_zpet_menu_vetsi.render(
                                    "Zpět do hlavního menu", True, CERNA)
                                pozice_zpet_menu = zpet_menu.get_rect(
                                    center=ZPET_MENU_OKNO.center)
                                WIN.blit(zpet_menu, pozice_zpet_menu)
                                if event.type == pygame.MOUSEBUTTONUP:
                                    pause = True
                                    menu = False
                                    level = 0
                                    pygame.display.update()
                                    # pygame.mixer.music.unload()
                                    main(medailon, obtiznost)

                            X, Y = pygame.mouse.get_pos()
                            kurzor = KURZOR.get_rect(center=(X, Y))
                            WIN.blit(KURZOR, kurzor)
                            pygame.display.update()
                for enemak in NEPRATELE:
                    N1 = enemak[1]
                    N2 = enemak[2]
                    enemak_rect = ENEMY1.get_rect(center=(N1, N2))
                    enemak_big_rect = ENEMY1_BIG.get_rect(center=(N1, N2))

                    # HYPERPROJ KOLIZE S ENEMAKY
                    if obraz.colliderect(
                            enemak_big_rect) == True and NEPRATELE != []:
                        if enemak[0] != "tlusty":
                            NEPRATELE.remove(enemak)
                        else:
                            enemak[3] -= 1
                            if enemak[3] == 0:
                                NEPRATELE.remove(enemak)
                        strileni.remove(strela)
                        exploze = True
                        cil = raketka
                        e1, e2 = strela[P1], strela[P2]
                        doba_vybuchu = 0
                        zasobnik -= 1
                        zasobnik_displ = zasobnik
                        break

        N1 = 1
        N2 = 2

        # VYKRESLOVACÍ FORLOOP
        for enemak in NEPRATELE:
            # X,Y = pygame.mouse.get_pos()
            if pygame.time.get_ticks() - enemak[4] > 500:
                enemak[4] = 0

            if enemak[0] == "chytry" and enemak[4] == 0:
                enemy_rychlost = 0.65 + rychlostovac(pygame.time.get_ticks(),
                                                     pocatecni_cas)
                enemak[N1], enemak[N2] = pozicovac_enemaku_chytry_beta(
                    enemak[N1], enemak[N2], X, Y, enemy_rychlost)
                # pozicovac_enemaku(enemak[N1], enemak[N2], c1, c2, enemy_rychlost)
                pozice = clever_enemy(enemak[N1], enemak[N2]);

            elif enemak[0] == "tlusty" and enemak[4] == 0:
                enemy_rychlost = 0.5 + rychlostovac(pygame.time.get_ticks(),
                                                    pocatecni_cas)
                enemak[N1], enemak[N2] = pozicovac_enemaku(enemak[N1],
                                                           enemak[N2], c1, c2,
                                                           enemy_rychlost)
                pozice = tlusty_enemy(enemak[N1], enemak[N2], enemak[3])

            elif enemak[0] == "basic" and enemak[4] == 0:
                enemy_rychlost = 0.65 + rychlostovac(pygame.time.get_ticks(),
                                                     pocatecni_cas)
                enemak[N1], enemak[N2] = pozicovac_enemaku(enemak[N1],
                                                           enemak[N2], c1, c2,
                                                           enemy_rychlost)
                pozice = basic_enemy(enemak[N1], enemak[N2])

            if pozice_expl.colliderect(pozice) and NEPRATELE != []:
                if enemak[0] != "tlusty":
                    NEPRATELE.remove(enemak)
                else:
                    enemak[3] -= 1
                    if enemak[3] == 0:
                        NEPRATELE.remove(enemak)

        # EXPLOZE KOLIZE S ENEMAKEM
        if exploze:
            exploze, doba_vybuchu, pozice_expl = animace_exploze(e1, e2,
                                                                 doba_vybuchu,
                                                                 exploze, cil)
        # if not exploze or NEPRATELE == []:
        #     pozice_expl = ENEMY1.get_rect(center=(-150, -150))

        print(pozice, pozice_expl)

        if pozice_expl.colliderect(raketka):
            if explodovac < 11:
                explodovac += 1
            else:
                while run:
                    WIN.fill(SSBILA)
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                run = False
                                sys.exit()

                    pauza = font_maly.render("Vybouchl jsi!", True, CERNA)
                    pozice_pauza = pauza.get_rect(
                        center=(W // 2 - 10, H // 2 - 20))
                    WIN.blit(pauza, pozice_pauza)

                    ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA, (
                        W / 2 - 145, H - 400, 273, 65), 2, 15)
                    zpet_menu = font_zpet_menu.render("Zpět do hlavního menu",
                                                      True, CERNA)
                    pozice_zpet_menu = zpet_menu.get_rect(
                        center=ZPET_MENU_OKNO.center)
                    WIN.blit(zpet_menu, pozice_zpet_menu)
                    if kurzor.colliderect(ZPET_MENU_OKNO):
                        pozice_info = (W / 2 - 190, H - 327)
                        WIN.fill(SBILA, ZPET_MENU_OKNO)
                        pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2, 16)
                        zpet_menu = font_zpet_menu_vetsi.render(
                            "Zpět do hlavního menu", True, CERNA)
                        pozice_zpet_menu = zpet_menu.get_rect(
                            center=ZPET_MENU_OKNO.center)
                        WIN.blit(zpet_menu, pozice_zpet_menu)
                        if event.type == pygame.MOUSEBUTTONUP:
                            pause = True
                            menu = False
                            level = 0
                            pygame.display.update()
                            # pygame.mixer.music.unload()
                            main(medailon, obtiznost)

                    X, Y = pygame.mouse.get_pos()
                    kurzor = KURZOR.get_rect(center=(X, Y))
                    WIN.blit(KURZOR, kurzor)
                    pygame.display.update()

        if (obtiznost == "tezka" and level == 11) or (
                obtiznost == "stredni" and level == 8) or (
                obtiznost == "lehka" and level == 6):
            while run:
                WIN.fill(SSBILA)
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            sys.exit()

                pauza = font_velky.render("Vyhrál jsi!", True, CERNA)
                pozice_pauza = pauza.get_rect(
                    center=(W // 2 - 10, H // 2 - 150))
                WIN.blit(pauza, pozice_pauza)
                MEDAILE2 = pygame.transform.scale(MEDAILE, (100, 100))
                medaile = MEDAILE2.get_rect(center=(W / 2 - 15, H - 480))
                WIN.blit(MEDAILE2, medaile)
                medailon = True

                ZPET_MENU_OKNO = pygame.draw.rect(WIN, CERNA, (
                    W / 2 - 145, H - 400, 273, 65), 2, 15)
                zpet_menu = font_zpet_menu.render("Zpět do hlavního menu",
                                                  True, CERNA)
                pozice_zpet_menu = zpet_menu.get_rect(
                    center=ZPET_MENU_OKNO.center)
                WIN.blit(zpet_menu, pozice_zpet_menu)
                if kurzor.colliderect(ZPET_MENU_OKNO):
                    pozice_info = (W / 2 - 190, H - 327)
                    WIN.fill(SBILA, ZPET_MENU_OKNO)
                    pygame.draw.rect(WIN, CERNA, ZPET_MENU_OKNO, 2, 16)
                    zpet_menu = font_zpet_menu_vetsi.render(
                        "Zpět do hlavního menu", True, CERNA)
                    pozice_zpet_menu = zpet_menu.get_rect(
                        center=ZPET_MENU_OKNO.center)
                    WIN.blit(zpet_menu, pozice_zpet_menu)
                    if event.type == pygame.MOUSEBUTTONUP:
                        pause = True
                        menu = False
                        level = 0
                        pygame.display.update()
                        # pygame.mixer.music.unload()
                        main(medailon, obtiznost)

                X, Y = pygame.mouse.get_pos()
                kurzor = KURZOR.get_rect(center=(X, Y))
                WIN.blit(KURZOR, kurzor)
                pygame.display.update()

        if not NEPRATELE:
            level_pocty = LEVELY[level]
            basic = level_pocty[0]
            chytry = level_pocty[1]
            tlusty = level_pocty[2]
            casovac = pygame.time.get_ticks()
            pocet_enemaku = basic + chytry + tlusty

            for i in range(0, basic):
                levelocasovac = random.randint(
                    int(-100 * (10 * level ** ((level + 1) / level))), 500)

                cas = pygame.time.get_ticks() - levelocasovac
                souradnice = random.choice(([random.choice((-20, W + 20)),
                                             random.randint(-20, H + 20)],
                                            [random.randint(-20, W + 20),
                                             random.choice((-20, H + 20))]))
                n1 = souradnice[0]
                n2 = souradnice[1]
                NEPRATELE.append(["basic", n1, n2, 0, cas])

            for i in range(0, chytry):
                levelocasovac = random.randint(
                    int(-100 * (10 * level ** ((level + 1) / level))), 500)
                cas = pygame.time.get_ticks() - levelocasovac
                souradnice = random.choice(([random.choice((-20, W + 20)),
                                             random.randint(-20, H + 20)],
                                            [random.randint(-20, W + 20),
                                             random.choice((-20, H + 20))]))
                n1 = souradnice[0]
                n2 = souradnice[1]
                NEPRATELE.append(["chytry", n1, n2, 0, cas])
            for i in range(0, tlusty):
                levelocasovac = random.randint(
                    int(-100 * (10 * level ** ((level + 1) / level))), 500)
                cas = pygame.time.get_ticks() - levelocasovac
                souradnice = random.choice(([random.choice((-20, W + 20)),
                                             random.randint(-20, H + 20)],
                                            [random.randint(-20, W + 20),
                                             random.choice((-20, H + 20))]))
                n1 = souradnice[0]
                n2 = souradnice[1]
                NEPRATELE.append(["tlusty", n1, n2, 3, cas])
            level += 1
            max_pocty_naboju = [0, 5, 8, 10, 12, 15, 18, 20, 22, 25, 30]
            zasobnik_max = max_pocty_naboju[level - 1]
            random.shuffle(NEPRATELE)
            continue

        boost_tick = 0.3 * (1 + (level / level + 1))
        boost_cooldown = 1 / boost_tick * 1467
        raketka = draw_window(SSBILA, X, Y, stav_pohonu, rt, c1, c2)
        boost_timer(time_boost, BOOSTP)
        draw_text(zasobnik, zasobnik_max, vyhral, prohral, level - 1)
        pygame.display.update()

    #print(f"X,Y: {X, Y}")
    pygame.quit()


if __name__ == "__main__":
    main(medailon, obtiznost)
