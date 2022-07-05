import collections
import pygame
from pygame.locals import *
import sys

pygame.font.init()


def Classement():
    fenetre = pygame.display.set_mode((650, 500))
    pygame.display.set_caption('Classement')
    pygame.display.flip()

    import collections
    Player = collections.namedtuple('Player', 'score name')
    score = input("score:")
    nom = input("Quel est le nom :")
    fichiertemp = open("ScoreTemp.txt", "w")

    fichiertemp.write(nom)
    fichiertemp.write(" ")
    fichiertemp.write(score)

    fichiertemp.close()

    fichierfinal = open("Classement.txt", "a")
    fichier = open("ScoreTemp.txt", "r")

    for s in fichier:
        ajouter = s

    fichierfinal.write(ajouter)
    fichierfinal.write("\n")

    fichier.close()
    fichierfinal.close()

    fichierclassement = open("Classement.txt", "r")
    lignes = fichierclassement.readlines()

    d = {}
    listjoueur = []
    listscore = []
    for ligne in lignes:
        nom = ligne.split(" ")[0]
        score = ligne.split(" ")[1].split("\n")[0]
        listjoueur.append(nom)
        listscore.append(score)
    n = len(listjoueur)
    for i in range(n):
        if listjoueur[i] in listjoueur:

            value = listscore[i]
            name = listjoueur[i]
            d[name] = int(value)
        else:
            value = listscore[i]
            name = listjoueur[i]
            print(type(value))
            d[name] = int(value)
    # print(d)
    # print(max(d, key=d.get))
    fichierclassement.close()

    worst = sorted(Player(v, k) for (k, v) in d.items())
    # print(worst)
    print("\n")
    best = sorted([(v, k) for (k, v) in d.items()], reverse=True)

    # print(best)

    fichiertop = open("top10.txt", 'w')
    for i in range(10):
        print(best[i])
        text = str(best[i])
        fichiertop.write(text)
        fichiertop.write("\n")

    fichiertop.close()

    pygame.display.flip()
