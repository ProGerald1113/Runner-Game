import pygame
from pygame.locals import *

pygame.init()

gravity = 4

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Runner Game')
player = pygame.Rect((450,250,50,50))
floor = pygame.Rect((-20,575,3200,150))

run = True 

while run:
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-3,0)
    elif key[pygame.K_d] == True:
        player.move_ip(3,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-3)
    elif key[pygame.K_s] == True:
        player.move_ip(0,3)
    
    player.top += gravity
    floor.bottom += -4
    
    if pygame.Rect.colliderect(player,floor):
        floor.bottom = player.top
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN , floor)
    pygame.draw.rect(screen, BLACK , player)  
    pygame.display.update()
    
pygame.quit()
    
    
