import pygame 
from pygame import rect
import random
import time
pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fortnite")
TUBE_COLOR = (150,250,100)
ENEMY_COLOR = (250,0,100)
SPEED = 5
BACKGROUND = (10,20,30)
GRAVITY =5

class Tube:
	def  __init__(self):
		mrandom =  random.randint(100,500)
		self.top = pygame.Rect(1280,0,100,mrandom)
		self.bottom = pygame.Rect(1280,200+ mrandom,100,600)   

	def render(self):
		pygame.draw.rect(SCREEN, TUBE_COLOR, self.top)
		pygame.draw.rect(SCREEN, TUBE_COLOR, self.bottom)

	def update(self):
		self.top.x -= SPEED
		self.bottom.x -= SPEED


def rendertubes(arrtubes):
	for tube in arrtubes:
		tube.render()

def drawScreen():
	playeranimation(player)
	updateTubes(arrtubes)
	rendertubes(arrtubes)
	pygame.display.update()

def playeranimation(player):
	player.y += GRAVITY

def updateTubes(arrtubes):
	for tube in arrtubes:
		tube.update()

	
arrtubes = [] 



time = 0
player = pygame.Rect(1280/2, 720/2, 25,25)
while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: 
				player.y -=100    
		
	SCREEN.fill(BACKGROUND)
	currenttime = pygame.time.get_ticks()
	if currenttime - time > 1700:
		arrtubes.append(Tube())
		time = currenttime
	pygame.draw.rect(SCREEN,ENEMY_COLOR,player)
	drawScreen()
	## TUBE_COLOR = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
	clock.tick(60)