import pygame
import os
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
magnet = pygame.image.load("NSMagnet.png")
def NSMagnet(x,y):
    gameDisplay.blit(magnet, (x,y))
x = 360
y = 400
while run:
    gameDisplay.fill(white)
    NSMagnet(x,y)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            x += x_change

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            ######################
        
pygame.quit()
quit()