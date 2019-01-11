import pygame
import os
import random
a_random = random.randint(10,750)
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
screen_rect=gameDisplay.get_rect()
# player=pygame.Rect(180, 180, 20, 20)
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
magnet = pygame.image.load("NSMagnet.png")
magnetSouth = pygame.image.load("SNMagnet.png")
magnetStackHeight = 102

def NSMagnet(x,y):
    gameDisplay.blit(magnet, (x,y))
x = 360
y = 400
counter, text = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 90)
font = pygame.font.SysFont('Helvetica', 30)

def fallingMagnet(a,b):
    gameDisplay.blit(magnet, (a,b))
a = a_random
b = 0

def fallingMagnetSouth(a,b):
    gameDisplay.blit(magnetSouth, (c,d))
c = 50
d = 0

fall=True

while run:
    pygame.time.delay(10)

    if b == (y-magnetStackHeight) and a >= (x-20) and a <= (x+20):
        a = x 
        magnetStackHeight = magnetStackHeight + 102
        fall = False

    if fall == True: 
        b += .5
    

    # this part was my attempt for multiple falling magnets, it didnt work 
    if counter % 10 == 0:
        fallingMagnet(a,b)

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= .1
            text = str(counter).rjust(3) if counter > 0 else "sorry, you lost"
        gameDisplay.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        x_change = 0
        if keys[pygame.K_LEFT]:
            x_change = -5
            if x < 10:
                x = 10
        elif keys[pygame.K_RIGHT]:
            x_change = 5
            if x > 750:
                x = 750

        if fall == False:
                a = x

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0 
        x+= x_change
                ################
    gameDisplay.fill(white)
    NSMagnet(x,y)
    fallingMagnet(a,b)
    fallingMagnetSouth(c,d)
    pygame.display.update()
pygame.quit()
exit()