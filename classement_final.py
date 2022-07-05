import pygame
import time
import linecache
from pygame.locals import *
import sys

pygame.font.init()

retour = False


def finalclassement():
    pygame.init()
    fenetre = pygame.display.set_mode((650, 500))
    pygame.display.set_caption('Classement des joueurs')
    fenetre.fill((42, 89, 176))
    boucle4 = True

    fichier = open('top10.txt', 'r')

    xfirst = 5
    yfirst = 160
    xsecond = 5
    ysecond = 230
    xthird = 5
    ythird = 300
    xfourth = 5
    yfourth = 380
    xfifth = 5
    yfifth = 440

    intro = True
    for i in range(1, 255, 3):
        podium = pygame.image.load("podium.png")
        fenetre.fill((0, 0, 0))
        podium.fill((i, i, i, i), special_flags=BLEND_RGBA_MULT)
        fenetre.blit(podium, (0, 0))
        pygame.display.flip()
        time.sleep(0.000000001)
    intro = False

    NumberOfLine = 0
    for ligne in fichier:
        NumberOfLine += 1
        first = linecache.getline('top10.txt', 1).strip()
        second = linecache.getline('top10.txt', 2).strip()
        third = linecache.getline('top10.txt', 3).strip()
        fourth = linecache.getline('top10.txt', 4).strip()
        fifth = linecache.getline('top10.txt', 5).strip()
        font = pygame.font.SysFont("broadway", 40, bold=False, italic=False)
        textfirst = font.render(str(first), 1, (255, 255, 255))
        textsecond = font.render(str(second), 1, (255, 255, 255))
        textthird = font.render(str(third), 1, (255, 255, 255))
        textfourth = font.render(str(fourth), 1, (255, 255, 255))
        textfifth = font.render(str(fifth), 1, (255, 255, 255))
        pygame.display.flip()

    fenetre.blit(textfirst, (xfirst, yfirst))
    fenetre.blit(textsecond, (xsecond, ysecond))
    fenetre.blit(textthird, (xthird, ythird))
    fenetre.blit(textfourth, (xfourth, yfourth))
    fenetre.blit(textfifth, (xfifth, yfifth))
    pygame.display.flip()
    time.sleep(5)
    fenetre = pygame.display.set_mode((1000, 600))
    fenetre.fill((42, 89, 176))
