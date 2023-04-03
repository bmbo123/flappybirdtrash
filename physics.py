import pymunk
import pygame

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280,720))

space = pymunk.Space()
space.gravity  = (0,500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    space.step(1/50)
    pygame.display.flip()

    clock.tick(120)
        
