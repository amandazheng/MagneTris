'''To Do Problems'''
# doesn't randomize position for magnets (done) // randomize magnet orientation
# fix endgame for when touches top of screen (done, but may want to include some sort of victory message)
# make it fall by certain amount of time (?)
#next magnet wont fall unless they connect (done)
#magnet reset_pos only works after miss


import pygame
import os
import random
import time

a_random = random.randint(10,750)
magnet_random = random.randint(1,2)
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,800))
screen_rect=gameDisplay.get_rect()
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
magnet = pygame.image.load("NSMagnet.png")
magnetNS = pygame.image.load("NSMagnet.png")
magnetSN = pygame.image.load("SNMagnet.png")
#magnet_current = 0
x = 360
y = 515
counter, text = 10, '100'.rjust(3) #change counter back to 50ish? when done
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Helvetica', 30)
stackheight = 1

def NSMagnet(x,y):
    gameDisplay.blit(magnetNS, (x,y))

if magnet_random == 0: 
    magnet_current = magnetNS
else: 
    magnet_current = magnetSN
    
class fallingMagnet:
    def __init__(self, a, b, orientation, fall):
        self.a = a
        self.b = b
        self.orientation = orientation
        self.fall = fall
        self.drawChar()
        self.fallConnect()

    def drawChar (self):
        gameDisplay.blit(magnet_current, (self.a,self.b))

    def reset_pos(self):
        self.b = 0
        self.a = random.randrange(0, 750)
        self.orientation = random.randrange(-1,2)
 
    def fallConnect (self):
        if self.fall == False: 
            self.a = x
            self.reset_pos
        else: 
            self.b += 1
            if self.b > 800:
                self.reset_pos()
            if self.b == (y-102*stackheight) and self.a >= (x-20) and self.a <= (x+20):
                self.a = x
                self.reset_pos
                self.fall = False

magnetList=[]
magnetList.append(fallingMagnet(a_random, 0, magnet_current, True))
magnetList[len(magnetList)-1].drawChar()

while run:
    gameDisplay.fill(white)
    NSMagnet(x,y)

    '''my attempt at falling by time''' 
    # if counter % 5.00 == 0.00:
    #     magnetList.append(fallingMagnet(a_random, 0, True))
    #     stackheight += 1

    for i in range(len(magnetList)):
        magnetList[i].drawChar()
        magnetList[i].fallConnect()

        if magnetList[i].fall == False and len(magnetList)-1 == i:
            magnetList.append(fallingMagnet(a_random, 0, magnet_current, True))
            stackheight += 1
        
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3)
            if counter < 0:
                "sorry, you lost"
            #if counter < -3:
                #run = False
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
    if stackheight == 5:
        run = False
            ################
        
pygame.quit()
exit()



