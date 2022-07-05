import pygame
from pygame.locals import *
from jeu_france import *
from jeu_europe import *
from regle_city import *
from jeu_monde import *

pygame.font.init()

retour = False


def bouclecity():
    xfrance = 350

    yfrance = 30

    xeurope = 350

    yeurope = 180

    xmonde = 350

    ymonde = 330

    xregle = 320

    yregle = 480

    fenetre = pygame.display.set_mode((1000, 600))

    pygame.display.set_caption('Entrainez-vous')

    fenetre.fill((42, 89, 176))

    pygame.display.flip()
    boucle2 = True
    while boucle2 == True:
        chainefrance = "Jeu France"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        textfrance = font.render(chainefrance, 1, (255, 255, 255))
        fenetre.blit(textfrance, (xfrance, yfrance))

        chaineeurope = "Jeu Europe"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        texteurope = font.render(chaineeurope, 1, (255, 255, 255))
        fenetre.blit(texteurope, (xeurope, yeurope))

        chainemonde = "Jeu Monde"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        textmonde = font.render(chainemonde, 1, (255, 255, 255))
        fenetre.blit(textmonde, (xmonde, ymonde))

        retour = pygame.image.load("retour.png")
        fenetre.blit(retour, (0, 0))

        chaineregle = "Voir les règles"
        font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
        textregle = font.render(chaineregle, 1, (255, 255, 255))
        fenetre.blit(textregle, (xregle, yregle))

        for event in pygame.event.get():

            if event.type == MOUSEMOTION and event.pos[0] < xfrance + 600 and event.pos[0] > xfrance and event.pos[1] > yfrance and event.pos[1] < yfrance + 50:
                textfrance = font.render(chainefrance, 1, (0, 0, 0))
                fenetre.blit(textfrance, (xfrance, yfrance))

            elif event.type == MOUSEMOTION and event.pos[0] < xeurope + 600 and event.pos[0] > xeurope and event.pos[1] > yeurope and event.pos[1] < yeurope + 50:
                texteurope = font.render(chaineeurope, 1, (0, 0, 0))
                fenetre.blit(texteurope, (xeurope, yeurope))

            elif event.type == MOUSEMOTION and event.pos[0] < xmonde + 600 and event.pos[0] > xmonde and event.pos[1] > ymonde and event.pos[1] < ymonde + 50:
                textmonde = font.render(chainemonde, 1, (0, 0, 0))
                fenetre.blit(textmonde, (xmonde, ymonde))

            elif event.type == MOUSEMOTION and event.pos[0] < xregle + 600 and event.pos[0] > xregle and event.pos[1] > yregle and event.pos[1] < yregle + 50:
                textregle = font.render(chaineregle, 1, (0, 0, 0))
                fenetre.blit(textregle, (xregle, yregle))

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xfrance + 600 and event.pos[0] > xfrance and event.pos[1] > yfrance and event.pos[1] < yfrance + 50:
                jeu_france()
                fenetre = pygame.display.set_mode((1000, 600))
                fenetre.fill((69, 93, 215))
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xeurope + 600 and event.pos[0] > xeurope and event.pos[1] > yeurope and event.pos[1] < yeurope + 50:
                jeu_europe()
                fenetre = pygame.display.set_mode((1000, 600))
                fenetre.fill((69, 93, 215))
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xmonde + 600 and event.pos[0] > xmonde and event.pos[1] > ymonde and event.pos[1] < ymonde + 50:
                jeu_monde()
                fenetre = pygame.display.set_mode((1000, 600))
                fenetre.fill((69, 93, 215))
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < xregle + 600 and event.pos[0] > xregle and event.pos[1] > yregle and event.pos[1] < yregle + 50:
                regle_city()
                retour = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 100 and event.pos[1] < 100:
                boucle2 = False
                fenetre.fill((69, 93, 215))
                break

            if boucle2 == True:
                pygame.display.flip()
            if event.type == QUIT:
                boucle2 = False
                retour = False
                fenetre.fill((69, 93, 215))
                break

    while retour == True:
        pygame.init()
