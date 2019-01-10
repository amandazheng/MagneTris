import pygame
import os
import random
a_random = random.randint(10,750)
_image_library = {}
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
screen_rect=gameDisplay.get_rect()
player=pygame.Rect(180, 180, 20, 20)
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
run = True
magnet = pygame.image.load("NSMagnet.png")

def NSMagnet(x,y):
    gameDisplay.blit(magnet, (x,y))
x = 360
y = 400
counter, text = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Helvetica', 30)

def fallingMagnet(a,b):
    gameDisplay.blit(magnet, (a,b))
a = a_random
b = 0

fall=True
while run:
    gameDisplay.fill(white)
    NSMagnet(x,y)
    fallingMagnet(a,b)
    pygame.display.update()
    clock.tick(60)

    if b >= x and a >= (x-30) and a <= (x+30):
        a = x
        fall = False
        # pygame.quit()
        # exit()

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            if fall == True: 
                b+=30
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else "sorry, you lost"
        if event.type == pygame.QUIT: break
        
    else:
        # gameDisplay.fill((255, 255, 255))
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