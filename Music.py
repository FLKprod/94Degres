import pygame
from pygame.locals import*
def Music():
    # Initialisation des variables
    xsound1 = 50
    xsound2 = 200
    xsound3=350
    xsound4 = 500
    xsound5 = 650
    xsoundstop = 850
    ysound1 = 440
    ysound2 = 490
    ysound3 = 440
    ysound4 = 490
    ysound5 = 440
    ysoundstop = 465
    xplus = 500
    yplus = 5
    xmoins = 677
    ymoins = 5
    pygame.mixer.init()
    valeurson = pygame.mixer.music.get_volume()

    fenetre = pygame.display.set_mode((1000, 600))
    fenetre.fill((253, 17, 251))
    Principal = pygame.image.load("Musique.jpg")
    PrincipalII = pygame.image.load("son.png")
    fenetre.blit(Principal, (0, 0))
    fenetre.blit(PrincipalII, (xsound1, ysound1))
    fenetre.blit(PrincipalII, (xsound2, ysound2))
    fenetre.blit(PrincipalII, (xsound3, ysound3))
    fenetre.blit(PrincipalII, (xsound4, ysound4))
    fenetre.blit(PrincipalII, (xsound5, ysound5))
    plus = pygame.image.load("Plus.png")
    moins = pygame.image.load("moins.png")
    retourmusic = pygame.image.load("retour.png")
    soncoupe = pygame.image.load("soncoupe.png")
    fenetre.blit(plus, (xplus, yplus))
    fenetre.blit(moins, (xmoins, ymoins))
    fenetre.blit(moins, (xmoins, ymoins))
    fenetre.blit(retourmusic, (0, 0))
    pygame.display.flip()
    music=True
    while music==True:
        boucle3 = True
        pygame.display.set_caption('Interface Musical')
        while boucle3 == True:

            fenetre.blit(PrincipalII, (xsound1, ysound1))
            fenetre.blit(PrincipalII, (xsound2, ysound2))
            fenetre.blit(PrincipalII, (xsound3, ysound3))
            fenetre.blit(PrincipalII, (xsound4, ysound4))
            fenetre.blit(PrincipalII, (xsound5, ysound5))
            fenetre.blit(soncoupe, (xsoundstop, ysoundstop))
            fenetre.blit(plus, (xplus, yplus))
            fenetre.blit(moins, (xmoins, ymoins))
            fenetre.blit(moins, (xmoins, ymoins))
            fenetre.blit(retourmusic, (0,0))
            for event in pygame.event.get():
                if event.type == MOUSEMOTION and event.pos[0] < xsound1 + 100 and event.pos[0] > xsound1 and event.pos[1] > ysound1 and event.pos[1] < ysound1 + 100:
                    sonselect = pygame.image.load("sonselect.png")
                    fenetre.blit(sonselect, (xsound1, ysound1))
                elif event.type == MOUSEMOTION and event.pos[0] < xsound2 + 100 and event.pos[0] > xsound2 and event.pos[1] > ysound2 and event.pos[1] < ysound2 + 100:
                    sonselect = pygame.image.load("sonselect.png")
                    fenetre.blit(sonselect, (xsound2, ysound2))
                elif event.type == MOUSEMOTION and event.pos[0] < xsound3 + 100 and event.pos[0] > xsound3 and event.pos[1] > ysound3 and event.pos[1] < ysound3 + 100:
                    sonselect = pygame.image.load("sonselect.png")
                    fenetre.blit(sonselect, (xsound3, ysound3))
                elif event.type == MOUSEMOTION and event.pos[0] < xplus + 100 and event.pos[0] > xplus and event.pos[1] > yplus and event.pos[1] < yplus + 100:
                    plusselect = pygame.image.load("Plusselect.png")
                    fenetre.blit(plusselect, (xplus, yplus))
                elif event.type == MOUSEMOTION and event.pos[0] < xmoins + 100 and event.pos[0] > xmoins and event.pos[1] > ymoins and event.pos[1] < ymoins + 100:
                    moinsselect = pygame.image.load("moinsselect.png")
                    fenetre.blit(moinsselect, (xmoins, ymoins))
                elif event.type == MOUSEMOTION and event.pos[0] < 100 and event.pos[0] > 0 and event.pos[1] > 0 and event.pos[1] < 100:
                    retourmusicselect = pygame.image.load("retourselect.png")
                    fenetre.blit(retourmusicselect, (0, 0))
                if event.type == MOUSEMOTION and event.pos[0] < xsound4 + 100 and event.pos[0] > xsound4 and event.pos[1] > ysound4 and event.pos[1] < ysound4 + 100:
                    sonselect = pygame.image.load("sonselect.png")
                    fenetre.blit(sonselect, (xsound4, ysound4))
                if event.type == MOUSEMOTION and event.pos[0] < xsound5 + 100 and event.pos[0] > xsound5 and event.pos[1] > ysound5 and event.pos[1] < ysound5 + 100:
                    sonselect = pygame.image.load("sonselect.png")
                    fenetre.blit(sonselect, (xsound5, ysound5))
                if event.type == MOUSEMOTION and event.pos[0] < xsoundstop + 100 and event.pos[0] > xsoundstop and event.pos[1] > ysoundstop and event.pos[1] < ysoundstop + 100:
                    sonselect = pygame.image.load("sonselectcoupe.png")
                    fenetre.blit(sonselect, (xsoundstop, ysoundstop))
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xsound1 + 100 and event.pos[0] > xsound1 and event.pos[1] > ysound1 and event.pos[1] < ysound1 + 100:
                    son = pygame.mixer.music.load("Music.WAV")
                    pygame.mixer.music.play(1, 0.0)
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xsound2 + 100 and event.pos[0] > xsound2 and event.pos[1] > ysound2 and event.pos[1] < ysound2 + 100:
                    son = pygame.mixer.music.load("MusicII.WAV")
                    pygame.mixer.music.play(1, 0.0)
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xsound3 + 100 and event.pos[0] > xsound3 and event.pos[1] > ysound3 and event.pos[1] < ysound3 + 100:
                    son = pygame.mixer.music.load("MusicIII.WAV")
                    pygame.mixer.music.play(1, 0.0)
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xsound4 + 100 and event.pos[0] > xsound4 and event.pos[1] > ysound4 and event.pos[1] < ysound4 + 100:
                    son = pygame.mixer.music.load("MusicIV.WAV")
                    pygame.mixer.music.play(1, 0.0)
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xsound5 + 100 and event.pos[0] > xsound5 and event.pos[1] > ysound5 and event.pos[1] < ysound5 + 100:
                    son = pygame.mixer.music.load("MusicV.WAV")
                    pygame.mixer.music.play(1, 0.0)
                if event.type == MOUSEBUTTONDOWN and event.pos[0] < xsoundstop + 100 and event.pos[0] > xsoundstop and event.pos[1] > ysoundstop and event.pos[1] < ysoundstop + 100:
                    pygame.mixer.music.pause()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xplus + 100 and event.pos[0] > xplus and event.pos[1] > yplus and event.pos[1] < yplus + 100:
                    if valeurson != 1.0:
                        valeurson += 0.2
                    pygame.mixer.music.set_volume(valeurson)
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xmoins + 100 and event.pos[0] > xmoins and event.pos[1] > ymoins and event.pos[1] < ymoins + 100:
                    if valeurson != 0.0:
                        valeurson -= 0.2
                    pygame.mixer.music.set_volume(valeurson)
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 100 and event.pos[0] > 0 and event.pos[1] > 0 and event.pos[1] < 100:
                    boucle3 = False
                    music = False
                if boucle3 == True:
                    pygame.display.flip()
                if event.type == QUIT:
                    boucle3 = False
                    music = False
                elif event.type == KEYUP and event.key == K_ESCAPE:
                    boucle3 = False
                    music = False
    pygame.display.flip()
    return music