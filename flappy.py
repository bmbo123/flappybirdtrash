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
BACKGROUND = pygame.image.load('back.png')
BACKGROUNDSCALED = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGHT+10))  
GRAVITY =5
FONT = pygame.font.SysFont("Calibri", 20)  
SCORE = 0
SCALE = 60  
FLAPPYBIRDIMAGE = pygame.image.load('picflappy.png') 
FLAPPYBIRDIMAGESCALED = pygame.transform.scale(FLAPPYBIRDIMAGE, (SCALE,SCALE)) 


class Tube:
	def  __init__(self):
		mrandom =  random.randint(100,500)
		self.top = pygame.Rect(SCREEN_WIDTH,0,100,mrandom)
		self.bottom = pygame.Rect(SCREEN_WIDTH,200+ mrandom,100,600)   

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

def checkDown(player):
	if player.y > 630: 
		pygame.quit()


arrtubes = [] 

time = 0

player = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCALE,SCALE)
while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: 
				player.y -=100     
		checkDown(player)
	SCREEN.blit(BACKGROUNDSCALED,(0,0))
	currenttime = pygame.time.get_ticks() 
	if currenttime - time > 1700:
		arrtubes.append(Tube())
		time = currenttime

	pygame.Surface.blit(SCREEN, FLAPPYBIRDIMAGESCALED, player)
	drawScreen()
	## TUBE_COLOR = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
	clock.tick(60)