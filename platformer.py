import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import *
import pygame.image

pygame.init()
SCREENWIDTH = 1000
SCREENHEIGHT = 1000

#Colors
WHITE = (255,255,255)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Platformer")

#Background
bg1 = pygame.image.load("bg1.png").convert()
pygame.draw.rect(screen, WHITE , (400, 400, 20, 20),0)
screen.fill(WHITE)

pygame.display.update()

running = True
while running:

    screen.blit(bg1,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()