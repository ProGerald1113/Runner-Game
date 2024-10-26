import pygame
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Runner Game')
player = pygame.Rect((4,18,50,50))

run = True 

while run:
    
    pygame.draw.rect(screen, BLACK , player)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
    screen.fill(BLUE)
    pygame.display.update()
    
pygame.quit()
    
    
