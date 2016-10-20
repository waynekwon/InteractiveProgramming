import pygame, sys
from pygame.locals import *
pygame.init()
display_width = 1600
display_height = 900
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Penalty Shootout!')


#set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 250,   0)
BLUE  = (  0,   0, 255)

#loading images

soccerball = pygame.image.load('soccerball.png')
soccerball = pygame.transform.scale(soccerball, (50, 50))
messi = pygame.image.load('messi.png')
messi = pygame.transform.scale(messi, (100, 100))
soccernet = pygame.image.load('goalnets.png')
soccernet = pygame.transform.scale(soccernet, (600, 250))
ballrect = soccerball.get_rect()
speed = [2, 2]

#draw on the surface object
screen.fill(GREEN)
pygame.draw.rect(screen, BLUE, (0,0,1600,450),0)


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(soccernet, (500, 220))
    screen.blit(soccerball, (800,600))
    screen.blit(messi, (830, 650))

    pygame.display.flip()



#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            #pygame.display.quit()
#            sys.exit()
#    pygame.display.update()

pygame.quit()
quit()
