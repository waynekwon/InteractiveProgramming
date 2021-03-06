import pygame, sys
import os
import random
import time
from pygame.locals import *


def result(ball, goalie):
	"""If the direction of the ball and the goalie is the same, it prints 'No Goal' on the screen
	and return False. If the direction of the ball and the goalie is different, it prints 'Goal' and
	return True"""
	if ball.movement[pygame.K_LEFT] and goalie.random_direction == 1:
		screen.blit(NoGoal, (730,550))
		return False
	if ball.movement[pygame.K_UP] and goalie.random_direction == 2:
		screen.blit(NoGoal, (730,550))
		return False
	if ball.movement[pygame.K_RIGHT] and goalie.random_direction == 3:
		screen.blit(NoGoal, (730,550))
		return False
	screen.blit(Goal, (730,550))
	return True

class Ball(pygame.sprite.Sprite):
	"""Define a new class Ball that is a sprite object.
	This class has a direction, position (in x and y) and animating movement (position adjustment)"""
    
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('soccerball.png')
		self.image = pygame.transform.scale(self.image, (60, 60))
		self.x = 800
		self.y = 600
		self.reset()

	def direction(self):
		key = pygame.key.get_pressed()
		self.movement=key
		if key[pygame.K_LEFT]:
			return True
		if key[pygame.K_UP]:
			return True
		if key[pygame.K_RIGHT]:
			return True
		return False

	def step(self): #position adjustment
		self.y -= 50
		if self.movement[pygame.K_LEFT]:
			self.x -= 30
		if self.movement[pygame.K_RIGHT]:
			self.x += 30

	def reset(self): #reset the ball to its starting position
		self.x = 800
		self.y = 600

	def position(self, surface):
		surface.blit(self.image, (self.x, self.y))


class Goalie(pygame.sprite.Sprite):
	"""Define a new class Goalie that is a sprite object
	This class has a direction, position (in x and y) and animating movement (position adjustment) """
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Goalie.png')
		self.image = pygame.transform.scale(self.image, (175, 175))
		self.x = 730
		self.y = 350
		self.reset()

	def direction(self):
		random_direction = random.randint(1,3) # 1 = left, 2 = center, 3 = right
		self.random_direction=random_direction

	def step(self):
		self.y -= 10
		if self.random_direction == 1:
			self.x -= 20
		if self.random_direction == 3:
			self.x += 30

	def reset(self): #reset the goalie to its starting position
		self.x = 730
		self.y = 350

	def position(self, surface):
		surface.blit(self.image, (self.x, self.y))


class Background(object):
	"""Create a new class Background that redraws the background once the sprite objects
	move their position - reset to the default screen"""
	def __init__(self):
		self.draw(screen)

	def draw(self, surface): #loading images and adjusting the scale of the images
		surface.fill(GREEN)
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

#initialize font
myfont=pygame.font.SysFont("monospace",50)

#render text
Goal = myfont.render("GOAL!!!!", 3, (0,0,0))
NoGoal = myfont.render("NO GOAL!!!", 3, (0,0,0))


#Setting up all frames per second timing
FPS = 30
fpsClock = pygame.time.Clock()

#Setting up the display of the game
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
pygame.display.set_caption('Penalty Shootout Practice!')


#loading image for the class "Ball"
soccerball = pygame.image.load('soccerball.png')
soccerball = pygame.transform.scale(soccerball, (60, 60))

#initializing new classes
ball = Ball()
goalie = Goalie()
background = Background()


running = True
animating = False
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if animating:
	background.draw(screen)
	goalie.step()
	goalie.position(screen)
	ball.step()
	ball.position(screen)
	if ball.y <= 300:
	    #when the vertical position of the ball position is less or equal to 300, reset the position of the ball and the goalie
	    ball.reset()
	    goalie.reset()
	    animating = False
	    result(ball, goalie)
	pygame.display.update()
  	fpsClock.tick(FPS)
	continue

    ball.position(screen)

	#the goalie only starts moving once the ball starts moving
    user_choose_direction=ball.direction()
    if user_choose_direction:
	goalie.direction()
	animating = True
    background.draw(screen)
    ball.position(screen)
    goalie.position(screen)
    pygame.display.update()
    ball.reset()
    goalie.reset()
    ball.position(screen)
    goalie.position(screen)
    fpsClock.tick(FPS)


pygame.quit()
quit()
