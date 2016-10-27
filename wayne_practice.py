import pygame, sys
import os
from pygame.locals import *





class Ball(object):
    def __init__(self):
        self.radius = 20
        self.reset()

    def step(self):
        self.y += self.dy
        self.dy += .08
        if self.y > 480 - self.radius and self.dy > 0:
            self.dy *= -1
        self.dy *= 0.99

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, int(self.y)), self.radius)

    def draw_gauges(self, surface):
        ke = self.dy ** 2
        pe = (480 - self.y) ** 2
        pygame.draw.line(surface, RED, (10, 480), (10, 480 - int(ke * 20)), 20)
        pygame.draw.line(surface, RED, (40, 480), (40, 480 - int(pe / 10)), 20)

    def reset(self):
        self.x = 320
        self.y = 240
        self.dy = 0

    def contains_pt(self, pt):
        return (self.x - pt[0]) ** 2 + (self.y - pt[1]) ** 2 < self.radius ** 2

class BallView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.circle(surface, BLUE, (model.x, int(model.y)), model.radius)

class BallEnergyView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        ke = model.dy ** 2
        pe = (480 - model.y) ** 2
        pygame.draw.line(surface, RED, (10, 480), (10, 480 - int(ke * 20)), 20)
        pygame.draw.line(surface, RED, (40, 480), (40, 480 - int(pe / 10)), 20)

class BounceController(object):
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    model.reset()
                    break
        if event.type == pygame.KEYDOWN:
            for model in self.models:
                model.reset()


pygame.init()
display_width = 1600
display_height = 900
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Penalty Shootout!')

ball = Ball()
models = [ball]

views = []
views.append(BallView(ball))
views.append(BallEnergyView(ball))

controller = BounceController([ball])


#Represents the kicker

class kicker(object):
	def __init__(self):
		self.image=pygame.image.load('Kicker.png')
		self.x=0
		self.y=0
	def handle_keys(self):
		key = pygame.key.get_pressed()
		dist=5
		if key[pygame.K_DOWN]:
			self.y += dist
		elif key[pygame.K_UP]:
			self.y -= dist
		if key[pygame.K_Right]:
			self.x += dist
		elif key[pygame.K_Left]:
			self.x -= dist

kicker=kicker()



#set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 250,   0)
BLUE  = (  0,   0, 255)
RED = (255, 0, 0)

#loading images

soccerball = pygame.image.load('soccerball.png')
soccerball = pygame.transform.scale(soccerball, (60, 60))
kicker = pygame.image.load('Kicker.png')
kicker = pygame.transform.scale(kicker, (150, 150))
goalie = pygame.image.load('Goalie.png')
goalie = pygame.transform.scale(goalie, (175,175))
soccernet = pygame.image.load('goalnets')
soccernet = pygame.transform.scale(soccernet, (600, 250))
crowd = pygame.image.load('crowd')
crowd = pygame.transform.scale(crowd, (1600, 450))
ballrect = soccerball.get_rect()
speed = [2, 2]

#draw on the surface object
screen.fill(GREEN)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
		if ball.contains_pt(pygame.mouse.get_pos()):
			ball.reset()
		if event.type == pygame.QUIT:
                	running = False
    for model in models:
        model.step()

    

    ball.step()

    screen.blit(crowd, (0, 0))
    screen.blit(soccernet, (500, 220))
    screen.blit(soccerball, (800,600))
    screen.blit(kicker, (830, 650))
    screen.blit(goalie, (730, 350))
    ball.draw(screen)
    ball.draw_gauges(screen)
   


    pygame.display.flip()



#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            #pygame.display.quit()
#            sys.exit()
#    pygame.display.update()

pygame.quit()
quit()
