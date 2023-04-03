import pygame 
from pygame import rect
import random
import time
pygame.init()
clock = pygame.time.Clock()

Screen_Width = 1280
Screen_Height = 720
SCREEN = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Fortnite")
TUBE_COLOR = (150,250,100)
ENEMY_COLOR = (250,0,100)
SPEED = 5
background = (10,20,30)
GRAVITY =5
def playeranimation(player):
    player.y += GRAVITY

def tube_animation(arrtubes):
    for tube in arrtubes:
        tube.top.x -= SPEED
        tube.bottom.x -= SPEED

class Tube:
    def  __init__(self):
        mrandom =  random.randint(100,500)
        self.top = pygame.Rect(1280,0,100,mrandom)
        self.bottom = pygame.Rect(1280,200+ mrandom,100,600)   

def rendertubes(arrtubes):
    for tube in arrtubes:
        pygame.draw.rect(SCREEN,TUBE_COLOR,tube.top)
        pygame.draw.rect(SCREEN,TUBE_COLOR,tube.bottom)



    
arrtubes = [] 

time = 0
player = pygame.Rect(1280/2, 720/2, 25,25)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP: 
                player.y += 10    
        
    SCREEN.fill(background)
    currenttime = pygame.time.get_ticks()
    if currenttime - time > 1700:
        arrtubes.append(Tube())
        time = currenttime
    pygame.draw.rect(SCREEN,ENEMY_COLOR,player)
    playeranimation(player)
    rendertubes(arrtubes)
    tube_animation(arrtubes)
    TUBE_COLOR = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
    pygame.display.update()
    clock.tick(60)


