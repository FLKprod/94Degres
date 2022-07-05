import pygame
from pygame.locals import *
from regle_pays import *
from jeu_pays_europe import *
from jeu_pays_monde import *

pygame.font.init()

retour = False


def bouclepays():
    xeurope = 330

    yeurope = 100

    xmonde = 330

    ymonde = 275

    xregle = 320

    yregle = 450

    fenetre = pygame.display.set_mode((1000, 600))

    pygame.display.set_caption('Entrainez-vous')

    fenetre.fill((42, 89, 176))

    pygame.display.flip()
    boucle3 = True
    while boucle3 == True:
        chainepayseurope = "Pays Europe"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        texteurope = font.render(chainepayseurope, 1, (255, 255, 255))
        fenetre.blit(texteurope, (xeurope, yeurope))

        chainepaysmonde = "Pays Monde"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        textmonde = font.render(chainepaysmonde, 1, (255, 255, 255))
        fenetre.blit(textmonde, (xmonde, ymonde))

        retour = pygame.image.load("retour.png")
        fenetre.blit(retour, (0, 0))

        chaineregle = "Voir les règles"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        textregle = font.render(chaineregle, 1, (255, 255, 255))
        fenetre.blit(textregle, (xregle, yregle))

        for event in pygame.event.get():

            if event.type == MOUSEMOTION and event.pos[0] < xeurope + 600 and event.pos[0] > xeurope and event.pos[
                1] > yeurope and event.pos[1] < yeurope + 50:
                # select2="Jeu Europe"
                # font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
                textpayseurope = font.render(chainepayseurope, 1, (0, 0, 0))
                fenetre.blit(textpayseurope, (xeurope, yeurope))

            elif event.type == MOUSEMOTION and event.pos[0] < xmonde + 600 and event.pos[0] > xmonde and event.pos[
                1] > ymonde and event.pos[1] < ymonde + 50:
                # select3="Jeu Monde"
                # font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
                textpaysmonde = font.render(chainepaysmonde, 1, (0, 0, 0))
                fenetre.blit(textpaysmonde, (xmonde, ymonde))

            elif event.type == MOUSEMOTION and event.pos[0] < xregle + 600 and event.pos[0] > xregle and event.pos[
                1] > yregle and event.pos[1] < yregle + 50:
                # select4 = "Voir les règles"
                # font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
                textregle = font.render(chaineregle, 1, (0, 0, 0))
                fenetre.blit(textregle, (xregle, yregle))

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xeurope + 600 and event.pos[
                0] > xeurope and event.pos[1] > yeurope and event.pos[1] < yeurope + 50:
                # regles()
                jeu_pays_europe()
                fenetre = pygame.display.set_mode((1000, 600))
                fenetre.fill((69, 93, 215))
                retour = True
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xmonde + 600 and event.pos[
                0] > xmonde and event.pos[1] > ymonde and event.pos[1] < ymonde + 50:
                jeu_pays_monde()
                fenetre = pygame.display.set_mode((1000, 600))
                fenetre.fill((69, 93, 215))
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xregle + 600 and event.pos[
                0] > xregle and event.pos[1] > yregle and event.pos[1] < yregle + 50:
                regle_pays()
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 100 and event.pos[1] < 100:
                boucle3 = False
                retour = False
                fenetre.fill((69, 93, 215))
                break

            if boucle3 == True:
                pygame.display.flip()
            if event.type == QUIT:
                boucle3 = False
                retour = False
                fenetre.fill((69, 93, 215))
                break

    while retour == True:
        pygame.init()
