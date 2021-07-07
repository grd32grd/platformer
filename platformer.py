import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()
SCREENWIDTH = 1000
SCREENHEIGHT = 1000

#Colors
WHITE = (255,255,255)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Platformer")

pygame.draw.rect(screen, WHITE , (400, 400, 20, 20),0)
screen.fill(WHITE)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()