import pygame
import sys
import random
import math
import time
import linecache
from pygame.locals import *
from game_over import *
from Classemen import *
from classement_final import *

retour = False


def jeu_europe():
    fenetre = pygame.display.set_mode((969, 650))
    pygame.display.set_caption('Europe')

    # Initialisation des textures
    carteeurope = pygame.image.load("Europe.png")
    coeur = pygame.image.load("coeur.png")
    ico_bleu = pygame.image.load("iconebleu.png")
    ico_jaune = pygame.image.load("iconejaune.png")
    ico_vert = pygame.image.load("iconevert.png")
    ico_orange = pygame.image.load("iconeorange.png")
    ico_rouge = pygame.image.load("iconerouge.png")
    ico_noir = pygame.image.load("iconenoir.png")

    # Creation du GIF de victoire
    winI = pygame.image.load("winI.png")
    winII = pygame.image.load("winII.png")
    winIII = pygame.image.load("winIII.png")
    winIV = pygame.image.load("winIV.png")
    winV = pygame.image.load("winV.png")
    winVI = pygame.image.load("winVI.png")
    win = [winI, winII, winIII, winIV, winV, winVI]

    # Creation du GIF de défaite
    perduI = pygame.image.load("perduI.png")
    perduII = pygame.image.load("perduII.png")
    perduIII = pygame.image.load("perduIII.png")
    perduIV = pygame.image.load("perduIV.png")
    perdu = [perduI, perduII, perduIII, perduIV]

    # Positions des textes et images
    xcarte = 0
    ycarte = 50
    xecart = 858
    yecart = 0
    xdistance = 725
    ydistance = 24
    xville = 450
    yville = 14
    xscore = 830
    yscore = 6
    xpoints = 923
    ypoints = 0
    xcoeur4 = 175
    xcoeur3 = 135
    xcoeur2 = 95
    xcoeur1 = 55
    xcoeur0 = 15
    ycoeur = 10
    coeur_liste = [xcoeur0, xcoeur1, xcoeur2, xcoeur3, xcoeur4]

    # affichage des textures initiales
    chainescore = "Score:"
    font = pygame.font.SysFont("broadway", 24, bold=False, italic=False)
    textscore = font.render(chainescore, 1, (255, 255, 255))
    points = 0
    chainedistance = "Distance = ____ km"
    textdistance = font.render(chainedistance, 1, (255, 255, 255))

    pygame.display.flip()
    continuer = True
    while continuer == True:

        # Affichage des premieres structures
        fenetre.fill((51, 189, 223))
        fenetre.blit(carteeurope, (xcarte, ycarte))
        fenetre.blit(coeur, (xcoeur1, ycoeur))
        fenetre.blit(coeur, (xcoeur2, ycoeur))
        fenetre.blit(coeur, (xcoeur3, ycoeur))
        fenetre.blit(coeur, (xcoeur4, ycoeur))
        fenetre.blit(coeur, (xcoeur0, ycoeur))

        # Affichages des structures d'affichage du score et de la distance
        textpoints = font.render(str(points), 1, (255, 255, 255))
        fenetre.blit(textscore, (xscore, yscore))
        fenetre.blit(textpoints, (xpoints, yscore))
        fenetre.blit(textdistance, (xdistance, ydistance))

        # Prise d'une ville au hasard et initialisation des variables nécésaire au déroulement d'un tour
        fichier = open('villeseurope.txt', 'r')
        NumberOfLine = 0
        for line in fichier:
            NumberOfLine += 1
        a = random.randint(1, NumberOfLine)
        b = a
        while a == b:
            a = random.randint(1, NumberOfLine)
        v = linecache.getline('villeseurope.txt', a).strip()
        fichierII = open('cooreurope.txt', 'r')
        xy = linecache.getline('cooreurope.txt', a)
        font = pygame.font.SysFont("broadway", 31, bold=False, italic=True)
        textville = font.render(v, 1, (255, 255, 255))
        fenetre.blit(textville, (xville, yville))
        X = int(xy[0] + xy[1] + xy[2])
        Y = int(xy[4] + xy[5] + xy[6])
        ville = [X, Y]
        gagne = 0
        vie = 5
        pygame.display.flip()

        while gagne == 0 and vie != 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    position = event.pos
                    x = abs(ville[0] + xcarte - position[0])
                    y = abs(ville[1] - (position[1]))
                    distance = int(math.sqrt((x - xcarte) ** 2 + (y - ycarte) ** 2))

                    # Calcul et affichage de la distance
                    font = pygame.font.SysFont("broadway", 24, bold=False, italic=False)
                    textdistance = font.render(chainedistance, 1, (255, 255, 255))
                    fenetre.blit(textdistance, (xdistance, ydistance))
                    ecart = int(distance * 900 / 178)
                    textecart = font.render(str(ecart), 1, (255, 255, 255))

                    # Choix de l'icone en fonction de la distance
                    if distance >= 180:
                        ico = ico_bleu
                    elif distance < 180 and distance >= 92:
                        ico = ico_vert
                    elif distance < 92 and distance >= 51:
                        ico = ico_jaune
                    elif distance < 51 and distance >= 30:
                        ico = ico_orange
                    elif distance < 30:
                        ico = ico_rouge
                        gagne = 1
                        points = points + 1
                        fenetre.blit(carteeurope, (xcarte, ycarte))
                        fenetre.blit(ico, (position[0] - 20, position[1] - 40))

                    # Affichage des textures apres modifications
                    fenetre.fill((51, 189, 223))
                    fenetre.blit(textecart, (xecart, ydistance))
                    fenetre.blit(carteeurope, (xcarte, ycarte))
                    fenetre.blit(textscore, (xscore, yscore))
                    fenetre.blit(textville, (xville, yville))
                    fenetre.blit(textpoints, (xpoints, yscore))
                    fenetre.blit(textdistance, (xdistance, ydistance))
                    fenetre.blit(ico, (position[0] - 20, position[1] - 40))

                    vie = vie - 1

                    # Verification si succés
                    for c in range(0, vie):
                        fenetre.blit(coeur, (coeur_liste[c], ycoeur))
                    if vie == 0 and gagne != 1:
                        fenetre.blit(ico_noir, (ville[0] + xcarte - 20, ville[1] + ycarte - 40))
                        pygame.draw.circle(fenetre, (40, 40, 40), (ville[0] + xcarte, ville[1] + ycarte), distance, 2)
                        rep = 0
                        for i in range(0, 2):
                            repII = 0
                            for repII in range(0, 3):
                                fenetre.blit(perdu[repII], (100, 100))
                                pygame.display.flip()
                                time.sleep(0.3)
                                fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                                fenetre.blit(ico_noir, (ville[0] + xcarte - 20, ville[1] + ycarte - 40))
                                pygame.draw.circle(fenetre, (40, 40, 40), (ville[0] + xcarte, ville[1] + ycarte),
                                                   distance, 2)

                                for c in range(0, vie):
                                    fenetre.blit(coeur, (coeur_liste[c], 30))
                                repII += 1
                            rep += 1
                        pygame.display.flip()
                        continuer = False
                    if gagne == 1:
                        rep = 0
                        for rep in range(0, 4):
                            repII = 0
                            for repII in range(0, 5):
                                fenetre.blit(win[repII], (100, 100))
                                pygame.display.flip()
                                time.sleep(0.1)
                                fenetre.fill(0)
                                fenetre.fill((51, 189, 223))
                                fenetre.blit(textecart, (xecart, ydistance))
                                fenetre.blit(carteeurope, (xcarte, ycarte))
                                fenetre.blit(textscore, (xscore, yscore))
                                fenetre.blit(textville, (xville, yville))
                                fenetre.blit(textpoints, (xpoints, yscore))
                                fenetre.blit(textdistance, (xdistance, ydistance))
                                fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                                for c in range(0, vie):
                                    fenetre.blit(coeur, (coeur_liste[c], ycoeur))
                                repII += 1
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
