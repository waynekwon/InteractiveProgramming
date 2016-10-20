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

#soccerball movement

soccerball = pygame.image.load('soccerball.png')
soccerball = pygame.transform.scale(soccerball, (50, 50))
ballrect = soccerball.get_rect()
speed = [2, 2]

#draw on the surface object
screen.fill(GREEN)



running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    for i in range(10):
        screen.blit(soccerball, (800,600))
    pygame.display.flip()



#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            #pygame.display.quit()
#            sys.exit()
#    pygame.display.update()

pygame.quit()
quit()
