import pygame
import sys
import random
import math
import time
import linecache
from Classemen import *
from classement_final import *
from game_over import *
from pygame.locals import *

retour = False


def jeu_pays_monde():
    fenetre = pygame.display.set_mode((1135, 695))
    pygame.display.set_caption('Monde')
    pygame.font.init()

    # Initialisation des textures
    cartemonde = pygame.image.load("PCarteMonde.png")
    coeur = pygame.image.load("coeur.png")
    ico_rouge = pygame.image.load("iconerouge.png")
    ico_noir = pygame.image.load("iconenoir.png")
    perdu = pygame.image.load("perduI.png")

    # Creation du GIF de victoire
    winI = pygame.image.load("winI.png")
    winII = pygame.image.load("winII.png")
    winIII = pygame.image.load("winIII.png")
    winIV = pygame.image.load("winIV.png")
    winV = pygame.image.load("winV.png")
    winVI = pygame.image.load("winVI.png")
    win = [winI, winII, winIII, winIV, winV, winVI]

    # Positions des textes et images
    xcarte = 15
    ycarte = 80
    xpays = 390
    ypays = 14
    xscore = 995
    yscore = 37
    xpoints = 1090
    ypoints = 38
    xcoeur4 = 185
    xcoeur3 = 145
    xcoeur2 = 105
    xcoeur1 = 65
    xcoeur0 = 25
    ycoeur = 10
    coeur_liste = [xcoeur0, xcoeur1, xcoeur2, xcoeur3, xcoeur4]

    # affichage des textures initiales
    chainescore = "Score:"
    font = pygame.font.SysFont("broadway", 24, bold=False, italic=False)
    textscore = font.render(chainescore, 1, (255, 255, 255))
    points = 0
    pygame.display.flip()
    continuer = True

    while continuer == True:
        # Affichage des premieres structures
        fenetre.fill((40, 133, 255))
        fenetre.blit(cartemonde, (xcarte, ycarte))
        fenetre.blit(coeur, (xcoeur1, ycoeur))
        fenetre.blit(coeur, (xcoeur2, ycoeur))
        fenetre.blit(coeur, (xcoeur3, ycoeur))
        fenetre.blit(coeur, (xcoeur4, ycoeur))
        fenetre.blit(coeur, (xcoeur0, ycoeur))

        # Affichages des structures d'affichage du score et de la distance
        textpoints = font.render(str(points), 1, (255, 255, 255))
        fenetre.blit(textscore, (xscore, yscore))
        fenetre.blit(textpoints, (xpoints, yscore))

        # Prise d'une ville au hasard et initialisation des variables nécésaire au déroulement d'un tour
        fichier = open('PaysMonde.txt', 'r')
        NumberOfLine = 0
        for line in fichier:
            NumberOfLine += 1
        a = random.randint(1, NumberOfLine)
        b = a
        while a == b:
            a = random.randint(1, NumberOfLine)
        p = linecache.getline('PaysMonde.txt', a).strip()
        fichierII = open('ColPaysMonde.txt', 'r')
        colors = linecache.getline('ColPaysMonde.txt', a)
        font = pygame.font.SysFont("broadway", 35, bold=False, italic=True)
        textpays = font.render(p, 1, (255, 255, 255))
        fenetre.blit(textpays, (xpays, ypays))
        red = int(colors[0] + colors[1] + colors[2])
        green = int(colors[4] + colors[5] + colors[6])
        blue = int(colors[8] + colors[9] + colors[10])
        couleurs = [red, green, blue]
        gagne = 0
        vie = 5
        pygame.display.flip()
        while gagne == 0 and vie != 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    position = event.pos
                    x = position[0] - xcarte  # ajout du decalage de la carte
                    y = position[1] - ycarte  # ajout du decalage de la carte
                    colors = pygame.Surface.get_at(cartemonde, (x, y))
                    couleurposition = [colors[0], colors[1], colors[2]]

                    # Choix de l'icone en fonction de la distance
                    if couleurs == couleurposition:
                        ico = ico_rouge
                        gagne = 1
                        points = points + 1
                        fenetre.blit(cartemonde, (xcarte, ycarte))
                        fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                    else:
                        ico = ico_noir

                    # Affichage des textures apres modifications
                    fenetre.fill((40, 133, 255))
                    fenetre.blit(cartemonde, (xcarte, ycarte))
                    fenetre.blit(textscore, (xscore, yscore))
                    fenetre.blit(textpays, (xpays, ypays))
                    fenetre.blit(textpoints, (xpoints, yscore))
                    fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                    vie = vie - 1

                    # Verification si succés
                    for c in range(0, vie):
                        fenetre.blit(coeur, (coeur_liste[c], ycoeur))
                    if vie == 0 and gagne != 1:
                        taille = 979
                        if a == 8:
                            taille = 300  # Cas pour les Etats-Unis car pb de qualité d'image
                        k = i = j = 0
                        for k in range(0, 4):
                            for i in range(0, taille):
                                for j in range(0, 600):
                                    colorpixel = pygame.Surface.get_at(cartemonde, (i, j))
                                    cpixel = [colorpixel[0], colorpixel[1], colorpixel[2]]
                                    if couleurs == cpixel:
                                        pygame.Surface.set_at(cartemonde, (i, j), (0, 255, 0))
                                    j += 1
                                i += 1
                            time.sleep(0.01)
                            fenetre.blit(perdu, (100, 100))
                            pygame.display.flip()
                            fenetre.blit(cartemonde, (xcarte, ycarte))
                            i = j = 0
                            for i in range(0, taille):
                                for j in range(0, 600):
                                    colorpixel = pygame.Surface.get_at(cartemonde, (i, j))
                                    cpixel = [colorpixel[0], colorpixel[1], colorpixel[2]]
                                    if cpixel == [0, 255, 0]:
                                        pygame.Surface.set_at(cartemonde, (i, j), couleurs)
                                    j += 1
                                i += 1
                            time.sleep(0.1)
                            fenetre.blit(perdu, (100, 100))
                            pygame.display.flip()
                            fenetre.blit(cartemonde, (xcarte, ycarte))
                            k += 1
                        pygame.display.flip()
                        continuer = False
                    if gagne == 1:
                        rep = 0
                        for rep in range(0, 4):
                            a = 0
                            for a in range(0, 5):
                                fenetre.blit(win[a], (100, 100))
                                pygame.display.flip()
                                time.sleep(0.1)
                                fenetre.fill(0)
                                fenetre.fill((40, 133, 255))
                                fenetre.blit(textscore, (xscore, yscore))
                                fenetre.blit(textpays, (xpays, ypays))
                                fenetre.blit(textpoints, (xpoints, ypoints))
                                fenetre.blit(cartemonde, (xcarte, ycarte))
                                fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                                for c in range(0, vie):
                                    fenetre.blit(coeur, (coeur_liste[c], ycoeur))
                                a += 1
                            rep += 1
                    pygame.display.flip()
                if event.type == QUIT:
                    sys.exit()

    pygame.display.flip()
    game_over()
    Classement()
    finalclassement()

    retour = False

    while retour == True:
        pygame.init()
