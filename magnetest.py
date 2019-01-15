'''To Do Problems'''
# doesn't randomize position for magnets // randomize magnet orientation
# fix endgame for when touches top of screen
# make it fall by certain amount of time

import pygame
import os
import random
import time

a_random = random.randint(10,750)
magnet_random = random.randint(1,2)
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
screen_rect=gameDisplay.get_rect()
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
magnet = pygame.image.load("NSMagnet.png")
magnetNS = pygame.image.load("NSMagnet.png")
magnetSN = pygame.image.load("SNMagnet.png")
magnet_current = 0
x = 360
y = 400
counter, text = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 100)
font = pygame.font.SysFont('Helvetica', 30)
stackheight = 1

def NSMagnet(x,y):
    gameDisplay.blit(magnetNS, (x,y))

if magnet_random == 1: 
    magnet_current = magnetNS
else: 
    magnet_current = magnetSN
    
class fallingMagnet:
    def __init__(self, a, b, orientation, fall):
        self.a = a
        self.b = b
        self.orientation = magnet_random
        self.fall = fall
        self.drawChar()
        self.fallConnect()

    def drawChar (self):
        gameDisplay.blit(magnet_current, (self.a,self.b))
    
    def fallConnect (self):
        if self.fall == False: 
            self.a = x
        else: 
            self.b += 1
            if self.b == (y-102*stackheight) and self.a >= (x-20) and self.a <= (x+20):
                self.a = x
                self.fall = False

magnetList=[]
magnetList.append(fallingMagnet(a_random, 0, magnet_random, True))
magnetList[len(magnetList)-1].drawChar()

def fallingMagnetSouth(a,b):
    gameDisplay.blit(magnetSN, (a,b))
a = 50
b = 0

fall=True

while run:
    pygame.time.delay(10)
    gameDisplay.fill(white)
    NSMagnet(x,y) 
    magnet1 = fallingMagnet(0,0,magnet_current,True)
    b = magnet1.b
    a = magnet1.a
    if b == (y-stackheight) and a >= (x-20) and a <= (x+20):
        a = x 
        magnetStackHeight = magnetStackHeight + 102
        fall = False

    if fall == True: 
        b += .5
    

    # this part was my attempt for multiple falling magnets, it didnt work 
    #if counter % 10 == 0:
    #    fallingMagnet(a,b)

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
    pygame.display.update()
#while run:
#    gameDisplay.fill(white)
#    NSMagnet(x,y)

    '''my attempt at falling by time''' 
    # if counter % 5.00 == 0.00:
    #     magnetList.append(fallingMagnet(a_random, 0, True))
    #     stackheight += 1

    for i in range(len(magnetList)):
        magnetList[i].drawChar()
        magnetList[i].fallConnect()
        if magnetList[i].fall == False and len(magnetList)-1 == i:
            magnetList.append(fallingMagnet(a_random, 0, magnet_random, True))
            stackheight += 1
    
#    for event in pygame.event.get():
#        if event.type == pygame.USEREVENT: 
#            counter -= 1
#            text = str(counter).rjust(3)
#            if counter < 0:
##                "sorry, you lost"
        if event.type == pygame.QUIT: break
        
#    else:
#        gameDisplay.blit(font.render(text, True, (0, 0, 0)), (32, 48))
#        pygame.display.flip()
#        clock.tick(60)

#    if event.type == pygame.QUIT:
#        run = False
#    if event.type == pygame.KEYDOWN:
#        if event.key == pygame.K_LEFT:
#            x_change = -5
 #           if x < 10:
  #              x = 10
   #     elif event.key == pygame.K_RIGHT:
    #        x_change = 5
     #       if x > 750:
      #          x = 750
       # x += x_change

#    if event.type == pygame.KEYUP:
#        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#            x_change = 0
            ################
        
pygame.quit()
exit()