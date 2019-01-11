import pygame
import os
import random
a_random = random.randint(10,750)
<<<<<<< HEAD
magnet_random = random.randint(1,2)
=======
c_random = random.randint(10,750)
>>>>>>> 4224090b84be37ec24e3f0a1b0a0d5d89ae0071c
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
screen_rect=gameDisplay.get_rect()
# player=pygame.Rect(180, 180, 20, 20)
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
<<<<<<< HEAD
magnetNS = pygame.image.load("NSMagnet.png")
=======
magnet = pygame.image.load("NSMagnet.png")
magnetSouth = pygame.image.load("SNMagnet.png")
>>>>>>> 4224090b84be37ec24e3f0a1b0a0d5d89ae0071c

def NSMagnet(x,y):
    gameDisplay.blit(magnetNS, (x,y))
x = 360
y = 400
counter, text = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Helvetica', 30)

# if magnet_random == 1: 
#     magnet_current == magnetNS
# else: 
#      magnet_current == mangetSN
    
magnet_current = magnetNS

def fallingMagnet(a,b):
    gameDisplay.blit(magnet_current, (a,b))
a = a_random
b = 0

def fallingMagnetSouth(a,b):
    gameDisplay.blit(magnetSouth, (c,d))
c = 50
d = 0
fall=True
while run:
    gameDisplay.fill(white)
    NSMagnet(x,y)
    fallingMagnet(a,b)
    fallingMagnetSouth(c,d)
    pygame.display.update()
    clock.tick(60)

    if b == (y-102) and a >= (x-20) and a <= (x+20):
        a = x
        fall = False

    if fall == True: 
        b += 1
    

    # this part was my attempt for multiple falling magnets, it didnt work 
    # if counter % 10 == 0:
    #      fallingMagnet(a,b)

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else "sorry, you lost"
        if event.type == pygame.QUIT: break
        
    else:
        gameDisplay.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                if x < 10:
                    x = 10
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                if x > 750:
                    x = 750
            x += x_change

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            ################
        
pygame.quit()
exit()