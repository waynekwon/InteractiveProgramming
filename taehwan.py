import pygame, sys
import os
import random
from pygame.locals import *





class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('soccerball.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.x = 800
        self.y = 600
        self.reset()

    def direction(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x = 600
            self.y = 300
        if key[pygame.K_UP]:
            self.x = 800
            self.y = 300
        if key[pygame.K_RIGHT]:
            self.x = 1000
            self.y = 300

    def reset(self):
        self.x = 800
        self.y = 600

    def position(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Goalie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Goalie.png')
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.x = 730
        self.y = 350
        self.reset()

    def direction(self):
        random_direction = random.randint(1,3) # 1 = left, 2 = center, 3 = right
        if random_direction == 1:
            self.x = 500
            self.y = 300
        if random_direction == 2:
            self.x = 700
            self.y = 300
        if random_direction == 3:
            self.x = 900
            self.y = 300

    def reset(self):
        self.x = 730
        self.y = 350

    def position(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Background(object):
    def __init__(self):
        self.draw(screen)

    def draw(self, surface):
        surface.fill(GREEN)
        #loading images
    	kicker = pygame.image.load('Kicker.png')
    	kicker = pygame.transform.scale(kicker, (150, 150))
    	soccernet = pygame.image.load('goalnets.png')
    	soccernet = pygame.transform.scale(soccernet, (600, 250))
    	crowd = pygame.image.load('crowd.png')
    	crowd = pygame.transform.scale(crowd, (1600, 450))

        surface.blit(crowd, (0, 0))
        surface.blit(soccernet, (500, 220))
        surface.blit(kicker, (830, 650))



pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()
display_width = 1600
display_height = 900
size = (display_width, display_height)
screen = pygame.display.set_mode(size)


#set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 250,   0)
BLUE  = (  0,   0, 255)
RED   = (255,   0,   0)

screen.fill(GREEN)
pygame.display.set_caption('Penalty Shootout!')


#loading images
soccerball = pygame.image.load('soccerball.png')
soccerball = pygame.transform.scale(soccerball, (60, 60))


ball = Ball()
goalie = Goalie()
background = Background()






running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.position(screen)

    ball.direction()
    goalie.direction()
    background.draw(screen)
    ball.position(screen)
    goalie.position(screen)
    pygame.display.update()

    ball.reset()
    goalie.reset()
    ball.position(screen)
    goalie.position(screen)
    fpsClock.tick(FPS)




#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            #pygame.display.quit()
#            sys.exit()
#    pygame.display.update()

pygame.quit()
quit()
