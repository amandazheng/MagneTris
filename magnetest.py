import pygame
import os
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



while run:
    gameDisplay.fill(white)
    NSMagnet(x,y)
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
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

        #player.clamp_ip(screen_rect)
        #if NSMagnet.screen_rect.right > 800:
         #   NSMagnet.screen_rect.right = 800
        #if NSMagnet.screen_rect.left < 0:
         #   NSMagnet.screen_rect.left = 0
        #if NSMagnet.screen_rect.bottom > 600:
        #    NSMagnet.screen_rect.bottom = 600
        #if NSMagnet.screen_rect.top < 0:
         #   NSMagnet.screen_rect.top = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            ################
        
pygame.quit()
exit()


