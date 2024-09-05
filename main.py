import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    fps = 60
    clock = pygame.time.Clock()
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(fps) /1000

if __name__ == "__main__":
    main()