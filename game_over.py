import pygame, linecache, time
import sys
from pygame.locals import*
#from Classemen import*

def game_over():

    fenetre = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('GameOver')
    GO1= pygame.image.load("GameOverI.jpg")
    GO2= pygame.image.load("GameOverII.jpg")
    GO3= pygame.image.load("GameOverIII.jpg")
    GO4= pygame.image.load("GameOverIV.jpg")
    GO=[GO1,GO2,GO3,GO4]
    font = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
    rep = 0
    for rep in range(0, 11):
        repII = 0
        for repII in range(0, 3):
            fenetre.blit(GO[repII], (0, 0))
            pygame.display.flip()
            time.sleep(0.05)
            fenetre.fill(0)
            repII += 1
        rep += 1




    for event in pygame.event.get():


        if event.type == QUIT:
            sys.exit()

    #Classemen()
    pygame.display.flip()






